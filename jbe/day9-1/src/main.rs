use std::collections::HashSet;

const DIST_LIMIT: isize = 2;

fn main() {
    let moves = common::lines("day9-1/assets/input.txt").map(CompoundMove::from);
    let mut head = Position::origin();
    let mut tail = Position::origin();
    let mut positions = HashSet::new();
    for compound_move in moves {
        let set = compound_move.apply(&mut head, &mut tail);
        positions = positions.union(&set).map(Clone::clone).collect();
    }
    println!("The number of unique positions are: {}", positions.len());
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
                _   => panic!("impossible move"),
            }
        }
    }

    fn apply(&self, head: &mut Position, tail: &mut Position) -> HashSet<Position> {
        let mut res = HashSet::new();
        for _ in 0..self.count {
            head.move_(&self.move_);
            tail.follow(head);
            res.insert(tail.clone());
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

#[derive(Hash,Clone,PartialEq,Eq)]
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

    fn squared_distance(&self, other: &Position) -> isize {
        let x_delta = (other.x - self.x).abs();
        let y_delta = (other.y - self.y).abs();
        x_delta.pow(2) + y_delta.pow(2)
    }

    fn follow(&mut self, head: &Position) {
        if self.squared_distance(head) < DIST_LIMIT + 1 {
            return
        }
        let x_diff = head.x - self.x;
        let y_diff = head.y - self.y;

        if x_diff > 1 {
            self.set(head.x - 1, head.y);
        }
        else if x_diff < -1 {
            self.set(head.x + 1, head.y);
        }
        else if y_diff > 1 {
            self.set(head.x , head.y - 1);
        }
        else if y_diff < -1 {
            self.set(head.x , head.y + 1);
        }
    }
}
