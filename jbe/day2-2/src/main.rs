const ROCK: &str = "A";
const PAPER: &str = "B";
const SCISSORS: &str = "C";

const LOSE: &str = "X";
const DRAW: &str = "Y";
const WIN: &str = "Z";

const ROCK_SCORE: u32 = 1;
const PAPER_SCORE: u32 = 2;
const SCISSORS_SCORE: u32 = 3;

const WIN_SCORE: u32 = 6;
const DRAW_SCORE: u32 = 3;
const LOSE_SCORE: u32 = 0;

fn main() {
    let sum: u32 = common::lines("day2-2/assets/input.txt")
        .map(|line| get_score(line.split_once(' ').unwrap()))
        .sum();
    println!("The final score is {sum}");
}

fn get_score(game_round: (&str, &str)) -> u32 {
    match game_round {
        (ROCK,     WIN)  => PAPER_SCORE    + WIN_SCORE,
        (PAPER,    WIN)  => SCISSORS_SCORE + WIN_SCORE,
        (SCISSORS, WIN)  => ROCK_SCORE     + WIN_SCORE,
        (ROCK,     DRAW) => ROCK_SCORE     + DRAW_SCORE,
        (PAPER,    DRAW) => PAPER_SCORE    + DRAW_SCORE,
        (SCISSORS, DRAW) => SCISSORS_SCORE + DRAW_SCORE,
        (ROCK,     LOSE) => SCISSORS_SCORE + LOSE_SCORE,
        (PAPER,    LOSE) => ROCK_SCORE     + LOSE_SCORE,
        (SCISSORS, LOSE) => PAPER_SCORE    + LOSE_SCORE,
        _                => panic!("not possible"),
    }
}
