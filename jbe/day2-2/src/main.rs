use std::path::Path;

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
    let res = solve("assets/day2.txt");
    println!("The final score is {res}");
}

pub fn solve<P>(path: P) -> u32
where
    P: AsRef<Path>,
{
    common::lines(path)
        .map(|line| get_score(line.split_once(' ').unwrap()))
        .sum()
}

fn get_score(game_round: (&str, &str)) -> u32 {
    match game_round {
        (ROCK, WIN) => PAPER_SCORE + WIN_SCORE,
        (PAPER, WIN) => SCISSORS_SCORE + WIN_SCORE,
        (SCISSORS, WIN) => ROCK_SCORE + WIN_SCORE,
        (ROCK, DRAW) => ROCK_SCORE + DRAW_SCORE,
        (PAPER, DRAW) => PAPER_SCORE + DRAW_SCORE,
        (SCISSORS, DRAW) => SCISSORS_SCORE + DRAW_SCORE,
        (ROCK, LOSE) => SCISSORS_SCORE + LOSE_SCORE,
        (PAPER, LOSE) => ROCK_SCORE + LOSE_SCORE,
        (SCISSORS, LOSE) => PAPER_SCORE + LOSE_SCORE,
        _ => panic!("not possible"),
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_input_solve() {
        let res = solve("../assets/day2-test.txt");
        assert_eq!(res, 12);
    }

    #[test]
    fn test_solve() {
        let res = solve("../assets/day2.txt");
        assert_eq!(res, 12881);
    }
}
