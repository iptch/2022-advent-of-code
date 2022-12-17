use std::collections::HashSet;
use std::path::Path;

const LEN: usize = 10;

fn main() {
    let res = solve("assets/day9.txt");
    println!("The number of unique positions are: {res}");
}

pub fn solve<P>(path: P) -> usize
where
    P: AsRef<Path>,
{
    let moves = common::lines(path).map(CompoundMove::from);
    let mut rope = vec![Position::origin(); LEN];
    let mut positions = HashSet::new();
    for compound_move in moves {
        let set = compound_move.apply(&mut rope);
        positions = positions.union(&set).map(Clone::clone).collect();
    }
    positions.len()
}

struct CompoundMove {
    move_: Move,
    count: u8,
}

impl CompoundMove {
    fn from(line: String) -> CompoundMove {
        let (dir, count) = line.split_once(' ').unwrap();
        let count = count.parse().unwrap();
        CompoundMove {
            count,
            move_: match dir {
                "R" => Move::Right,
                "L" => Move::Left,
                "U" => Move::Up,
                "D" => Move::Down,
                _ => panic!("impossible move"),
            },
        }
    }

    fn apply(&self, rope: &mut Vec<Position>) -> HashSet<Position> {
        let mut res = HashSet::new();
        let len = rope.len();
        for _ in 0..self.count {
            rope[0].move_(&self.move_);
            for idx in 0..len - 1 {
                let head = rope[idx].clone();
                rope[idx + 1].follow(&head);
            }
            res.insert(rope[len - 1].clone());
        }
        res
    }
}

enum Move {
    Up,
    Down,
    Right,
    Left,
}

#[derive(Hash, Clone, PartialEq, Eq)]
struct Position {
    x: isize,
    y: isize,
}

impl Position {
    fn origin() -> Position {
        Position { x: 0, y: 0 }
    }

    fn move_(&mut self, move_: &Move) {
        match move_ {
            Move::Up => self.y += 1,
            Move::Down => self.y -= 1,
            Move::Right => self.x += 1,
            Move::Left => self.x -= 1,
        };
    }

    fn set(&mut self, x: isize, y: isize) {
        self.x = x;
        self.y = y;
    }

    fn follow(&mut self, head: &Position) {
        let x_diff = head.x - self.x;
        let y_diff = head.y - self.y;

        match (x_diff, y_diff) {
            (2, 2) => self.set(head.x - 1, head.y - 1),
            (2, -2) => self.set(head.x - 1, head.y + 1),
            (-2, -2) => self.set(head.x + 1, head.y + 1),
            (-2, 2) => self.set(head.x + 1, head.y - 1),
            (2, _) => self.set(head.x - 1, head.y),
            (-2, _) => self.set(head.x + 1, head.y),
            (_, 2) => self.set(head.x, head.y - 1),
            (_, -2) => self.set(head.x, head.y + 1),
            (_, _) => {}
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_input_solve() {
        let res = solve("../assets/day9-test.txt");
        assert_eq!(res, 1);
    }

    #[test]
    fn test_solve() {
        let res = solve("../assets/day9.txt");
        assert_eq!(res, 2482);
    }
}
