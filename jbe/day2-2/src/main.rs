use std::fs::File;
use std::io::{BufRead, BufReader};

const ROCK: &str = "A";
const PAPER: &str = "B";
const SCISSORS: &str = "C";

const LOSE: &str = "X";
const DRAW: &str = "Y";
const WIN: &str = "Z";

const ROCK_SCORE: u32 = 1;
const PAPER_SCORE: u32 = 2;
const SCISSORS_SCORE: u32 = 3;

fn main() {
    let filename = "assets/input.txt";
    let file = File::open(filename).unwrap();
    let reader = BufReader::new(file);

    let mut sum = 0;
    for line in reader.lines() {
        let line = line.unwrap();
        let (other, res) = line.split_once(" ").unwrap();
        sum += get_score(other, res)
    }
    println!("The final score is {}", sum);
}

fn get_score(other: &str, result: &str) -> u32 {
    match result {
        WIN => {
            6 + match other {
                ROCK => PAPER_SCORE,
                PAPER => SCISSORS_SCORE,
                SCISSORS => ROCK_SCORE,
                _ => panic!("not possible"),
            }
        },
        DRAW => {
            3 + match other {
                ROCK => ROCK_SCORE,
                PAPER => PAPER_SCORE,
                SCISSORS => SCISSORS_SCORE,
                _ => panic!("not possible"),
            }
        },
        LOSE => {
            match other {
                ROCK => SCISSORS_SCORE,
                PAPER => ROCK_SCORE,
                SCISSORS => PAPER_SCORE,
                _ => panic!("not possible"),
            }
        },
        _ => panic!("not possible"),
    }
}
