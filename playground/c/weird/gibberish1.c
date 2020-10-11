#include <stdio.h>

int foo(void){ return 0; }
int bar(){ return 0; }
void baz(void){}
void bam(){}

int main(void)
{
    int (*(*fp)(void))[4];

    fp = foo;

    return 0;
}
