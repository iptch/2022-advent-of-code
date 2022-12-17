use std::collections::{BinaryHeap, HashMap, HashSet};

const START: u8 = 'E' as u8;
const END: u8 = 'S' as u8;
const END_BIS: u8 = 'a' as u8;

fn main() {
    let map = parse_map(common::lines("day12-2/assets/input.txt"));
    let start = find_start(&map).copied().unwrap();
    let ends = find_ends(&map);
    let distances = dijkstra(&map, start);
    let min_dist = distances
        .iter()
        .filter_map(|(node, dist)| {
            if ends.contains(node) {
                Some(dist)
            } else {
                None
            }
        })
        .min()
        .unwrap();
    println!("The shortest distance is {min_dist}");
}

fn dijkstra(map: &Map, start: Node) -> HashMap<Node, usize> {
    let mut distances = HashMap::new();
    let mut visited = HashSet::new();
    let mut to_visit = BinaryHeap::new();
    distances.insert(start, 0);
    to_visit.push(Visit {
        node: start,
        distance: 0,
    });

    while let Some(Visit { node, distance }) = to_visit.pop() {
        if !visited.insert(node) {
            continue;
        }

        for neighbour in node.reachable(map) {
            let new_distance = distance + 1;
            let is_shorter = distances
                .get(neighbour)
                .map_or(true, |&current| new_distance < current);

            if is_shorter {
                distances.insert(*neighbour, new_distance);
                to_visit.push(Visit {
                    node: *neighbour,
                    distance: new_distance,
                });
            }
        }
    }

    distances
}

#[derive(Copy, Clone, PartialEq, Eq, Hash, Debug)]
struct Node {
    x: usize,
    y: usize,
    level: u8,
}

impl Node {
    fn from(x: usize, y: usize, level: u8) -> Node {
        Node { x, y, level }
    }

    fn is_end(&self) -> bool {
        self.level == END || self.level == END_BIS
    }

    fn is_start(&self) -> bool {
        self.level == START
    }

    fn level(&self) -> u8 {
        if self.is_end() {
            'a' as u8
        } else if self.is_start() {
            'z' as u8
        } else {
            self.level
        }
    }

    fn reachable<'a>(&self, map: &'a Map) -> Vec<&'a Node> {
        let res = self.surrounding(map);
        res.into_iter()
            .filter(|node| node.level() > self.level() - 2)
            .collect()
    }

    fn surrounding<'a>(&self, map: &'a Map) -> Vec<&'a Node> {
        let x_max = map.len() - 1;
        let y_max = map[0].len() - 1;
        let mut res = Vec::new();
        if self.x > 0 {
            res.push(&map[self.x - 1][self.y]);
        }
        if self.x < x_max {
            res.push(&map[self.x + 1][self.y]);
        }
        if self.y > 0 {
            res.push(&map[self.x][self.y - 1]);
        }
        if self.y < y_max {
            res.push(&map[self.x][self.y + 1]);
        }
        res
    }
}

#[derive(Eq, Debug)]
struct Visit {
    node: Node,
    distance: usize,
}

impl Ord for Visit {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        other.distance.cmp(&self.distance)
    }
}
impl PartialOrd for Visit {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

impl PartialEq for Visit {
    fn eq(&self, other: &Self) -> bool {
        self.distance.eq(&other.distance)
    }
}

type Map = Vec<Vec<Node>>;

fn parse_map<T>(input: T) -> Map
where
    T: Iterator<Item = String>,
{
    input
        .enumerate()
        .map(|(x, line)| {
            line.chars()
                .enumerate()
                .map(|(y, ch)| Node::from(x, y, ch as u8))
                .collect()
        })
        .collect()
}

fn find_start(map: &Map) -> Option<&Node> {
    map.iter().flatten().find(|node| node.is_start())
}

fn find_ends(map: &Map) -> HashSet<Node> {
    map.iter()
        .flatten()
        .filter(|node| node.is_end())
        .map(Clone::clone)
        .collect()
}
