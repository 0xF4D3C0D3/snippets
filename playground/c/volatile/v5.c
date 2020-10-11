#include <signal.h>
#include <stdio.h>
#include <unistd.h>

int flag = 1;

void intHandler(int dummy)
{
    flag = 0;
}

int main(void)
{
    signal(SIGINT, intHandler);

    while(flag) {
        printf("I'm still waiting for flag to be off\n");
        sleep(1);
    }

    return 0;
}
