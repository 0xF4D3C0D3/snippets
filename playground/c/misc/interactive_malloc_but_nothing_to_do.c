#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int size;
	int sum = 0;
	char *p;

	do {
		printf("size(MB): ");
		scanf("%d", &size);
		malloc(size * 1024 * 1024);
		sum += size;
		printf("allocated heap(MB): %d\n", sum);
	} while (size);

	return EXIT_SUCCESS;
}
