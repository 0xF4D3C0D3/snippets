#include <stdio.h>

int main(void)
{
    printf("char : %lu\n", sizeof(char));
    printf("short : %lu\n", sizeof(short));
    printf("int : %lu\n", sizeof(int));
    printf("long : %lu\n", sizeof(long));
    printf("unsigned : %lu\n", sizeof(unsigned));
    printf("unsinged int : %lu\n", sizeof(unsigned int));
    printf("unsigned long : %lu\n", sizeof(unsigned long));
    printf("float : %lu\n", sizeof(float));
    printf("double : %lu\n", sizeof(double));
    printf("unsigned long : %lu\n", sizeof(unsigned long));
    printf("unsigned long long : %lu\n", sizeof(unsigned long long));
    printf("void : %lu\n", sizeof(void));
    printf("void * : %lu\n", sizeof(void *));
    printf("int * : %lu\n", sizeof(int *));
    printf("unsinged int * : %lu\n", sizeof(unsigned int *));
    printf("int ** : %lu\n", sizeof(int **));
}
