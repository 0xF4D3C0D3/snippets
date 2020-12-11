#include <stdio.h>

#include <sys/time.h>

#define PAGESIZE 4273
#define N 100

int loop_in_pagesize()
{
	int arr[PAGESIZE * N];

	for (int i = 0; i < PAGESIZE * N; i++) {
		int idx = (i%N)*PAGESIZE + i/N;
		arr[i] = i;
	}	

	int sum = 0;

	for (int i = 0; i < PAGESIZE * N; i++) {
		int idx = (i%N)*PAGESIZE + i/N;
		sum = (sum + arr[i]) % 100;
	}	

	return sum;
}

int loop_out_of_pagesize()
{
	int arr[PAGESIZE * N];

	for (int i = 0; i < PAGESIZE * N; i++) {
		int idx = (i%N)*PAGESIZE + i/N;
		arr[idx] = i;
	}	

	int sum = 0;

	for (int i = 0; i < PAGESIZE * N; i++) {
		int idx = (i%N)*PAGESIZE + i/N;
		sum = (sum + arr[idx]) % 100;
	}	

	return sum;
}

int main()
{
	struct timeval start, end;
	int n = 1000;
	printf("PAGESIZE: %d\n", PAGESIZE);

	gettimeofday(&start, NULL);
	for (int i = 0; i < n; i++)
		loop_in_pagesize();
	gettimeofday(&end, NULL);

	printf("loop in pagesize: %.4lf sec\n", (end.tv_sec - start.tv_sec) + (end.tv_usec - start.tv_usec) / 1e6);


	gettimeofday(&start, NULL);
	for (int i = 0; i < n; i++)
		loop_out_of_pagesize();
	gettimeofday(&end, NULL);

	printf("loop out of pagesize: %.4lf sec\n", (end.tv_sec - start.tv_sec) + (end.tv_usec - start.tv_usec) / 1e6);
	printf("\n");
	return 0;
}
