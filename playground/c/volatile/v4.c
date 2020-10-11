#include <signal.h>
#include <stdio.h>
#include <unistd.h>

double ctr = 10;
double *p = &ctr;

void intHandler(int dummy)
{
    *p -= 1.1;
}

int main(void)
{
    signal(SIGINT, intHandler);

    while(ctr >= 0) {
        printf("ctr: %f\n", *p);
        sleep(1);
    }
}
