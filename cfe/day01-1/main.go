package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	input, err := os.Open("input.txt")
	if err != nil {
		log.Fatalf("failed to open: %v", err)
	}
	defer input.Close()

	scanner := bufio.NewScanner(input)
	maxCalories := 0
	currentCalories := 0
	for scanner.Scan() {
		if scanner.Text() == "" {
			if currentCalories > maxCalories {
				maxCalories = currentCalories
			}
			currentCalories = 0
		} else {
			snack, _ := strconv.Atoi(scanner.Text())
			currentCalories += snack
		}
	}
	fmt.Println(maxCalories)
}
