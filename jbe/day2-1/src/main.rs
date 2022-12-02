const ROCK: &str = "A";
const PAPER: &str = "B";
const SCISSORS: &str = "C";

const ROCK_ME: &str = "X";
const PAPER_ME: &str = "Y";
const SCISSORS_ME: &str = "Z";

const ROCK_SCORE: u32 = 1;
const PAPER_SCORE: u32 = 2;
const SCISSORS_SCORE: u32 = 3;

const WIN_SCORE: u32 = 6;
const DRAW_SCORE: u32 = 3;
const LOSE_SCORE: u32 = 0;

fn main() {
    let mut sum = 0;
    for line in common::lines("day2-1/assets/input.txt") {
        let (other, me) = line.split_once(' ').unwrap();
        sum += get_score(other, me)
    }
    println!("The final score is {}", sum);
}

fn get_score(other: &str, me: &str) -> u32 {
    match (other, me) {
        (ROCK,     ROCK_ME)     => ROCK_SCORE     + DRAW_SCORE,
        (SCISSORS, ROCK_ME)     => ROCK_SCORE     + WIN_SCORE,
        (PAPER,    ROCK_ME)     => ROCK_SCORE     + LOSE_SCORE,
        (ROCK,     PAPER_ME)    => PAPER_SCORE    + WIN_SCORE,
        (SCISSORS, PAPER_ME)    => PAPER_SCORE    + LOSE_SCORE,
        (PAPER,    PAPER_ME)    => PAPER_SCORE    + DRAW_SCORE,
        (ROCK,     SCISSORS_ME) => SCISSORS_SCORE + LOSE_SCORE,
        (PAPER,    SCISSORS_ME) => SCISSORS_SCORE + WIN_SCORE,
        (SCISSORS, SCISSORS_ME) => SCISSORS_SCORE + DRAW_SCORE,
        _                       => panic!("not possible"),
    }
}
