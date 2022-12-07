use lazy_static::lazy_static;
use regex::Regex;

lazy_static! {
    static ref FILE: Regex = Regex::new(r"(?P<size>\d+) (?P<name>\S+)").unwrap();
    static ref DIR: Regex  = Regex::new(r"dir (?P<name>\S+)").unwrap();
    static ref CD: Regex   = Regex::new(r"\$ cd (?P<name>\S+)").unwrap();
}

fn main() {
    let mut state = State {
        cwd: "/".into(),
        fs: Node::Directory("/".into(), Vec::new()),
    };

    common::lines("day7-1/assets/input.txt").for_each(|statement| state.parse(&statement));
    let nodes = state.fs.flatten();
    let sum: usize = nodes
        .iter()
        .filter(|node| node.is_dir())
        .map(|node| node.size())
        .filter(|size| *size <= 100000)
        .sum();
    println!("The sum of the total sizes of these directories is {sum}");
}

#[derive(Clone)]
enum Node {
    File(String, usize),
    Directory(String, Vec<Node>),
}

impl Node {
    fn name(&self) -> &str {
        match self {
            Node::File(name, _)      => name,
            Node::Directory(name, _) => name,
        }
    }

    fn size(&self) -> usize {
        match self {
            Node::File(_, size)          => *size,
            Node::Directory(_, children) => children.iter().map(|node| node.size()).sum(),
        }
    }

    fn is_dir(&self) -> bool {
        match self {
            Node::File(_, _)      => false,
            Node::Directory(_, _) => true,
        }
    }

    fn add_child(&mut self, child: Node) {
        match self {
            Node::File(_, _)             => panic!("Cannot add child to file node"),
            Node::Directory(_, children) => {
                children.push(child);
            }
        }
    }

    fn find(&mut self, path: &str) -> Option<&mut Node> {
        if self.name() == path {
            return Some(self);
        } else if !path.starts_with(self.name()) {
            return None;
        }
        match self {
            Node::Directory(_, children) => children.iter_mut().find_map(|node| node.find(path)),
            _                            => None,
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
    cwd: String,
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
        let curr_node = self.fs.find(&self.cwd).unwrap();
        curr_node.add_child(Node::File(name, size));
    }

    fn parse_cd(&mut self, statement: &str) {
        let caps = CD.captures(statement).unwrap();
        let mut name = caps.name("name").unwrap().as_str().to_string();
        match name.as_str() {
            "/"  => self.cwd = name,
            ".." => self.cwd = self.cwd.rsplit_once('/').unwrap().0.into(),
            _    => {
                name = format!("{}/{name}", self.cwd);
                self.cwd = name;
            }
        }
    }

    fn parse_dir(&mut self, statement: &str) {
        let caps = DIR.captures(statement).unwrap();
        let mut name = caps.name("name").unwrap().as_str().into();
        name = format!("{}/{name}", self.cwd);
        let curr_node = self.fs.find(&self.cwd).unwrap();
        curr_node.add_child(Node::Directory(name, Vec::new()));
    }
}
