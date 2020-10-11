#include <stdio.h>

int main(void) {
    const int local = 0x30519;
    int *ptr = (int*) &local;

    printf("Initial value of local: %#x\n", local);

    *ptr = 0x971220;

    printf("Modified value of local: %#x\n", local);

    return 0;
}
