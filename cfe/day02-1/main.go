package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	input, err := os.Open("input.txt")
	if err != nil {
		log.Fatalf("failed to open: %v", err)
	}
	defer input.Close()

	scanner := bufio.NewScanner(input)
	score := 0
	for scanner.Scan() {
		gameInput := strings.Split(scanner.Text(), " ")
		game := formatInput(gameInput)
		score += game[1]
		if game[0] == game[1] {
			score += 3
		}
		if game[1] == 1 {
			game[1] = 4
		}
		if game[0]+1 == game[1] {
			score += 6
		}
	}
	fmt.Println(score)
}

func formatInput(input []string) []int {
	output := make([]int, 2)
	if input[0] == "A" {
		output[0] = 1
	}
	if input[0] == "B" {
		output[0] = 2
	}
	if input[0] == "C" {
		output[0] = 3
	}
	if input[1] == "X" {
		output[1] = 1
	}
	if input[1] == "Y" {
		output[1] = 2
	}
	if input[1] == "Z" {
		output[1] = 3
	}
	return output
}
