#![feature(array_windows)]
use std::path::Path;

use std::collections::HashSet;

const WINDOW_SIZE: usize = 14;

fn main() {
    let res = solve("assets/day6.txt");
    println!("The first marker appears on position: {res}");
}

pub fn solve<P>(path: P) -> usize
where
    P: AsRef<Path>,
{
    let line = common::lines(path).next().unwrap();
    let chars: Vec<char> = line.chars().collect();
    chars
        .array_windows::<WINDOW_SIZE>()
        .enumerate()
        .find(|(_, slice)| uniq(*slice))
        .map(|(idx, _)| idx + WINDOW_SIZE)
        .unwrap()
}

fn uniq(slice: &[char]) -> bool {
    let mut unique = HashSet::new();
    slice.iter().all(move |x| unique.insert(x))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_input_solve() {
        let res = solve("../assets/day6-test.txt");
        assert_eq!(res, 19);
    }

    #[test]
    fn test_solve() {
        let res = solve("../assets/day6.txt");
        assert_eq!(res, 2145);
    }
}
