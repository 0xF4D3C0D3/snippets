#include "algo.h"

#define NOT_FOUND -1

int linear_search(int *L, int n, int v)
{
	/* loop invariant: on the i-th iteration, L[0..i-1] doesn't contain any value equal to v. 
	 *
	 * initialization: when i = 0, the subarray is empty, so none of its elements are equal to v.
	 *   and it meets the loop invariant.
	 * maintenance: on the i-th iteration, L[0..i-1] doesn't contain any value equal to v,
	 *   and check L[i] whether it's equal to v or not, if it doesn't then continue next
	 *   iterations, else terminate. so it meets the loop invariant unless the loop terminates.
	 * termination: the loop terminates when i >= n = L.last_index + 1 or L[i] == v, so it turns
	 *   out to be one of these. L[0..(L.last_index+1)-1] = L doesn't contain any value equal
	 *   to v then return -1 which means not found, or i the index for the value equal to v
	 */

	for (int i = 0; i < n; i++)
		if (L[i] == v)
			return i;
	return NOT_FOUND;
}

int main()
{
	printf(">>> input numbers: ");
	int *arr = NULL;
	size_t n = input_ints(&arr);

	printf("[+] arr: ");
	print_ints(arr, n);

	printf("[?] ctrl+D to terminate\n");
	int v, ret;
	do {
		printf(">>> v: ");
		ret = scanf("%d", &v);
		if (ret == EOF) break;

		int idx = linear_search(arr, n, v);
		if (idx == NOT_FOUND)
			printf("[+] %d is not in arr\n", v);
		else
			printf("[+] arr[%d] -> %d\n", idx, v);
				
	} while (ret != EOF);
	return EXIT_SUCCESS;
}
