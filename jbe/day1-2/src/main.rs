fn main() {
    let mut curr_sum = 0;
    let mut maxes = (0, 0, 0);
    for line in common::lines("day1-1/assets/input.txt") {
        if line.is_empty() {
            maxes = get_maxes(curr_sum, maxes);
            curr_sum = 0;
            continue
        }
        let calories = line.parse::<u32>().unwrap();
        curr_sum += calories;
    }
    let (fst, scd, thd) = get_maxes(curr_sum, maxes);
    println!("Highest count is: {}", fst + scd + thd);
}


fn get_maxes(val: u32, maxes: (u32, u32, u32)) -> (u32, u32, u32) {
    let (fst, scd, thd) = maxes;
    match val {
        x if x > fst => (x, fst, scd),
        x if x > scd => (fst, x, scd),
        x if x > thd => (fst, scd, x),
        _ => (fst, scd, thd)
    }
}
