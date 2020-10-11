#include "input.h"
#include "print.h"

void insertion_sort(int *L, int n)
{
	/* loop invariant: on the every start of iterations, L[0..i-1] is sorted order and
	 * consists of elements which have been originally within there.
	 *
	 * initialization: L[0] meets the loop invariant trivially
	 * maintenance: on the i-th iteration, L[0..i-1] have been sorted order and L[i] would move
	 *   to the left while it's compared with the value larger than it, or keep its position.
	 *   so on the next step i+1, L[0..i] have been sorted order and L[i] have been there,
	 *   hence L[0..(i+1)-1] satisfies the loop invariant
	 * termination: the loop terminates when i >= n = L.last_index + 1, so
	 *   [0..(L.last_index+1)-1] = L meets the loop invariant, that is the algorithm is correct.
	 */

	for (int i = 1; i < n; i++) {
		int key = L[i];

		int j = i-1;
		while (j >= 0 && L[j] > key) {
			L[j+1] = L[j];
			j--;
		}

		L[j+1] = key;
	}
}

int main()
{
	int *arr = NULL;
	int n = input_ints(&arr);

	printf("arr: ");
	print_ints(arr, n);

	insertion_sort(arr, n);
	print_ints(arr, n);

	free(arr);

	return EXIT_SUCCESS;
}
