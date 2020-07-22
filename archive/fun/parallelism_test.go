package main

import (
	"fmt"
	"sync"
	"time"
)

func benchmark() int {
	x := 0
	timer := time.After(1 * time.Second)
	for {
		select {
		case <-timer:
			return x
		default:
			x++
		}
	}
}

func main() {
	var wg sync.WaitGroup

	for i := 1; i <= 4096; i *= 2 {
		sum := 0
		for j := 0; j < i; j++ {
			wg.Add(1)
			go func() {
				sum += benchmark()
				defer wg.Done()
			}()
		}

		wg.Wait()
		fmt.Printf("%4v -> %16v\n", i, sum)
	}

	/*
		   1 ->        153388453
		   2 ->        308295256
		   4 ->        608957699
		   8 ->        842699735
		  16 ->       1072344084
		  32 ->       1078645355
		  64 ->       1212425247
		 128 ->       1347460944
		 256 ->       4820308136
		 512 ->       4525312863
		1024 ->       3684765587
		2048 ->       4877638720
	*/
}
