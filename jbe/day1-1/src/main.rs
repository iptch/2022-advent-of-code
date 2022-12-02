use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let filename = "assets/input.txt";
    let file = File::open(filename).unwrap();
    let reader = BufReader::new(file);

    let mut curr_sum = 0;
    let mut max = 0;
    for line in reader.lines() {
        let line = line.unwrap();
        if line.is_empty() {
            if curr_sum > max {
                max = curr_sum;
            }
            curr_sum = 0;
            continue
        }
        let calories = line.parse::<u32>().unwrap();
        curr_sum += calories;
    }
    if curr_sum > max {
        max = curr_sum;
    }
    println!("Highest count is: {}", max);
}
