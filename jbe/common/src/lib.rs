use std::fs::File;
use std::io::{BufRead, BufReader};
use std::path::Path;

pub fn lines<P>(path: P) -> impl Iterator<Item=String> where P: AsRef<Path> {
    let file = File::open(path).unwrap();
    let reader = BufReader::new(file);
    reader.lines().map(|x| x.unwrap())
}

