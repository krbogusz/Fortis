//! Lexer for the rule notation. Vocabulary-free: a `[...]` bundle is one opaque token, and a
//! NAME is any maximal run of characters that are neither whitespace nor structural punctuation.

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum Token {
    Arrow,
    Slash,
    Focus,
    LParen,
    RParen,
    LBrace,
    RBrace,
    Comma,
    Star,
    Plus,
    QMark,
    Pipe,
    Bang,
    Eq,
    At,
    Caret,
    Bundle,
    Floating,
    Boundary,
    Name,
}

impl Token {
    /// The token's name as Python's `Token.<NAME>.name` spells it, for error messages.
    pub fn name(self) -> &'static str {
        match self {
            Token::Arrow => "ARROW",
            Token::Slash => "SLASH",
            Token::Focus => "FOCUS",
            Token::LParen => "LPAREN",
            Token::RParen => "RPAREN",
            Token::LBrace => "LBRACE",
            Token::RBrace => "RBRACE",
            Token::Comma => "COMMA",
            Token::Star => "STAR",
            Token::Plus => "PLUS",
            Token::QMark => "QMARK",
            Token::Pipe => "PIPE",
            Token::Bang => "BANG",
            Token::Eq => "EQ",
            Token::At => "AT",
            Token::Caret => "CARET",
            Token::Bundle => "BUNDLE",
            Token::Floating => "FLOATING",
            Token::Boundary => "BOUNDARY",
            Token::Name => "NAME",
        }
    }
}

#[derive(Clone, Debug)]
pub struct TokenInfo {
    pub kind: Token,
    pub text: String,
    /// Code-point offset of the token's start.
    pub pos: usize,
}

pub struct LexError {
    pub message: String,
    pub pos: usize,
}

fn single(c: char) -> Option<Token> {
    Some(match c {
        '/' => Token::Slash,
        '_' => Token::Focus,
        '(' => Token::LParen,
        ')' => Token::RParen,
        '{' => Token::LBrace,
        '}' => Token::RBrace,
        ',' => Token::Comma,
        '*' => Token::Star,
        '+' => Token::Plus,
        '?' => Token::QMark,
        '|' => Token::Pipe,
        '!' => Token::Bang,
        '=' => Token::Eq,
        '@' => Token::At,
        '^' => Token::Caret,
        _ => return None,
    })
}

fn is_stop(c: char) -> bool {
    crate::py::is_space(c)
        || single(c).is_some()
        || matches!(c, '#' | '$' | '[' | ']' | '⟨' | '⟩' | '→' | '-')
}

pub fn lex(source: &str) -> Result<Vec<TokenInfo>, LexError> {
    let chars: Vec<char> = source.chars().collect();
    let n = chars.len();
    let mut tokens = Vec::new();
    let mut i = 0;
    let text = |a: usize, b: usize| chars[a..b].iter().collect::<String>();
    let find = |c: char, from: usize| (from..n).find(|&j| chars[j] == c);
    while i < n {
        let ch = chars[i];
        if crate::py::is_space(ch) {
            i += 1;
            continue;
        }
        if ch == '→' {
            tokens.push(TokenInfo { kind: Token::Arrow, text: ch.to_string(), pos: i });
            i += 1;
            continue;
        }
        if ch == '-' {
            if i + 1 < n && chars[i + 1] == '>' {
                tokens.push(TokenInfo { kind: Token::Arrow, text: "->".into(), pos: i });
                i += 2;
                continue;
            }
            tokens.push(TokenInfo { kind: Token::Boundary, text: "-".into(), pos: i });
            i += 1;
            continue;
        }
        if ch == '[' {
            let Some(close) = find(']', i + 1) else {
                return Err(LexError { message: "unterminated feature bundle".into(), pos: i });
            };
            tokens.push(TokenInfo { kind: Token::Bundle, text: text(i + 1, close), pos: i });
            i = close + 1;
            continue;
        }
        if ch == ']' {
            return Err(LexError { message: "']' with no matching '['".into(), pos: i });
        }
        if ch == '⟨' {
            let Some(close) = find('⟩', i + 1) else {
                return Err(LexError { message: "unterminated floating autosegment".into(), pos: i });
            };
            tokens.push(TokenInfo { kind: Token::Floating, text: text(i + 1, close), pos: i });
            i = close + 1;
            continue;
        }
        if ch == '⟩' {
            return Err(LexError { message: "'⟩' with no matching '⟨'".into(), pos: i });
        }
        if ch == '#' || ch == '$' {
            tokens.push(TokenInfo { kind: Token::Boundary, text: ch.to_string(), pos: i });
            i += 1;
            continue;
        }
        if let Some(kind) = single(ch) {
            tokens.push(TokenInfo { kind, text: ch.to_string(), pos: i });
            i += 1;
            continue;
        }
        let start = i;
        while i < n && !is_stop(chars[i]) {
            i += 1;
        }
        tokens.push(TokenInfo { kind: Token::Name, text: text(start, i), pos: start });
    }
    Ok(tokens)
}
