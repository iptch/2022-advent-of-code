#![feature(iter_array_chunks)]

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
    println!("The sum of indices in the right order is: {res}");
}

pub fn solve<P>(path: P) -> usize
where
    P: AsRef<Path>,
{
    common::lines(path)
        .filter_map(|line| Element::parse(&mut line.chars().peekable()))
        .array_chunks()
        .enumerate()
        .filter_map(
            |(idx, [left, right])| {
                if left <= right {
                    Some(idx + 1)
                } else {
                    None
                }
            },
        )
        .sum()
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
            (left, right) => left.into_list().cmp(&right.into_list()),
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
            (left, right) => left.into_list() == right.into_list(),
        }
    }
}

impl Element {
    fn into_list(&self) -> Element {
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
        assert_eq!(res, 13);
    }

    #[test]
    fn parse_simple_integer() {
        let mut input = "123".chars().peekable();
        assert_eq!(Element::parse(&mut input), Some(Element::Integer(123)));
    }

    #[test]
    fn parse_simple_list() {
        let mut input = "[1,2,3]".chars().peekable();
        let expected = Element::List(vec![
            Element::Integer(1),
            Element::Integer(2),
            Element::Integer(3),
        ]);
        assert_eq!(Element::parse(&mut input), Some(expected));
    }

    #[test]
    fn parse_simple_list_of_lists() {
        let mut input = "[[1,2,3]]".chars().peekable();
        let expected = Element::List(vec![Element::List(vec![
            Element::Integer(1),
            Element::Integer(2),
            Element::Integer(3),
        ])]);
        assert_eq!(Element::parse(&mut input), Some(expected));
    }

    #[test]
    fn parse_longer_list_of_lists() {
        let mut input = "[[1,2,3],[4,5,6]]".chars().peekable();
        let expected = Element::List(vec![
            Element::List(vec![
                Element::Integer(1),
                Element::Integer(2),
                Element::Integer(3),
            ]),
            Element::List(vec![
                Element::Integer(4),
                Element::Integer(5),
                Element::Integer(6),
            ]),
        ]);
        assert_eq!(Element::parse(&mut input), Some(expected));
    }

    #[test]
    fn parse_longer_mixed_list_of_lists() {
        let mut input = "[[1,2,3],789,[4,5,6],[[]]]".chars().peekable();
        let expected = Element::List(vec![
            Element::List(vec![
                Element::Integer(1),
                Element::Integer(2),
                Element::Integer(3),
            ]),
            Element::Integer(789),
            Element::List(vec![
                Element::Integer(4),
                Element::Integer(5),
                Element::Integer(6),
            ]),
            Element::List(vec![Element::List(vec![])]),
        ]);
        assert_eq!(Element::parse(&mut input), Some(expected));
    }

    #[test]
    fn comparison_int_list() {
        let mut left_in = "[123]".chars().peekable();
        let mut right_in = "123".chars().peekable();
        let left = Element::parse(&mut left_in);
        let right = Element::parse(&mut right_in);
        assert_eq!(left.cmp(&right), std::cmp::Ordering::Equal);
    }

    #[test]
    fn comparison_lists_less() {
        let mut left_in = "[[1],[2,3,4]]".chars().peekable();
        let mut right_in = "[[1],4]".chars().peekable();
        let left = Element::parse(&mut left_in);
        let right = Element::parse(&mut right_in);
        assert_eq!(left.cmp(&right), std::cmp::Ordering::Less);
    }

    #[test]
    fn comparison_lists_greater() {
        let mut left_in = "[9]".chars().peekable();
        let mut right_in = "[[8,7,6]]".chars().peekable();
        let left = Element::parse(&mut left_in);
        let right = Element::parse(&mut right_in);
        assert_eq!(left.cmp(&right), std::cmp::Ordering::Greater);
    }

    #[test]
    fn comparison_empty_lists() {
        let mut left_in = "[]".chars().peekable();
        let mut right_in = "[]".chars().peekable();
        let left = Element::parse(&mut left_in);
        let right = Element::parse(&mut right_in);
        assert_eq!(left.cmp(&right), std::cmp::Ordering::Equal);
    }

    #[test]
    fn comparison_lists_of_empty_lists() {
        let mut left_in = "[[[]]]".chars().peekable();
        let mut right_in = "[[]]".chars().peekable();
        let left = Element::parse(&mut left_in);
        let right = Element::parse(&mut right_in);
        assert_eq!(left.cmp(&right), std::cmp::Ordering::Greater);
    }
}
