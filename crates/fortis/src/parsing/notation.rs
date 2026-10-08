//! Recursive-descent parser for the rule notation.
//!
//! A failed bundle is recorded and parsing continues (the bracket is one opaque token, so the
//! stream stays in sync); a structural failure stops the parse.

use super::bundles::{parse_feature_bundle, parse_pattern_bundle, parse_result_bundle};
use super::lexer::{Token, TokenInfo, lex};
use crate::models::*;

#[derive(Clone, Copy, PartialEq, Eq)]
enum Side {
    Pattern,
    Result,
}

struct Abort;

struct Parser<'a> {
    source: &'a str,
    features: &'a FeatureInventory,
    toks: Vec<TokenInfo>,
    i: usize,
    errors: Vec<String>,
}

pub fn parse_definition(source: &str, features: &FeatureInventory) -> Result<StructuralDescription, Vec<String>> {
    let mut p = Parser { source, features, toks: Vec::new(), i: 0, errors: Vec::new() };
    match lex(source) {
        Err(e) => return Err(vec![format!("{} at position {}", e.message, e.pos)]),
        Ok(toks) => p.toks = toks,
    }
    match p.definition() {
        Err(Abort) => Err(p.errors),
        Ok(sd) => {
            if p.errors.is_empty() {
                Ok(sd)
            } else {
                Err(p.errors)
            }
        }
    }
}

pub fn parse_sequence(source: &str, features: &FeatureInventory) -> Result<Vec<Element>, Vec<String>> {
    let mut p = Parser { source, features, toks: Vec::new(), i: 0, errors: Vec::new() };
    match lex(source) {
        Err(e) => return Err(vec![format!("{} at position {}", e.message, e.pos)]),
        Ok(toks) => p.toks = toks,
    }
    let result = p.sequence(&[], Side::Pattern).and_then(|seq| p.expect_end().map(|_| seq));
    match result {
        Err(Abort) => Err(p.errors),
        Ok(seq) => {
            if p.errors.is_empty() {
                Ok(seq)
            } else {
                Err(p.errors)
            }
        }
    }
}

impl Parser<'_> {
    fn definition(&mut self) -> Result<StructuralDescription, Abort> {
        let target = self.sequence(&[Token::Arrow, Token::Slash], Side::Pattern)?;
        self.expect(Token::Arrow)?;
        let result = self.sequence(&[Token::Slash], Side::Result)?;
        let mut sd = StructuralDescription { target, result, ..Default::default() };
        if self.at(Token::Slash) && !self.at_double_slash() {
            self.advance();
            let (l, r) = self.environment(&[Token::Slash])?;
            sd.left_context = l;
            sd.right_context = r;
        }
        if self.at(Token::Slash) {
            self.expect(Token::Slash)?;
            self.expect(Token::Slash)?;
            let (l, r) = self.environment(&[])?;
            sd.left_exception = l;
            sd.right_exception = r;
        }
        self.expect_end()?;
        Ok(sd)
    }

    fn environment(&mut self, right_terminators: &[Token]) -> Result<(Vec<Element>, Vec<Element>), Abort> {
        let left = self.sequence(&[Token::Focus], Side::Pattern)?;
        self.expect(Token::Focus)?;
        let right = self.sequence(right_terminators, Side::Pattern)?;
        Ok((left, right))
    }

    fn sequence(&mut self, terminators: &[Token], side: Side) -> Result<Vec<Element>, Abort> {
        let mut elements = Vec::new();
        loop {
            match self.peek() {
                None => break,
                Some(tok) if terminators.contains(&tok.kind) => break,
                _ => elements.push(self.element(side)?),
            }
        }
        Ok(elements)
    }

    fn element(&mut self, side: Side) -> Result<Element, Abort> {
        if self.at_binding() {
            let r = self.integer()?;
            self.expect(Token::Eq)?;
            return Ok(Element::Bound(r, Box::new(self.unit(side)?)));
        }
        self.unit(side)
    }

    fn unit(&mut self, side: Side) -> Result<Element, Abort> {
        let negated = self.accept(Token::Bang);
        let mut atom = self.atom(side)?;
        if negated {
            atom = Element::Negated(Box::new(atom));
        }
        let Some(tok) = self.peek() else { return Ok(atom) };
        let bounds = match tok.kind {
            Token::Star => Some((0, None)),
            Token::Plus => Some((1, None)),
            Token::QMark => Some((0, Some(1))),
            _ => None,
        };
        if let Some((min, max)) = bounds {
            self.advance();
            return Ok(Element::Quantified(Box::new(atom), Quantifier { min, max }));
        }
        if tok.kind == Token::LBrace {
            let (min, max) = self.count()?;
            return Ok(Element::Quantified(Box::new(atom), Quantifier { min, max }));
        }
        Ok(atom)
    }

    fn atom(&mut self, side: Side) -> Result<Element, Abort> {
        let Some(tok) = self.peek().cloned() else {
            return Err(self.fail("expected an element, found end of input", None));
        };
        match tok.kind {
            Token::Bundle => {
                self.advance();
                if crate::py::strip(&tok.text).is_empty() {
                    return Ok(Element::Wildcard);
                }
                Ok(self.bundle(&tok, side))
            }
            Token::Floating => {
                self.advance();
                match parse_pattern_bundle(&tok.text, self.features) {
                    Ok(bundle) => Ok(Element::FloatingAutoseg(bundle)),
                    Err(errors) => {
                        self.record(&errors, &tok);
                        Ok(Element::Wildcard)
                    }
                }
            }
            Token::At => {
                self.advance();
                Ok(Element::RecallRef(self.integer()?))
            }
            Token::Name => {
                self.advance();
                if tok.text == "∅" || tok.text == "0" {
                    return Ok(Element::Null);
                }
                if self.accept(Token::Caret) {
                    let delta_tok = self.expect(Token::Bundle)?;
                    return match parse_feature_bundle(&delta_tok.text, self.features) {
                        Ok(delta) => Ok(Element::ModifiedLetter(tok.text.clone(), delta)),
                        Err(errors) => {
                            self.record(&errors, &delta_tok);
                            Ok(Element::Wildcard)
                        }
                    };
                }
                Ok(Element::LetterRef(tok.text.clone()))
            }
            Token::Boundary => {
                self.advance();
                Ok(match tok.text.as_str() {
                    "#" => Element::WordBoundary,
                    "$" => Element::SyllableBoundary,
                    _ => Element::MorphemeBoundary,
                })
            }
            Token::LParen => self.paren(side),
            kind => Err(self.fail(&format!("unexpected {}", kind.name()), Some(&tok))),
        }
    }

    fn bundle(&mut self, tok: &TokenInfo, side: Side) -> Element {
        let parsed = match side {
            Side::Pattern => parse_pattern_bundle(&tok.text, self.features).map(Element::BundleElem),
            Side::Result => parse_result_bundle(&tok.text, self.features).map(Element::ResultElem),
        };
        match parsed {
            Ok(element) => element,
            Err(errors) => {
                self.record(&errors, tok);
                Element::Wildcard
            }
        }
    }

    fn paren(&mut self, side: Side) -> Result<Element, Abort> {
        self.expect(Token::LParen)?;
        let mut branches = vec![self.sequence(&[Token::Pipe, Token::RParen], side)?];
        while self.accept(Token::Pipe) {
            branches.push(self.sequence(&[Token::Pipe, Token::RParen], side)?);
        }
        self.expect(Token::RParen)?;
        if branches.len() == 1 {
            return Ok(Element::Group(branches.pop().unwrap()));
        }
        Ok(Element::Disjunction(branches))
    }

    fn count(&mut self) -> Result<(usize, Option<usize>), Abort> {
        let open = self.expect(Token::LBrace)?;
        let has_min = self.at(Token::Name);
        let min = if has_min { self.integer()? } else { 0 };
        let max = if self.accept(Token::Comma) {
            if self.at(Token::Name) { Some(self.integer()?) } else { None }
        } else if has_min {
            Some(min)
        } else {
            return Err(self.fail("empty count", Some(&open)));
        };
        self.expect(Token::RBrace)?;
        Ok((min.max(0) as usize, max.map(|m| m.max(0) as usize)))
    }

    fn integer(&mut self) -> Result<i64, Abort> {
        let tok = self.expect(Token::Name)?;
        match crate::py::parse_int(&tok.text) {
            Some(n) => Ok(n),
            None => Err(self.fail(
                &format!("expected an integer, found {}", crate::py::repr_str(&tok.text)),
                Some(&tok),
            )),
        }
    }

    fn peek(&self) -> Option<&TokenInfo> {
        self.toks.get(self.i)
    }

    fn at(&self, kind: Token) -> bool {
        self.peek().is_some_and(|t| t.kind == kind)
    }

    fn at_binding(&self) -> bool {
        let Some(tok) = self.peek() else { return false };
        if tok.kind != Token::Name || !crate::py::is_digit_str(&tok.text) {
            return false;
        }
        self.toks.get(self.i + 1).is_some_and(|t| t.kind == Token::Eq)
    }

    fn at_double_slash(&self) -> bool {
        self.at(Token::Slash) && self.toks.get(self.i + 1).is_some_and(|t| t.kind == Token::Slash)
    }

    fn advance(&mut self) -> TokenInfo {
        let tok = self.toks[self.i].clone();
        self.i += 1;
        tok
    }

    fn accept(&mut self, kind: Token) -> bool {
        if self.at(kind) {
            self.advance();
            return true;
        }
        false
    }

    fn expect(&mut self, kind: Token) -> Result<TokenInfo, Abort> {
        match self.peek().cloned() {
            Some(tok) if tok.kind == kind => Ok(self.advance()),
            other => {
                let found = other.as_ref().map_or("end of input", |t| t.kind.name());
                Err(self.fail(&format!("expected {}, found {found}", kind.name()), other.as_ref()))
            }
        }
    }

    fn expect_end(&mut self) -> Result<(), Abort> {
        if let Some(tok) = self.peek().cloned() {
            return Err(self.fail(&format!("unexpected trailing {}", tok.kind.name()), Some(&tok)));
        }
        Ok(())
    }

    fn record(&mut self, messages: &[String], tok: &TokenInfo) {
        for m in messages {
            self.errors.push(format!("{m} at position {}", tok.pos));
        }
    }

    fn fail(&mut self, message: &str, tok: Option<&TokenInfo>) -> Abort {
        let pos = tok.map_or_else(|| self.source.chars().count(), |t| t.pos);
        self.errors.push(format!("{message} at position {pos}"));
        Abort
    }
}
