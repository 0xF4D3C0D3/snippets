package main

import (
	"fmt"
	"math"
)

// PrimeGenerator returns generator that yields prime number one by one.
func PrimeGenerator() func() int {

	primeNumbers := []int{2}
	lastIndex := 0

	return func() int {
		for cur := primeNumbers[lastIndex] + 1; ; cur++ {
			isPrime := true
			sqrtCur := int(math.Sqrt(float64(cur)))
			for _, primeNumber := range primeNumbers {
				if cur%primeNumber == 0 {
					isPrime = false
					break
				}
				if primeNumber > sqrtCur {
					break
				}
			}
			if isPrime {
				primeNumbers = append(primeNumbers, cur)
				lastIndex++
				return primeNumbers[lastIndex-1]
			}
		}
	}
}

func main() {
	gen := PrimeGenerator()

	for i := 0; i < 500000-1; i++ {
		gen()
	}

	fmt.Println(gen()) // 7,368,787.
	fmt.Println(gen())
	fmt.Println(gen())
	fmt.Println(gen())
	fmt.Println(gen())
}
