use lazy_static::lazy_static;
use regex::Regex;
use std::collections::LinkedList;

fn main() {
    let stack_def: Vec<String> = common::lines("day5-1/assets/input.txt")
        .take_while(|line| !line.is_empty())
        .collect();
    let mut stacks = parse_stacks(stack_def);
    common::lines("day5-1/assets/input.txt")
        .skip_while(|line| !line.starts_with("move"))
        .map(|line| parse_instruction(&line))
        .for_each(|instr| instr.exec(&mut stacks));
    let stacks_top = stacks
        .iter()
        .filter_map(|stack| stack.front())
        .fold(String::new(), |acc, ch| format!("{acc}{ch}"));
    println!("The top of the stacks is: {stacks_top}");

}

struct Move {
    from: usize,
    to: usize,
    count: usize,
}

impl Move {
    fn exec(&self, state: &mut [LinkedList<char>]) {
        for _ in 0..self.count {
            if let Some(val) = state[self.from - 1].pop_front() {
                state[self.to - 1].push_front(val);
            }
        }
    }
}

fn parse_instruction(line: &str) -> Move {
    lazy_static! {
        static ref RE: Regex =
            Regex::new(r"move (?P<count>\d+) from (?P<from>\d+) to (?P<to>\d+)").unwrap();
    }
    let caps = RE.captures(line).unwrap();
    Move {
        count: caps.name("count").unwrap().as_str().parse().unwrap(),
        from: caps.name("from").unwrap().as_str().parse().unwrap(),
        to: caps.name("to").unwrap().as_str().parse().unwrap(),
    }
}

fn parse_stacks(mut lines: Vec<String>) -> Vec<LinkedList<char>> {
    let last_id: usize = lines
        .last()
        .unwrap()
        .split_whitespace()
        .last()
        .unwrap()
        .parse()
        .unwrap();
    let _ = lines.pop();
    lines.reverse();

    let mut res = vec![LinkedList::new(); last_id];
    for line in lines {
        for idx in 0..last_id {
            let pos = 1 + idx * 4;
            let chr = line.chars().nth(pos).unwrap();
            if !chr.is_whitespace() {
                res[idx].push_front(chr);
            }
        }
    }

    res
}
