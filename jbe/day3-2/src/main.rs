#![feature(iter_array_chunks)]

const OFFSET_LOWER: usize = 96;
const OFFSET_UPPER: usize = 64 - 26;

fn main() {
    let sum: usize = common::lines("day3-2/assets/input.txt").array_chunks()
        .map(|[bp1, bp2, bp3]| find_duplicate(&bp1, &bp2, &bp3))
        .filter(|chr| chr.is_some())
        .map(|chr| score(chr.unwrap()))
        .sum();
    println!("The sum of badges is: {sum}");
}

fn score(ch: char) -> usize {
    if ch.is_lowercase() {
        ch as usize - OFFSET_LOWER
    } else {
        ch as usize - OFFSET_UPPER
    }
}

// This should be much faster than simple lookup which is worst case O(n^2) worst case with n being
// the length of the compartment. This uses several partern-defeating quicksorts which are only O(n
// * log(n)) worst case, followed by a simple traversal in O(n). This means this should be worst
// case O(n * log(n) + n).
fn find_duplicate(backpack1: &str, backpack2: &str, backpack3: &str) -> Option<char> {
    let mut state = vec![
        (get_sorted(backpack1), 0usize, backpack1.len()),
        (get_sorted(backpack2), 0usize, backpack2.len()),
        (get_sorted(backpack3), 0usize, backpack3.len()),
    ];

    // while the end of the backpack is not reached for all backpacks
    while state[0].1 < state[0].2 || state[1].1 < state[1].2 || state[2].1 < state[2].2 {
        sort_state(&mut state);

        let ch0 = get_char(&state, 0);
        let ch1 = get_char(&state, 1);
        let ch2 = get_char(&state, 2);
        if ch0 == ch1 && ch1 == ch2 {
            return Some(ch0);
        }

        // first character is guaranteed to be the smallest, if this can be increased, to so. If it
        // cannot, then no solution can be reached.
        if state[0].1 < state[0].2 - 1 {
            state[0].1 += 1;
        } else {
            break;
        }
    }

    None
}

// sorts the state based on the smallest current character being observed
fn sort_state(state: &mut [(Vec<char>, usize, usize)]) {
    state.sort_unstable_by(|(content1, idx1, _), (content2, idx2, _)| {
        content1[*idx1].cmp(&content2[*idx2])
    });
}

// get currently observed character in state for index idx
fn get_char(state: &[(Vec<char>, usize, usize)], idx: usize) -> char {
    state[idx].0[state[idx].1]
}

// sort a string reference
fn get_sorted(val: &str) -> Vec<char> {
    let mut sorted = val.chars().collect::<Vec<char>>();
    sorted.sort_unstable();
    sorted
}
