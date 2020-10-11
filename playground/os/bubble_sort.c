#include <stdio.h>
#include <stdlib.h>

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

void bubble_sort(int *arr, int N)
{
    for (int i=0; i<N; i++) {
        for (int j=i; j>0; j--) {
            if (arr[j] < arr[j-1])
                swap(&arr[j], &arr[j-1]);   
        }
    }
}

void print_arr(int *arr, int N)
{
    for (int i=0; i<N; i++)
        printf("arr[%d]: %d\n", i, arr[i]);
    printf("\n");
}

int main(int argc, char *argv[])
{
    const int N = argc-1;
    int *arr = (int *)malloc(sizeof(int)*N);

    printf("N: %d\n", N);

    for (int i=0; i<N; i++)
        arr[i] = atoi(argv[i+1]);

    print_arr(arr, N);

    bubble_sort(arr, N);

    print_arr(arr, N);
}
