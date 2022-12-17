use std::path::Path;

fn main() {
    let res = solve("assets/day1.txt");
    println!("Highest count is: {res}");
}

pub fn solve<P>(path: P) -> u32
where
    P: AsRef<Path>,
{
    let mut curr_sum = 0;
    let mut max = 0;
    for line in common::lines(path) {
        if line.is_empty() {
            if curr_sum > max {
                max = curr_sum;
            }
            curr_sum = 0;
            continue;
        }
        let calories = line.parse::<u32>().unwrap();
        curr_sum += calories;
    }
    if curr_sum > max {
        max = curr_sum;
    }
    max
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_input_solve() {
        let res = solve("../assets/day1-test.txt");
        assert_eq!(res, 24000);
    }

    #[test]
    fn test_solve() {
        let res = solve("../assets/day1.txt");
        assert_eq!(res, 71502);
    }
}
