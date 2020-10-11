#include <stdio.h>

#define MAX_LEN 20

void InsertionSort(int * arr){
	int i,j;
	int key;

	for(i=1; i<MAX_LEN; i++){
		key = arr[i];

		for(j=i-1; j>=0; j--)
			if(arr[j] >key){
				if(arr[j] > key)
					arr[j+1] = arr[j];
				else
					break;
			}

		arr[j+1] = key;
	}
}

int main(void){
	int arr[MAX_LEN] = { 3, 8, 17, 11, 6, 2, 15, 19, 10, 16, 18, 13, 1, 5, 7, 8, 4, 12, 14, 9, 20};

	InsertionSort(arr);

	return 0;
}

