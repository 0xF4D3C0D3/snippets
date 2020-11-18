#include "algo.h"

void find_max_crossing_subarray(int A[], int low, int mid, int high,
				int *max_left, int *max_right, int *max_sum)
{
	int left_sum = INT_MIN;
	int sum = 0;
	for (int i = mid; i >= low; i--) {
		sum += A[i];
		if (sum > left_sum) {
			left_sum = sum;
			*max_left = i;
		}
	}

	int right_sum = INT_MIN;
	sum = 0;
	for (int i = mid+1; i <= high; i++) {
		sum += A[i];
		if (sum > right_sum) {
			right_sum = sum;
			*max_right = i;
		}
	}
	*max_sum = left_sum + right_sum;
}

void find_max_subarray(int A[], int low, int high,
			int *max_low, int *max_high, int *max_sum)
{
	if (low == high) {
		*max_low = low;
		*max_high = high;
		*max_sum = A[low];
	} else {
		int mid = (low + high) / 2;
		int left_low, left_high;
		int left_sum;
		find_max_subarray(A, low, mid, &left_low, &left_high, &left_sum);

		int right_low, right_high;
		int right_sum;
		find_max_subarray(A, mid+1, high, &right_low, &right_high, &right_sum);

		int cross_low, cross_high;
		int cross_sum;
		find_max_crossing_subarray(A, low, mid, high, &cross_low, &cross_high, &cross_sum);

		if (left_sum >= right_sum && left_sum >= cross_sum) {
			*max_low = left_low;
			*max_high = left_high;
			*max_sum = left_sum;
		} else if (right_sum >= left_sum && right_sum >= cross_sum) {
			*max_low = right_low;
			*max_high = right_high;
			*max_sum = right_sum;
		} else {
			*max_low = cross_low;
			*max_high = cross_high;
			*max_sum = cross_sum;
		}
	}
}

int main(void)
{
	int *arr = NULL;
	int n = input_ints(&arr);

	printf("arr: ");
	print_ints(arr, n);

	int max_low, max_high;
	int max_sum;
	find_max_subarray(arr, 0, n-1, &max_low, &max_high, &max_sum);
	printf("from %d to %d, the sum is %d\n", max_low, max_high, max_sum);

	free(arr);

	return EXIT_SUCCESS;
}
