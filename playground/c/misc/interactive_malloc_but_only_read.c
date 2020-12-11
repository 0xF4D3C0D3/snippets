#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int size;
	int sum = 0;
	int chksum = 0;
	char *p;

	do {
		printf("size(MB): ");
		scanf("%d", &size);
		p = malloc(size * 1024 * 1024);
		for (int i = 0; i < size*1024*1024; i++)
	       		chksum = (chksum + p[i]) % 64;
		sum += size;
		printf("allocated heap(MB): %d\n", sum);
	} while (size);

	return EXIT_SUCCESS;
}
