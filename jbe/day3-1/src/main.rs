use std::collections::HashSet;

const OFFSET_LOWER: usize = 96;
const OFFSET_UPPER: usize = 64 - 26;

fn main() {
    let sum: usize = common::lines("day3-1/assets/input.txt")
        .map(|line| find_duplicate(&line))
        .filter(|chr| chr.is_some())
        .map(|chr| score(chr.unwrap()))
        .sum();
    println!("The sum of duplicate items in the compartments is: {sum}");
    let sum_set_based: usize = common::lines("day3-1/assets/input.txt")
        .map(|line| find_duplicate_set_based(&line))
        .filter(|chr| chr.is_some())
        .map(|chr| score(chr.unwrap()))
        .sum();
    println!("The sum of duplicate items in the compartments is (set based): {sum_set_based}");
}



fn score(ch: char) -> usize {
    if ch.is_lowercase() {
        ch as usize - OFFSET_LOWER
    } else {
        ch as usize - OFFSET_UPPER
    }
}



// This should be much faster than simple lookup which is worst case O(n^2) with n being the length
// of the compartment. It uses no HashMap in order to optimize memory usage. This uses two
// partern-defeating quicksorts which are only O(n * log(n)) worst case, followed by a simple
// traversal in O(n). This means this should be worst case O(n * log(n) + n). In terms of memory,
// the sorting is done in place, which means we only allocate a single vector per compartment.
// Since we pipe the reference to this function, this should mean that we only assign each
// character twice in the entire program, once at read time, and once in this function.
fn find_duplicate(backpack: &str) -> Option<char> {
    let backpack_len = backpack.len();
    assert!(backpack_len % 2 == 0);
    let (comptmnt1, comptmnt2) = backpack.split_at(backpack_len / 2);
    let sorted1 = get_sorted(comptmnt1);
    let sorted2 = get_sorted(comptmnt2);

    let max_idx = comptmnt1.len();
    let mut idx1 = 0;
    let mut idx2 = 0;

    while idx1 < max_idx || idx2 < max_idx {
        let chr1 = sorted1[idx1];
        let chr2 = sorted2[idx2];
        if chr1 == chr2 {
            return Some(chr1);
        }
        if chr1 < chr2 {
            idx1 += 1;
        } else {
            idx2 += 1;
        }
    }

    None
}


// This solution is O(n), but it is boring. Moreover, due to the usage of a HashMap, it is more
// memory hungry than the solution above.
fn find_duplicate_set_based(backpack: &str) -> Option<char> {
    let backpack_len = backpack.len();
    assert!(backpack_len % 2 == 0);
    let (comptmnt1, comptmnt2) = backpack.split_at(backpack_len / 2);
    let comptmnt2_set: HashSet<char> = comptmnt2.chars().collect();

    for ch in comptmnt1.chars() {
        if comptmnt2_set.contains(&ch) {
            return Some(ch)
        }
    }

    None
}


fn get_sorted(val: &str) -> Vec<char> {
    let mut sorted = val.chars().collect::<Vec<char>>();
    sorted.sort_unstable();
    sorted
}
