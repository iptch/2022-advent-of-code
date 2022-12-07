#![feature(array_windows)]

use std::collections::HashSet;

const WINDOW_SIZE: usize = 4;

fn main() {
    let line = common::lines("day6-1/assets/input.txt").next().unwrap();
    let chars: Vec<char> = line.chars().collect();
    let index: usize = chars
        .array_windows::<WINDOW_SIZE>()
        .enumerate()
        .find(|(_, slice)| uniq(*slice))
        .map(|(idx, _)| idx + WINDOW_SIZE)
        .unwrap();
    println!("The first marker appears on position: {index}");
}

fn uniq(slice: &[char]) -> bool {
    let mut unique = HashSet::new();
    slice.iter().all(move |x| unique.insert(x))
}
