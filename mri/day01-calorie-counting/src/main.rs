use common::read_lines;

fn main() {
    
    let mut current_elf_calories = 0;
    let mut max_elf_calories = 0;

    let mut aggregated_calories = Vec::new();

    for line in read_lines("assets/input.txt") {
        if line.is_empty() {
            aggregated_calories.push(current_elf_calories);

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

    aggregated_calories.sort();
    aggregated_calories.reverse();
    let total_calories_top3 = aggregated_calories[0] + aggregated_calories[1] + aggregated_calories[2];

    println!("Maximum calories carried by an elf: {}", max_elf_calories);
    println!("Total amount caried by top 3 elves: {}", total_calories_top3);


}
