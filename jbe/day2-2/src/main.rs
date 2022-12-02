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
    let sum: u32 = common::lines("day2-2/assets/input.txt")
        .map(|line| get_score(line.split_once(' ').unwrap()))
        .sum();
    println!("The final score is {}", sum);
}

fn get_score((other, result): (&str, &str)) -> u32 {
    match result {
        WIN => {
            6 + match other {
                ROCK     => PAPER_SCORE,
                PAPER    => SCISSORS_SCORE,
                SCISSORS => ROCK_SCORE,
                _        => panic!("not possible"),
            }
        },
        DRAW => {
            3 + match other {
                ROCK     => ROCK_SCORE,
                PAPER    => PAPER_SCORE,
                SCISSORS => SCISSORS_SCORE,
                _        => panic!("not possible"),
            }
        },
        LOSE => {
            match other {
                ROCK     => SCISSORS_SCORE,
                PAPER    => ROCK_SCORE,
                SCISSORS => PAPER_SCORE,
                _        => panic!("not possible"),
            }
        },
        _ => panic!("not possible"),
    }
}
