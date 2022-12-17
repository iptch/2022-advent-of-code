use std::path::Path;

fn main() {
    let res = solve("assets/day8.txt");
    println!("The number of visible trees is {res}");
}

pub fn solve<P>(path: P) -> usize
where
    P: AsRef<Path>,
{
    let tree_map = generate_tree_matrix(common::lines(path));
    let height = tree_map.len();
    let width = tree_map[0].len();
    let mut hidden = 0;
    for h in 1..height - 1 {
        for w in 1..width - 1 {
            if is_tree_hidden(&tree_map, (h, w)) {
                hidden += 1;
            }
        }
    }
    width * height - hidden
}

fn is_tree_hidden(map: &Vec<Vec<u8>>, (h, w): (usize, usize)) -> bool {
    let height = map.len();
    let width = map[0].len();
    let tree = map[h][w];
    (0..w).any(|idx| map[h][idx] >= tree)
        && (w + 1..width).any(|idx| map[h][idx] >= tree)
        && (0..h).any(|idx| map[idx][w] >= tree)
        && (h + 1..height).any(|idx| map[idx][w] >= tree)
}

fn generate_tree_matrix<P>(lines: P) -> Vec<Vec<u8>>
where
    P: Iterator<Item = String>,
{
    let mut res = Vec::new();
    for line in lines {
        let heights = line
            .chars()
            .map(|x| x.to_digit(10).unwrap() as u8)
            .collect();
        res.push(heights);
    }
    res
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_input_solve() {
        let res = solve("../assets/day8-test.txt");
        assert_eq!(res, 21);
    }

    #[test]
    fn test_solve() {
        let res = solve("../assets/day8.txt");
        assert_eq!(res, 1870);
    }
}
