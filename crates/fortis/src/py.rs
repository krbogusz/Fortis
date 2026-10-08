//! Helpers that reproduce Python's standard-library behaviour exactly where the reports depend
//! on it: whitespace, `int()`, `str.splitlines`, the `csv` writer, `json.dumps`, float `repr`
//! and fixed-point formatting.

use std::fmt::Write as _;

/// `str.isspace()` for one character: Unicode whitespace plus the bidi separators U+001C..U+001F.
pub fn is_space(c: char) -> bool {
    c.is_whitespace() || ('\u{1c}'..='\u{1f}').contains(&c)
}

/// `str.strip()` with no argument.
pub fn strip(s: &str) -> &str {
    s.trim_matches(is_space)
}

/// `str.isdigit()` for an ASCII-or-not string: every character a decimal digit, and non-empty.
pub fn is_digit_str(s: &str) -> bool {
    !s.is_empty() && s.chars().all(|c| c.is_ascii_digit())
}

/// `int(s)` for a decimal string: surrounding whitespace, a sign, and single underscores
/// between digits are accepted, as Python accepts them.
pub fn parse_int(s: &str) -> Option<i64> {
    let t = strip(s);
    let (neg, digits) = match t.as_bytes().first() {
        Some(b'+') => (false, &t[1..]),
        Some(b'-') => (true, &t[1..]),
        _ => (false, t),
    };
    if digits.is_empty() || digits.starts_with('_') || digits.ends_with('_') || digits.contains("__")
    {
        return None;
    }
    let cleaned: String = digits.chars().filter(|&c| c != '_').collect();
    if !cleaned.chars().all(|c| c.is_ascii_digit()) {
        return None;
    }
    let value: i64 = cleaned.parse().ok()?;
    Some(if neg { -value } else { value })
}

/// `str.splitlines()`: split on every Python line boundary, dropping the terminators.
pub fn splitlines(text: &str) -> Vec<&str> {
    let mut lines = Vec::new();
    let mut start = 0;
    let mut chars = text.char_indices().peekable();
    while let Some((i, c)) = chars.next() {
        let boundary = matches!(
            c,
            '\n' | '\r' | '\u{0b}' | '\u{0c}' | '\u{1c}' | '\u{1d}' | '\u{1e}' | '\u{85}'
                | '\u{2028}' | '\u{2029}'
        );
        if boundary {
            lines.push(&text[start..i]);
            let mut next = i + c.len_utf8();
            if c == '\r'
                && let Some(&(j, '\n')) = chars.peek() {
                    chars.next();
                    next = j + 1;
                }
            start = next;
        }
    }
    if start < text.len() {
        lines.push(&text[start..]);
    }
    lines
}

/// A cell for [`CsvWriter`]: text, or an integer written with `str()`.
pub enum Cell {
    Text(String),
    Int(i64),
}

impl From<&str> for Cell {
    fn from(s: &str) -> Self {
        Cell::Text(s.to_string())
    }
}

impl From<String> for Cell {
    fn from(s: String) -> Self {
        Cell::Text(s)
    }
}

impl From<&String> for Cell {
    fn from(s: &String) -> Self {
        Cell::Text(s.clone())
    }
}

impl From<i64> for Cell {
    fn from(n: i64) -> Self {
        Cell::Int(n)
    }
}

impl From<usize> for Cell {
    fn from(n: usize) -> Self {
        Cell::Int(n as i64)
    }
}

/// Python's `csv.writer` with the default `excel` dialect: comma-separated, `\r\n` line ends,
/// a field quoted only when it holds a comma, a quote or a line break (quotes doubled), and a
/// lone empty field written as `""`.
#[derive(Default)]
pub struct CsvWriter {
    pub out: String,
}

impl CsvWriter {
    pub fn new() -> Self {
        Self::default()
    }

    pub fn row<I, C>(&mut self, cells: I)
    where
        I: IntoIterator<Item = C>,
        C: Into<Cell>,
    {
        let cells: Vec<Cell> = cells.into_iter().map(Into::into).collect();
        let single = cells.len() == 1;
        for (i, cell) in cells.iter().enumerate() {
            if i > 0 {
                self.out.push(',');
            }
            match cell {
                Cell::Int(n) => {
                    let _ = write!(self.out, "{n}");
                }
                Cell::Text(s) => {
                    if s.is_empty() && single {
                        self.out.push_str("\"\"");
                    } else if s.contains([',', '"', '\r', '\n']) {
                        self.out.push('"');
                        self.out.push_str(&s.replace('"', "\"\""));
                        self.out.push('"');
                    } else {
                        self.out.push_str(s);
                    }
                }
            }
        }
        self.out.push_str("\r\n");
    }
}

/// Python's `repr(float)`: the shortest string that round-trips, `.0` on an integral value, and
/// an exponent form outside `1e-4 <= |x| < 1e16`.
pub fn float_repr(x: f64) -> String {
    if x.is_nan() {
        return "nan".into();
    }
    if x.is_infinite() {
        return if x > 0.0 { "inf".into() } else { "-inf".into() };
    }
    let abs = x.abs();
    if x != 0.0 && !(1e-4..1e16).contains(&abs) {
        // Rust's `{:e}` is the shortest round-trip mantissa; Python writes `1e+16`, `1.5e-05`.
        let s = format!("{x:e}");
        let (mantissa, exp) = s.split_once('e').unwrap();
        let exp: i32 = exp.parse().unwrap();
        let sign = if exp < 0 { '-' } else { '+' };
        return format!("{mantissa}e{sign}{:02}", exp.abs());
    }
    let s = format!("{x:?}");
    if s.contains('.') || s.contains('e') { s } else { format!("{s}.0") }
}

/// `f"{x:.{prec}f}"`: round half to even on the exact binary value, as Python does.
pub fn fixed(x: f64, prec: usize) -> String {
    format!("{x:.prec$}")
}

/// `f"{x:.{prec}%}"`.
pub fn percent(x: f64, prec: usize) -> String {
    format!("{}%", fixed(x * 100.0, prec))
}

/// `f"{x:+.{prec}f}"`.
pub fn signed_fixed(x: f64, prec: usize) -> String {
    let s = fixed(x, prec);
    if s.starts_with('-') { s } else { format!("+{s}") }
}

/// `json.dumps(s)` for a string, with the default `ensure_ascii=True`.
pub fn json_str(s: &str, out: &mut String) {
    out.push('"');
    for c in s.chars() {
        match c {
            '"' => out.push_str("\\\""),
            '\\' => out.push_str("\\\\"),
            '\n' => out.push_str("\\n"),
            '\r' => out.push_str("\\r"),
            '\t' => out.push_str("\\t"),
            '\u{08}' => out.push_str("\\b"),
            '\u{0c}' => out.push_str("\\f"),
            c if (c as u32) < 0x20 || (c as u32) > 0x7e => {
                let mut buf = [0u16; 2];
                for unit in c.encode_utf16(&mut buf) {
                    let _ = write!(out, "\\u{unit:04x}");
                }
            }
            c => out.push(c),
        }
    }
    out.push('"');
}

/// A JSON value written the way `json.dumps` writes it (`", "` and `": "` separators).
pub enum Json {
    Null,
    Bool(bool),
    Int(i64),
    Float(f64),
    Str(String),
    List(Vec<Json>),
    Obj(Vec<(String, Json)>),
}

impl Json {
    pub fn dump(&self, out: &mut String) {
        match self {
            Json::Null => out.push_str("null"),
            Json::Bool(b) => out.push_str(if *b { "true" } else { "false" }),
            Json::Int(n) => {
                let _ = write!(out, "{n}");
            }
            Json::Float(x) => out.push_str(&float_repr(*x)),
            Json::Str(s) => json_str(s, out),
            Json::List(items) => {
                out.push('[');
                for (i, item) in items.iter().enumerate() {
                    if i > 0 {
                        out.push_str(", ");
                    }
                    item.dump(out);
                }
                out.push(']');
            }
            Json::Obj(fields) => {
                out.push('{');
                for (i, (key, value)) in fields.iter().enumerate() {
                    if i > 0 {
                        out.push_str(", ");
                    }
                    json_str(key, out);
                    out.push_str(": ");
                    value.dump(out);
                }
                out.push('}');
            }
        }
    }

    pub fn dumps(&self) -> String {
        let mut out = String::new();
        self.dump(&mut out);
        out
    }
}

/// `textwrap.fill(text, width, initial_indent, subsequent_indent)` for space-separated words.
pub fn fill(text: &str, width: usize, initial: &str, subsequent: &str) -> String {
    let mut lines: Vec<String> = Vec::new();
    let mut line = String::new();
    let mut line_len = 0;
    for word in text.split_whitespace() {
        let indent = if lines.is_empty() { initial } else { subsequent };
        let wlen = word.chars().count();
        if line.is_empty() {
            line = format!("{indent}{word}");
            line_len = indent.chars().count() + wlen;
        } else if line_len + 1 + wlen <= width {
            line.push(' ');
            line.push_str(word);
            line_len += 1 + wlen;
        } else {
            lines.push(std::mem::take(&mut line));
            line = format!("{subsequent}{word}");
            line_len = subsequent.chars().count() + wlen;
        }
    }
    if !line.is_empty() {
        lines.push(line);
    }
    lines.join("\n")
}

/// Python's `sum()` over floats (3.12+): Neumaier-compensated after the first item.
pub fn fsum<I: IntoIterator<Item = f64>>(items: I) -> f64 {
    let mut iter = items.into_iter();
    let Some(first) = iter.next() else { return 0.0 };
    let mut total = 0.0 + first;
    let mut c = 0.0f64;
    for x in iter {
        let t = total + x;
        if total.abs() >= x.abs() {
            c += (total - t) + x;
        } else {
            c += (x - t) + total;
        }
        total = t;
    }
    if c != 0.0 && c.is_finite() {
        total += c;
    }
    total
}

/// `str.casefold()`.
pub fn casefold(s: &str) -> String {
    caseless::default_case_fold_str(s)
}

/// Whether *c* is a combining mark (`unicodedata.category(c).startswith("M")`).
pub fn is_combining(c: char) -> bool {
    use unicode_general_category::{GeneralCategory, get_general_category};
    matches!(
        get_general_category(c),
        GeneralCategory::NonspacingMark | GeneralCategory::SpacingMark | GeneralCategory::EnclosingMark
    )
}

/// Python `repr()` of a string, as used in error messages: single quotes unless the string
/// holds a single quote and no double quote.
pub fn repr_str(s: &str) -> String {
    let quote = if s.contains('\'') && !s.contains('"') { '"' } else { '\'' };
    let mut out = String::new();
    out.push(quote);
    for c in s.chars() {
        match c {
            '\\' => out.push_str("\\\\"),
            '\n' => out.push_str("\\n"),
            '\r' => out.push_str("\\r"),
            '\t' => out.push_str("\\t"),
            c if c == quote => {
                out.push('\\');
                out.push(c);
            }
            c if (c as u32) < 0x20 || c as u32 == 0x7f => {
                let _ = write!(out, "\\x{:02x}", c as u32);
            }
            c => out.push(c),
        }
    }
    out.push(quote);
    out
}

/// Length in code points (Python's `len` on a `str`).
pub fn char_len(s: &str) -> usize {
    s.chars().count()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn floats_print_as_python_repr() {
        assert_eq!(float_repr(135.0), "135.0");
        assert_eq!(float_repr(0.1), "0.1");
        assert_eq!(float_repr(1e16), "1e+16");
        assert_eq!(float_repr(1.5e-5), "1.5e-05");
    }

    #[test]
    fn fixed_rounds_half_to_even() {
        assert_eq!(fixed(0.125, 2), "0.12");
        assert_eq!(fixed(2.5, 0), "2");
        assert_eq!(percent(0.9755, 1), "97.5%");
    }

    #[test]
    fn csv_quotes_like_python() {
        let mut w = CsvWriter::new();
        w.row(["a,b", "c\"d", "", "e"]);
        w.row([""]);
        assert_eq!(w.out, "\"a,b\",\"c\"\"d\",,e\r\n\"\"\r\n");
    }
}
