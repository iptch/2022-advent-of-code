use std::path::Path;

fn main() {
    let res = solve("assets/day4.txt");
    println!("The number of contained ranges is: {res}")
}

pub fn solve<P>(path: P) -> usize
where
    P: AsRef<Path>,
{
    common::lines(path)
        .map(|line| parse_line(&line))
        .filter(|(range1, range2)| range1.contains(range2) || range2.contains(range1))
        .count()
}

struct Range {
    min: usize,
    max: usize,
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

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_input_solve() {
        let res = solve("../assets/day4-test.txt");
        assert_eq!(res, 2);
    }

    #[test]
    fn test_solve() {
        let res = solve("../assets/day4.txt");
        assert_eq!(res, 464);
    }
}
