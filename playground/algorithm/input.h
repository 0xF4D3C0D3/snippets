#define  _POSIX_C_SOURCE 200809L
#ifndef INPUT_H
#define INPUT_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int input_ints(int **arr)
{
	char *line = NULL;
	size_t len = 0;
	getline(&line, &len, stdin);

	size_t cap = 4;
	*arr = (int*)malloc(sizeof(int) * cap);
	char *tok = strtok(line, " ");
	size_t i = 0;
	while (tok != NULL && *tok != '\n') {
		if (i >= cap) {
			cap *= 2;
			*arr = (int*)realloc(*arr, sizeof(int) * cap);
		}
		(*arr)[i++] = atoi(tok);
		tok = strtok(NULL, " ");
	}

	free(line);

	return i;
}

#endif /* INPUT_H */
