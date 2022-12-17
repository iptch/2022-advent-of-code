use std::collections::HashSet;
use std::path::Path;

fn main() {
    let res = solve("assets/day10.txt");
    println!("The sum of signal strengths is {res}");
}

pub fn solve<P>(path: P) -> isize
where
    P: AsRef<Path>,
{
    let mut state = State {
        cycle: 0,
        register: 1,
        sum: 0,
        trigger_cycles: vec![20, 60, 100, 140, 180, 220].into_iter().collect(),
    };
    common::lines(path)
        .map(parse_line)
        .for_each(|op| state.execute(&op));

    state.sum
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
    sum: isize,
    trigger_cycles: HashSet<usize>,
}

impl State {
    fn execute(&mut self, op: &Op) {
        match op {
            Op::Noop => {
                self.cycle += 1;
                self.update_sum();
            }
            Op::AddX(val) => {
                self.cycle += 1;
                self.update_sum();
                self.cycle += 1;
                self.update_sum();
                self.register += val;
            }
        }
    }

    fn update_sum(&mut self) {
        if self.trigger_cycles.contains(&self.cycle) {
            self.sum += self.register * self.cycle as isize;
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_input_solve() {
        let res = solve("../assets/day10-test.txt");
        assert_eq!(res, 13140);
    }

    #[test]
    fn test_solve() {
        let res = solve("../assets/day10.txt");
        assert_eq!(res, 13480);
    }
}
