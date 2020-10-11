#ifndef PRINT_H
#define PRINT_H

#include <stdio.h>

void print_ints(int *arr, int n)
{
	for (int i = 0; i < n; i++) {
		printf("%d ", arr[i]);
	}
	printf("\n");
}

#endif /* PRINT_H */
