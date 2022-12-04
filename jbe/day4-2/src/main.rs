fn main() {
    let count = common::lines("day4-2/assets/input.txt")
        .map(|line| parse_line(&line))
        .filter(|(range1, range2)| range1.overlaps(range2))
        .count();
    println!("The number of contained ranges is: {count}")
}

struct Range {
    min: usize,
    max: usize,
}

impl Range {
    fn contains(&self, other: &Range) -> bool {
        self.min <= other.min && self.max >= other.max
    }

    fn overlaps(&self, other: &Range) -> bool {
        self.contains(other)
            || self.min >= other.min && self.min <= other.max
            || self.max >= other.min && self.max <= other.max
    }
}

fn parse_line(line: &str) -> (Range, Range) {
    let (range1, range2) = line.split_once(',').unwrap();
    let (min1, max1) = range1.split_once('-').unwrap();
    let (min2, max2) = range2.split_once('-').unwrap();
    (
        Range {
            min: min1.parse::<usize>().unwrap(),
            max: max1.parse::<usize>().unwrap(),
        },
        Range {
            min: min2.parse::<usize>().unwrap(),
            max: max2.parse::<usize>().unwrap(),
        },
    )
}
