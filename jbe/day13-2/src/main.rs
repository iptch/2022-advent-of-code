use lazy_static::lazy_static;

use std::collections::HashSet;
use std::iter::Peekable;
use std::path::Path;

const LIST_OPEN: char = '[';
const LIST_CLOSE: char = ']';
const SEP: char = ',';

lazy_static! {
    static ref NON_DIGIT: HashSet<char> = vec![LIST_CLOSE, LIST_OPEN, SEP].into_iter().collect();
}

fn main() {
    let res = solve("assets/day13.txt");
    println!("The decoder key is {res}");
}

pub fn solve<P>(path: P) -> isize
where
    P: AsRef<Path>,
{
    let dividers = vec!["[[2]]", "[[6]]"]
        .into_iter()
        .filter_map(|line| Element::parse(&mut line.chars().peekable()));
    let mut lists: Vec<Element> = common::lines(path)
        .filter_map(|line| Element::parse(&mut line.chars().peekable()))
        .chain(dividers.clone())
        .collect();
    lists.sort();
    let mut decoder_key = 1;
    for divider in dividers {
        decoder_key *= lists.iter().position(|elem| *elem == divider).unwrap() as isize + 1;
    }
    decoder_key
}

#[derive(Eq, Debug, Clone)]
enum Element {
    Integer(u32),
    List(Vec<Element>),
}

impl Ord for Element {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        match (self, other) {
            (Element::Integer(left), Element::Integer(right)) => left.cmp(right),
            (Element::List(left), Element::List(right)) => {
                for (left_elem, right_elem) in left.iter().zip(right.iter()) {
                    if left_elem != right_elem {
                        return left_elem.cmp(right_elem);
                    }
                }
                left.len().cmp(&right.len())
            }
            (left, right) => left.as_list().cmp(&right.as_list()),
        }
    }
}

impl PartialOrd for Element {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

impl PartialEq for Element {
    fn eq(&self, other: &Self) -> bool {
        match (self, other) {
            (Element::Integer(left), Element::Integer(right)) => left == right,
            (Element::List(left), Element::List(right)) => left == right,
            (left, right) => left.as_list() == right.as_list(),
        }
    }
}

impl Element {
    fn as_list(&self) -> Element {
        match self {
            Element::List(_) => self.clone(),
            Element::Integer(_) => Element::List(vec![self.clone()]),
        }
    }

    fn parse<T>(input: &mut Peekable<T>) -> Option<Element>
    where
        T: Iterator<Item = char>,
    {
        if let Some(ch) = input.next() {
            if ch == LIST_OPEN {
                let mut res = Vec::new();
                while *input.peek().unwrap() != LIST_CLOSE {
                    res.push(Self::parse(input).unwrap());
                    // skip potential separator
                    if *input.peek().unwrap() == SEP {
                        input.next();
                    }
                }
                // skip closing
                input.next();
                Some(Element::List(res))
            } else {
                let mut digits = vec![ch];
                while !NON_DIGIT.contains(input.peek().unwrap_or(&',')) {
                    digits.push(input.next().unwrap());
                }
                Some(Element::Integer(
                    digits.iter().collect::<String>().parse().unwrap(),
                ))
            }
        } else {
            None
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solve() {
        let res = solve("../assets/day13-test.txt");
        assert_eq!(res, 140);
    }
}
