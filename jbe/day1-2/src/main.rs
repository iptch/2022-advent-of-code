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
    let mut maxes = (0, 0, 0);
    for line in common::lines(path) {
        if line.is_empty() {
            maxes = get_maxes(curr_sum, maxes);
            curr_sum = 0;
            continue;
        }
        let calories = line.parse::<u32>().unwrap();
        curr_sum += calories;
    }
    let (fst, scd, thd) = get_maxes(curr_sum, maxes);
    fst + scd + thd
}

fn get_maxes(val: u32, maxes: (u32, u32, u32)) -> (u32, u32, u32) {
    let (fst, scd, thd) = maxes;
    match val {
        x if x > fst => (x, fst, scd),
        x if x > scd => (fst, x, scd),
        x if x > thd => (fst, scd, x),
        _ => (fst, scd, thd),
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_input_solve() {
        let res = solve("../assets/day1-test.txt");
        assert_eq!(res, 45000);
    }

    #[test]
    fn test_solve() {
        let res = solve("../assets/day1.txt");
        assert_eq!(res, 208191);
    }
}
