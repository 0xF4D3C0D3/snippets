#include <stdlib.h>

#include <stdbool.h>

#include <stdio.h>



int main() {

    int* p = malloc(sizeof(int));

    int* q = realloc(p, sizeof(int));

    *p = 1;

    *q = 2;

    if (p == q) {

        printf("p == q, *p is %d and *q is %d", *p, *q);

    } else {

        printf("p != q");

    }

}
