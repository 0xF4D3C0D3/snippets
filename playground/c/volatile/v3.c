#include <stdio.h>
#include <stdlib.h>

int main(void) {
    volatile int *ptr = malloc(sizeof(int));

    *ptr = 0x10;
    *ptr = 0x20;
    *ptr = 0x30;
}
