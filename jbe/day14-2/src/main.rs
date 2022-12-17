#![feature(array_windows)]

use std::collections::HashSet;
use std::path::Path;

fn main() {
    let res = solve("assets/day14.txt");
    println!("There are {res} grains of sand");
}

pub fn solve<P>(path: P) -> usize
where
    P: AsRef<Path>,
{
    let rock_lines: Vec<RockLine> = common::lines(path)
        .map(parse_line)
        .map(extrapolate_rockline)
        .collect();
    let floor = lowerst_rock(&rock_lines) + 1;
    let mut sand: Sand = rock_lines.into_iter().flatten().collect();
    let rock_count = sand.len();
    loop {
        let final_state = Point::sand_origin().fall(&sand, floor);
        if final_state == Point::sand_origin() {
            sand.insert(final_state);
            break;
        }
        sand.insert(final_state);
    }
    sand.len() - rock_count
}

#[derive(PartialEq, Eq, Hash, Clone, Debug)]
struct Point {
    x: usize,
    y: usize,
}

impl Point {
    fn from(input: &str) -> Self {
        let (x, y) = input.split_once(',').unwrap();
        Point {
            x: x.parse().unwrap(),
            y: y.parse().unwrap(),
        }
    }

    fn sand_origin() -> Self {
        Point { x: 500, y: 0 }
    }

    fn fall(mut self, sand: &Sand, floor: usize) -> Point {
        while self.move_down(sand) {
            if self.y == floor {
                return self;
            }
        }
        self
    }

    fn move_down(&mut self, sand: &Sand) -> bool {
        self.y += 1;
        if sand.contains(self) {
            self.x -= 1;
            if sand.contains(self) {
                self.x += 2;
                if sand.contains(self) {
                    self.y -= 1;
                    self.x -= 1;
                    return false;
                }
            }
        }
        true
    }
}

type RockLine = Vec<Point>;
type Sand = HashSet<Point>;

fn parse_line(input: String) -> RockLine {
    input.split(" -> ").into_iter().map(Point::from).collect()
}

fn lowerst_rock(rock_lines: &[RockLine]) -> usize {
    rock_lines
        .iter()
        .flatten()
        .max_by_key(|rock| rock.y)
        .unwrap()
        .y
}

fn extrapolate_rockline(mut line: RockLine) -> RockLine {
    let mut newline = RockLine::new();
    for [fst, scd] in line.array_windows() {
        let x_delta = fst.x.abs_diff(scd.x);
        let y_delta = fst.y.abs_diff(scd.y);
        assert!(x_delta == 0 || y_delta == 0);
        let x_min = fst.x.min(scd.x);
        for delta in 1..x_delta {
            newline.push(Point {
                x: x_min + delta,
                y: fst.y,
            });
        }
        let y_min = fst.y.min(scd.y);
        for delta in 1..y_delta {
            newline.push(Point {
                x: fst.x,
                y: y_min + delta,
            });
        }
    }
    newline.append(&mut line);
    newline
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_input_solve() {
        let res = solve("../assets/day14-test.txt");
        assert_eq!(res, 93);
    }

    #[test]
    fn test_solve() {
        let res = solve("../assets/day14.txt");
        assert_eq!(res, 27601);
    }
}
