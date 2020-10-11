#include <signal.h>
#include <stdio.h>

int flag = 1;

void intHandler(int dummy)
{
    flag = 0;
}

int main(void)
{
    signal(SIGINT, intHandler);

    while(flag);

    return 0;
}
