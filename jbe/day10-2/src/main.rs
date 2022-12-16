const SCREEN_WIDTH: usize = 40;

fn main() {
    let mut state = State {
        cycle: 0,
        register: 1,
    };
    common::lines("day10-2/assets/input.txt")
        .map(parse_line)
        .map(|op| state.execute(&op))
        .collect::<Vec<Vec<char>>>()
        .concat()
        .chunks(SCREEN_WIDTH)
        .map(|c| c.iter().collect::<String>())
        .for_each(|line| println!("{line}"));
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
