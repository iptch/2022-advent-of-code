use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

pub fn read_lines<P>(filename: P) -> impl Iterator<Item=String> where P: AsRef<Path> {
    let file = File::open(filename).unwrap();
    let reader = io::BufReader::new(file);
    reader.lines().map(|x| x.unwrap())
}