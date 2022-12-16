use std::collections::HashSet;

fn main() {
    let mut state = State {
        cycle: 0,
        register: 1,
        sum: 0,
        trigger_cycles: vec![20, 60, 100, 140, 180, 220].into_iter().collect(),
    };
    common::lines("day10-1/assets/input.txt")
        .map(parse_line)
        .for_each(|op| state.execute(&op));

    println!("The sum of signal strengths is {}", state.sum);
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
