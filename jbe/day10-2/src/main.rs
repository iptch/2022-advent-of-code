use std::path::Path;

const SCREEN_WIDTH: usize = 40;

fn main() {
    let res = solve("assets/day10.txt");
    println!("The screen displays:\n{res}");
}

pub fn solve<P>(path: P) -> String
where
    P: AsRef<Path>,
{
    let mut state = State {
        cycle: 0,
        register: 1,
    };
    common::lines(path)
        .map(parse_line)
        .map(|op| state.execute(&op))
        .collect::<Vec<Vec<char>>>()
        .concat()
        .chunks(SCREEN_WIDTH)
        .map(|c| c.iter().collect::<String>())
        .collect::<Vec<String>>()
        .join("\n")
}

fn parse_line(line: String) -> Op {
    match line.as_str() {
        "noop" => Op::Noop,
        _ => {
            let (_, val) = line.split_once(' ').unwrap();
            Op::AddX(val.parse().unwrap())
        }
    }
}

enum Op {
    Noop,
    AddX(isize),
}

struct State {
    cycle: usize,
    register: isize,
}

impl State {
    fn execute(&mut self, op: &Op) -> Vec<char> {
        match op {
            Op::Noop => {
                self.cycle += 1;
                vec![self.draw()]
            }
            Op::AddX(val) => {
                self.cycle += 1;
                let mut res = vec![self.draw()];
                self.cycle += 1;
                res.push(self.draw());
                self.register += val;
                res
            }
        }
    }

    fn draw(&self) -> char {
        let pos = (self.cycle % SCREEN_WIDTH) as isize;
        if pos >= self.register && pos < self.register + 3 {
            '#'
        } else {
            '.'
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_input_solve() {
        let res = solve("../assets/day10-test.txt");
        let expected = "##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......###.
#######.......#######.......#######.....";
        assert_eq!(res, expected);
    }

    #[test]
    fn test_solve() {
        let res = solve("../assets/day10.txt");
        let expected = "####..##....##.###...##...##..####.#..#.
#....#..#....#.#..#.#..#.#..#.#....#.#..
###..#.......#.###..#....#....###..##...
#....#.##....#.#..#.#.##.#....#....#.#..
#....#..#.#..#.#..#.#..#.#..#.#....#.#..
####..###..##..###...###..##..#....#..#.";
        assert_eq!(res, expected);
    }
}
