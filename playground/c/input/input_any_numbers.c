#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int counter = 0;

struct d_int_arr {
	int *arr;
	size_t cap;
};

struct d_int_arr new_d_int_arr() {
	const size_t default_cap = 1;
	struct d_int_arr arr = {.arr=malloc(sizeof(int) * default_cap),
				.cap=default_cap};
	return arr;
}

void delete_d_int_arr(struct d_int_arr arr) {
	free(arr.arr);
}

void insert_to_d_int_arr(struct d_int_arr *arr, int idx, int val) {
	if (idx >= arr->cap) {
		arr->cap *= 2;
		arr->arr = realloc(arr->arr, sizeof(int) * arr->cap);
	}
	arr->arr[idx] = val;
}

void insertion_sort(int *arr, int len) {
	// 1. all elements in arr[0..i-1] are from originally within there
	// 2. all elements in arr[0..i-1] are sorted order
	for (int i = 1; i < len; i++) {
		int key = arr[i];

		int j = i - 1;
		while (j >= 0 && arr[j] > key) {
			arr[j+1] = arr[j];
			j--;
			counter++;
		}

		arr[j+1] = key;
	}
}

int main() {
	size_t len = 0;
	char *str = NULL; getline(&str, &len, stdin);

	char *tok = strtok(str, " ");

	struct d_int_arr arr = new_d_int_arr();
	int n = 0;
	while(tok != NULL) {
		insert_to_d_int_arr(&arr, n++, atoi(tok));
		tok = strtok(NULL, " ");
	}

	for(int i = 0; i < n; i++)
		printf("%d ", arr.arr[i]);
	printf("\n");

	insertion_sort(arr.arr, n);

	for(int i = 0; i < n; i++)
		printf("%d ", arr.arr[i]);
	printf("\n");

	free(str);
	delete_d_int_arr(arr);

	printf("counter: %d\n", counter);
	return EXIT_SUCCESS;
}
