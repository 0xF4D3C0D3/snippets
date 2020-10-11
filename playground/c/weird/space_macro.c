#include <stdio.h>

#define KERN_SOH    "1"
#define KERN_INFO   KERN_SOH "6"

int main(void) {
    printf(KERN_INFO "hello!\n");
    printf(KERN_INFO"hello!\n");

    return 0;
}
