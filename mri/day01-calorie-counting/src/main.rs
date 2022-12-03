use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    
    let mut current_elf_calories = 0;
    let mut max_elf_calories = 0;

    for line in read_lines("assets/input.txt") {
        if line.is_empty() {
            if current_elf_calories > max_elf_calories {
                max_elf_calories = current_elf_calories;
            }
            current_elf_calories = 0;
        } else {
            current_elf_calories += line.parse::<u32>().unwrap();
        }
    }

    if current_elf_calories > max_elf_calories {
        max_elf_calories = current_elf_calories;
    }

    println!("Maximum calories carried by an elf: {}", max_elf_calories);

    // The output is wrapped in a Result to allow matching on errors
    // Returns an Iterator to the Reader of the lines of the file.
    fn read_lines<P>(filename: P) -> impl Iterator<Item=String> where P: AsRef<Path>, {
        let file = File::open(filename).unwrap();
        let reader = io::BufReader::new(file);
        reader.lines().map(|x| x.unwrap())
    }

}
