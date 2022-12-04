fn main() {
    let mut curr_sum = 0;
    let mut max = 0;
    for line in common::lines("day1-1/assets/input.txt") {
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
    println!("Highest count is: {max}");
}
