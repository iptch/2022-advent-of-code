package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	fmt.Println(os.Getwd())
	input, err := os.Open("input.txt")
	if err != nil {
		log.Fatalf("failed to open: %v", err)
	}
	defer input.Close()

	scanner := bufio.NewScanner(input)
	currentCalories := 0
	maxHeap := newMaxHeap()
	for scanner.Scan() {
		if scanner.Text() == "" {
			maxHeap.insert(currentCalories)
			currentCalories = 0
		} else {
			snack, _ := strconv.Atoi(scanner.Text())
			currentCalories += snack
		}
	}
	fmt.Println(maxHeap.remove() + maxHeap.remove() + maxHeap.remove())
}

// source: https://golangbyexample.com/maxheap-in-golang/
type maxheap struct {
	heapArray []int
	size      int
}

func newMaxHeap() *maxheap {
	maxheap := &maxheap{
		heapArray: []int{},
		size:      0,
	}
	return maxheap
}

func (m *maxheap) leaf(index int) bool {
	if index >= (m.size/2) && index <= m.size {
		return true
	}
	return false
}

func (m *maxheap) parent(index int) int {
	return (index - 1) / 2
}

func (m *maxheap) leftchild(index int) int {
	return 2*index + 1
}

func (m *maxheap) rightchild(index int) int {
	return 2*index + 2
}

func (m *maxheap) insert(item int) error {
	m.heapArray = append(m.heapArray, item)
	m.size++
	m.upHeapify(m.size - 1)
	return nil
}

func (m *maxheap) swap(first, second int) {
	temp := m.heapArray[first]
	m.heapArray[first] = m.heapArray[second]
	m.heapArray[second] = temp
}

func (m *maxheap) upHeapify(index int) {
	for m.heapArray[index] > m.heapArray[m.parent(index)] {
		m.swap(index, m.parent(index))
		index = m.parent(index)
	}
}

func (m *maxheap) downHeapify(current int) {
	if m.leaf(current) {
		return
	}
	largest := current
	leftChildIndex := m.leftchild(current)
	rightRightIndex := m.rightchild(current)
	//If current is smallest then return
	if leftChildIndex < m.size && m.heapArray[leftChildIndex] > m.heapArray[largest] {
		largest = leftChildIndex
	}
	if rightRightIndex < m.size && m.heapArray[rightRightIndex] > m.heapArray[largest] {
		largest = rightRightIndex
	}
	if largest != current {
		m.swap(current, largest)
		m.downHeapify(largest)
	}
}

func (m *maxheap) remove() int {
	top := m.heapArray[0]
	m.heapArray[0] = m.heapArray[m.size-1]
	m.heapArray = m.heapArray[:(m.size)-1]
	m.size--
	m.downHeapify(0)
	return top
}
