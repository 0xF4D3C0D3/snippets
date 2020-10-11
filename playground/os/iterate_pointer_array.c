#include <stdio.h>

int main() {
    extern char _etext, _edata;

    char *p[] = {&_etext, &_edata, NULL};

    char **cur = p;

    while(*cur){
        printf("%p\n", *cur++);
    }
}
