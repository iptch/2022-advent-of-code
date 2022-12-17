use std::path::Path;

fn main() {
    let res = solve("assets/day8.txt");
    println!("The best scenic score is {res}");
}

pub fn solve<P>(path: P) -> usize
where
    P: AsRef<Path>,
{
    let tree_map = generate_tree_matrix(common::lines(path));
    let height = tree_map.len();
    let width = tree_map[0].len();
    let mut max = 0;
    for h in 1..height - 1 {
        for w in 1..width - 1 {
            let score = scenic_score(&tree_map, (h, w));
            if score > max {
                max = score;
            }
        }
    }
    max
}

fn scenic_score(map: &Vec<Vec<u8>>, (h, w): (usize, usize)) -> usize {
    let height = map.len();
    let width = map[0].len();
    let tree = map[h][w];
    let left = (1..=w).find(|idx| map[h][w - idx] >= tree).unwrap_or(w);
    let right = (1..width - w)
        .find(|idx| map[h][w + idx] >= tree)
        .unwrap_or(width - w - 1);
    let top = (1..=h).find(|idx| map[h - idx][w] >= tree).unwrap_or(h);
    let bottom = (1..height - h)
        .find(|idx| map[h + idx][w] >= tree)
        .unwrap_or(height - h - 1);
    left * right * top * bottom
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
        assert_eq!(res, 8);
    }

    #[test]
    fn test_solve() {
        let res = solve("../assets/day8.txt");
        assert_eq!(res, 517440);
    }
}
