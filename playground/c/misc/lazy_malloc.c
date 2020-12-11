#include <stdio.h>
#include <stdlib.h>

void plus_one(int **i)
{
	if (*i == NULL) {
		*i = malloc(sizeof(int));
		**i = 0;
	}
	**i += 1;
}

int main()
{
	int *i = NULL;

	plus_one(&i);
	plus_one(&i);
	plus_one(&i);
	
	printf("i: %d\n", *i);

	return EXIT_SUCCESS;
}
