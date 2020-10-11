#include "input.h"
#include "print.h"

void bubble_sort(int *L, int n)
{
	/* loop invariant: on the every start of i-th iteration, L[i-1] have (i-1)th smallest value, 
	 *   in other words, L[0..i-1] is sorted in ascending order.
	 *
	 * initialization: at first, when i = 1, the smallest value in L moves to the leftmost
	 *   one by one. so L[0] is the 0-th smallest value and it meets the loop invariant.
	 * maintenance: on the i-th iteration, L[0..i-1] has been sorted order and at the end of the
	 *   iteration, L[i] would be the smallest but larger than any values in L[0..i-1] that is
	 *   L[0..i] is sorted in ascending order. so on the next step i+1, L[0..(i+1)-1] meets the
	 *   loop invariant.
	 * termination: the loop terminates when i >= n = L.last_index + 1, so
	 *   L[0..(L.last_index+1)-1] = L is sorted in ascending order and the algorithm is correct.
	 */

	for (int i = 1; i < n; i++) {
		for (int j = n-1; j >= i; j--) {
			if (L[j-1] > L[j]) {
				int tmp = L[j-1];
				L[j-1] = L[j];
				L[j] = tmp;
			}
		}
	}
}

int main()
{
	int *arr = NULL;
	int n = input_ints(&arr);

	print_ints(arr, n);
	bubble_sort(arr, n);
	print_ints(arr, n);

	return EXIT_SUCCESS;
}
