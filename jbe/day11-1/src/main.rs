#![feature(iter_next_chunk)]

use std::collections::HashMap;
use std::path::Path;

use lazy_static::lazy_static;
use regex::Regex;

const ROUNDS: usize = 20;
const PATTERN: &str = r"Monkey (?P<id>\d+):\s+Starting items: (?P<items>(?:\d+, )*\d+)+\s+Operation: new = old (?P<op>\S+ \S+)\s+Test: divisible by (?P<test>\d+)\s+If true: throw to monkey (?P<true>\d+)\s+If false: throw to monkey (?P<false>\d+)";
lazy_static! {
    static ref MONKEY: Regex = Regex::new(PATTERN).unwrap();
}

fn main() {
    let res = solve("assets/day11.txt");
    println!("Monkey business level is: {res}");
}

pub fn solve<P>(path: P) -> usize
where
    P: AsRef<Path>,
{
    let mut lines = common::lines(path);
    let mut monkeys: HashMap<usize, Monkey> = HashMap::new();
    while let Ok(chunk) = lines.next_chunk::<6>() {
        let (id, monkey) = Monkey::from(chunk.concat());
        monkeys.insert(id, monkey);
        lines.next();
    }
    let monkey_count = monkeys.len();
    for _ in 0..ROUNDS {
        for idx in 0..monkey_count {
            let thows = monkeys.get_mut(&idx).unwrap().play();
            thows
                .into_iter()
                .for_each(|(id, item)| monkeys.get_mut(&id).unwrap().items.push(item));
        }
    }
    let mut monkeys: Vec<Monkey> = monkeys.into_values().collect();
    monkeys.sort_by_key(|monkey| monkey.inspections);
    monkeys.reverse();
    monkeys[0].inspections * monkeys[1].inspections
}

struct Monkey {
    items: Vec<usize>,
    operation: Operation,
    test: usize,
    passed: usize,
    failed: usize,
    inspections: usize,
}

impl Monkey {
    fn from(input: String) -> (usize, Monkey) {
        let caps = MONKEY.captures(&input).unwrap();
        let id = caps.name("id").unwrap().as_str().parse().unwrap();
        let items = caps
            .name("items")
            .unwrap()
            .as_str()
            .split(", ")
            .map(|x| x.parse().unwrap())
            .collect();
        let op = caps.name("op").unwrap().as_str();
        let operation = Operation::from(op);
        let test = caps.name("test").unwrap().as_str().parse().unwrap();
        let passed = caps.name("true").unwrap().as_str().parse().unwrap();
        let failed = caps.name("false").unwrap().as_str().parse().unwrap();

        (
            id,
            Monkey {
                items,
                operation,
                test,
                passed,
                failed,
                inspections: 0,
            },
        )
    }

    fn play(&mut self) -> Vec<(usize, usize)> {
        let mut res = Vec::new();
        for item in self.items.iter() {
            self.inspections += 1;
            let worry_level = self.operation.execute(*item);
            let bored_level = worry_level / 3;
            if bored_level % self.test == 0 {
                res.push((self.passed, bored_level));
            } else {
                res.push((self.failed, bored_level));
            }
        }
        self.items = Vec::new();
        res
    }
}

enum Operation {
    Add(usize),
    Multiply(usize),
    Power2,
    Double,
}

impl Operation {
    fn from(input: &str) -> Operation {
        match input.split_once(' ').unwrap() {
            ("+", "old") => Operation::Double,
            ("*", "old") => Operation::Power2,
            ("+", val) => Operation::Add(val.parse().unwrap()),
            ("*", val) => Operation::Multiply(val.parse().unwrap()),
            _ => panic!("unsupported operation"),
        }
    }

    fn execute(&self, on: usize) -> usize {
        match self {
            Operation::Add(val) => val + on,
            Operation::Multiply(val) => val * on,
            Operation::Double => on + on,
            Operation::Power2 => on * on,
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_input_solve() {
        let res = solve("../assets/day11-test.txt");
        assert_eq!(res, 10605);
    }

    #[test]
    fn test_solve() {
        let res = solve("../assets/day11.txt");
        assert_eq!(res, 98280);
    }
}
