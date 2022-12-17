use lazy_static::lazy_static;
use regex::Regex;
use std::path::Path;

lazy_static! {
    static ref FILE: Regex = Regex::new(r"(?P<size>\d+) (?P<name>\S+)").unwrap();
    static ref DIR: Regex = Regex::new(r"dir (?P<name>\S+)").unwrap();
    static ref CD: Regex = Regex::new(r"\$ cd (?P<name>\S+)").unwrap();
}

const TOTAL: usize = 70000000;
const UPDATE_SIZE: usize = 30000000;

fn main() {
    let res = solve("assets/day7.txt");
    println!("You should delete the node of size {res}");
}

pub fn solve<P>(path: P) -> usize
where
    P: AsRef<Path>,
{
    let mut state = State {
        cwd: Vec::new(),
        fs: Node::Directory(Vec::new(), Vec::new()),
    };

    common::lines(path).for_each(|statement| state.parse(&statement));
    let free_space = TOTAL - state.fs.size();
    let space_needed = UPDATE_SIZE - free_space;

    let nodes = state.fs.flatten();
    let mut dirs: Vec<Node> = nodes.into_iter().filter(|node| node.is_dir()).collect();
    dirs.sort_by_key(|node| node.size());
    dirs.iter()
        .find(|node| node.size() > space_needed)
        .unwrap()
        .size()
}

#[derive(Clone)]
enum Node {
    File(Vec<String>, usize),
    Directory(Vec<String>, Vec<Node>),
}

impl PartialEq<Node> for Node {
    fn eq(&self, other: &Node) -> bool {
        self.name() == other.name()
    }
}

impl Node {
    fn name(&self) -> String {
        match self {
            Node::File(path, _) => path.join("/"),
            Node::Directory(path, _) => path.join("/"),
        }
    }

    fn size(&self) -> usize {
        match self {
            Node::File(_, size) => *size,
            Node::Directory(_, children) => children.iter().map(|node| node.size()).sum(),
        }
    }

    fn is_dir(&self) -> bool {
        match self {
            Node::File(_, _) => false,
            Node::Directory(_, _) => true,
        }
    }

    fn add_child(&mut self, child: Node) {
        match self {
            Node::File(_, _) => panic!("Cannot add child to file node"),
            Node::Directory(_, children) => {
                if !children.contains(&child) {
                    children.push(child);
                }
            }
        }
    }

    fn find(&mut self, path: &[String]) -> Option<&mut Node> {
        let name = path.join("/");
        if self.name() == name {
            return Some(self);
        } else if !name.starts_with(&self.name()) {
            return None;
        }
        match self {
            Node::Directory(_, children) => children.iter_mut().find_map(|node| node.find(path)),
            _ => None,
        }
    }

    fn flatten(self) -> Vec<Node> {
        let mut res = Vec::new();
        if let Node::Directory(_, children) = self.clone() {
            for child in children {
                res.append(&mut child.flatten());
            }
        }
        res.push(self);
        res
    }
}

struct State {
    cwd: Vec<String>,
    fs: Node,
}

impl State {
    fn parse(&mut self, statement: &str) {
        if FILE.is_match(statement) {
            self.parse_file(statement);
        } else if CD.is_match(statement) {
            self.parse_cd(statement);
        } else if DIR.is_match(statement) {
            self.parse_dir(statement);
        }
    }

    fn parse_file(&mut self, statement: &str) {
        let caps = FILE.captures(statement).unwrap();
        let size = caps.name("size").unwrap().as_str().parse().unwrap();
        let name = caps.name("name").unwrap().as_str().into();
        let mut path = self.cwd.clone();
        let curr_node = self.fs.find(&path).unwrap();
        path.push(name);
        curr_node.add_child(Node::File(path, size));
    }

    fn parse_cd(&mut self, statement: &str) {
        let caps = CD.captures(statement).unwrap();
        let name = caps.name("name").unwrap().as_str().to_string();
        match name.as_str() {
            "/" => self.cwd = Vec::new(),
            ".." => {
                self.cwd.pop();
            }
            _ => self.cwd.push(name),
        }
    }

    fn parse_dir(&mut self, statement: &str) {
        let caps = DIR.captures(statement).unwrap();
        let name = caps.name("name").unwrap().as_str().into();
        let mut path = self.cwd.clone();
        let curr_node = self.fs.find(&path).unwrap();
        path.push(name);
        curr_node.add_child(Node::Directory(path, Vec::new()));
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_input_solve() {
        let res = solve("../assets/day7-test.txt");
        assert_eq!(res, 24933642);
    }

    #[test]
    fn test_solve() {
        let res = solve("../assets/day7.txt");
        assert_eq!(res, 942298);
    }
}
