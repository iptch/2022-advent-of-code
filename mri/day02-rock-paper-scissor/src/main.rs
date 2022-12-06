use common::read_lines;

fn main() {
    let mut score = 0;
    let mut score2 = 0;

    for line in read_lines("assets/input.txt") {
        let opponent: char = line.chars().nth(0).unwrap();
        let you: char = line.chars().nth(2).unwrap();

        score += calc_score(opponent, you);
        score2 += calc_score_2(opponent, you);
    }

    println!("score: {}", score);
    println!("score 2: {}", score2)
}

fn calc_score_2(opponent: char, you: char) -> u32 {
    let mut score = 0;
    match you {
        'X' => { // lose
            match opponent {
                'A' => score += 3,
                'B' => score += 1,
                'C' => score += 2,
                _ => eprintln!("Unknown shape: {}", opponent),
            };
        },
        'Y' => { // draw
            score += 3;
            match opponent {
                'A' => score += 1,
                'B' => score += 2,
                'C' => score += 3,
                _ => eprintln!("Unknown shape: {}", opponent),
            }
        }
        'Z' => { // win
            score += 6;
            match opponent {
                'A' => score += 2,
                'B' => score += 3,
                'C' => score += 1,
                _ => eprintln!("Unknown shape: {}", opponent),
            }
        }
        _ => eprintln!("Unknown shape: {}", you),
    };
    score
}

fn calc_score(opponent: char, you: char) -> u32 {
    let mut score = 0;
    match you {
        'X' => {
            score += 1;
            match opponent {
                'A' => score += 3,
                'B' => (),
                'C' => score += 6,
                _ => eprintln!("Unknown shape: {}", opponent),
            };
        },
        'Y' => {
            score += 2;
            match opponent {
                'A' => score += 6,
                'B' => score += 3,
                'C' => (),
                _ => eprintln!("Unknown shape: {}", opponent),
            }
        }
        'Z' => {
            score += 3;
            match opponent {
                'A' => (),
                'B' => score += 6,
                'C' => score += 3,
                _ => eprintln!("Unknown shape: {}", opponent),
            }
        }
        _ => eprintln!("Unknown shape: {}", you),
    };
    score
}
