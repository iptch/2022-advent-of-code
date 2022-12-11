package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
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
		set := make(map[byte]bool)
		items := scanner.Text()
		for i := 0; i < len(items)/2; i++ {
			set[items[i]] = true
		}
		for i := len(items) / 2; i < len(items); i++ {
			if _, ok := set[items[i]]; ok {
				score += calculateValue(items[i])
				break
			}
		}
	}
	fmt.Println(score)
}

func calculateValue(item byte) int {
	if int(item) < 91 {
		return int(item) - 38 //A-Z
	} else {
		return int(item) - 96 //a-z
	}
}
