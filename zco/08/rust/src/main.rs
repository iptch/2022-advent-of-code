use std::io;

trait Matrix<T> {
    fn height(&self) -> usize;
    fn width(&self) -> usize;

    fn value_at(&self, i: usize, j: usize) -> T;
}

struct IndicesMatrix {
    width: usize,
    height: usize,
}

impl Matrix<(usize, usize)> for IndicesMatrix {
    fn height(&self) -> usize {
        self.height
    }

    fn width(&self) -> usize {
        self.width
    }

    fn value_at(&self, i: usize, j: usize) -> (usize, usize) {
        (i, j)
    }
}

struct NRotatedMatrix<T> {
    base_matrix: T,
    n: u32,
}

impl<T, E> Matrix<E> for NRotatedMatrix<T>
where
    T: Matrix<E>,
{
    fn height(&self) -> usize {
        if self.n % 2 == 0 {
            self.base_matrix.height()
        } else {
            self.base_matrix.width()
        }
    }

    fn width(&self) -> usize {
        if self.n % 2 == 0 {
            self.base_matrix.width()
        } else {
            self.base_matrix.height()
        }
    }

    fn value_at(&self, i: usize, j: usize) -> E {
        // delegate to base matrix
        let (mut i, mut j) = (i, j);
        for _ in 0..self.n {
            (i, j) = (self.width() - 1 - j, i)
        }
        self.base_matrix.value_at(i, j)
    }
}

fn mark_visible_trees<T>(
    indices_matrix: &T,
    lines: &Vec<Vec<char>>,
    visible_trees: &mut Vec<Vec<bool>>,
) where
    T: Matrix<(usize, usize)>,
{
    for i in 0..indices_matrix.height() {
        let mut max: i32 = -1;
        for j in 0..indices_matrix.width() {
            let (i, j) = indices_matrix.value_at(i, j);
            let tree_height = lines[i][j].to_digit(10).unwrap() as i32;
            if tree_height > max {
                max = tree_height;
                visible_trees[i][j] = true;
            }
        }
    }
}

fn mark_scenic_ranges<T>(
    indices_matrix: &T,
    lines: &Vec<Vec<char>>,
    scenic_ranges: &mut Vec<Vec<u32>>,
) where
    T: Matrix<(usize, usize)>,
{
    for i in 0..indices_matrix.height() {
        let mut seen: Vec<u32> = vec![];
        for j in 0..indices_matrix.width() {
            let (i, j) = indices_matrix.value_at(i, j);
            let tree_height = lines[i][j].to_digit(10).unwrap() as u32;
            let blocking_tree_position = seen.iter().rposition(|&h| h >= tree_height).unwrap_or(0);
            scenic_ranges[i][j] *= (seen.len() - blocking_tree_position) as u32;
            seen.push(tree_height);
        }
    }
}

fn solve1(lines: &Vec<Vec<char>>) -> u32 {
    let (width, height) = (lines.len(), lines[0].len());
    let mut indices_matrix = NRotatedMatrix {
        base_matrix: IndicesMatrix { width, height },
        n: 0,
    };
    let mut visible_trees = vec![vec![false; width]; height];
    for _ in 0..4 {
        mark_visible_trees(&indices_matrix, &lines, &mut visible_trees);
        indices_matrix.n += 1;
    }
    visible_trees.iter().flatten().map(|&b| b as u32).sum()
}

fn solve2(lines: &Vec<Vec<char>>) -> u32 {
    let (width, height) = (lines.len(), lines[0].len());
    let mut indices_matrix = NRotatedMatrix {
        base_matrix: IndicesMatrix { width, height },
        n: 0,
    };
    let mut scenic_ranges = vec![vec![1; width]; height];
    for _ in 0..4 {
        mark_scenic_ranges(&indices_matrix, &lines, &mut scenic_ranges);
        indices_matrix.n += 1;
    }
    *scenic_ranges.iter().flatten().max().unwrap()
}

fn main() {
    let lines: Vec<Vec<char>> = io::stdin()
        .lines()
        .map(|l| l.unwrap().chars().collect())
        .collect();
    println!("ans1 {}", solve1(&lines));
    println!("ans2 {}", solve2(&lines));
}
