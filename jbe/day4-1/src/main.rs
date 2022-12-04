fn main() {
    let count = common::lines("day4-1/assets/input.txt")
        .map(|line| parse_line(&line))
        .filter(|(range1, range2)| range1.contains(range2) || range2.contains(range1))
        .count();
    println!("The number of contained ranges is: {count}")
}


struct Range {
    min: usize,
    max: usize
}

impl Range {
    fn contains(&self, other: &Range) -> bool {
        self.min <= other.min && self.max >= other.max
    }
}


fn parse_line(line: &str) -> (Range, Range) {
    let (range1, range2) = line.split_once(',').unwrap();
    let (min1, max1) = range1.split_once('-').unwrap();
    let (min2, max2) = range2.split_once('-').unwrap();
    (
        Range{
            min: min1.parse::<usize>().unwrap(),
            max: max1.parse::<usize>().unwrap(),
        },
        Range{
            min: min2.parse::<usize>().unwrap(),
            max: max2.parse::<usize>().unwrap(),
        }
    )
}
