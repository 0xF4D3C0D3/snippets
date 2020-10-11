#define _GNU_SOURCE
#include <sched.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

struct timespec timer_start()
{
    struct timespec start_time;
    if ( clock_gettime(CLOCK_MONOTONIC, &start_time) == -1 ) {
        perror("timer_start fail");
    }

    return start_time;
}

long timer_end(struct timespec start_time)
{
    struct timespec end_time;
    clock_gettime(CLOCK_MONOTONIC, &end_time);
    long diff_in_nanos = ((end_time.tv_sec - start_time.tv_sec) * (long)1e9 +
                          (end_time.tv_nsec - start_time.tv_nsec));

    return diff_in_nanos;

}

int main(int argc, char *argv[])
{
    cpu_set_t cpu;
    CPU_ZERO(&cpu);
    CPU_SET(atoi(argv[1]), &cpu);
    if (sched_setaffinity(getpid(), sizeof(cpu), &cpu) == -1)
        perror("NO WAY");


    struct timespec res;
    if ( clock_getres(CLOCK_MONOTONIC, &res) == -1) {
        perror("clock get resolution");
        return EXIT_FAILURE;
    }
 //   printf("Resolution is %ld nanoseconds\n", (unsigned int)(res.tv_sec*1e9) + res.tv_nsec);
    
    const unsigned int N = 10000000;
    struct timespec vartime = timer_start();

    for (int i=0; i<N; i++)
        getppid();

    long time_elapsed_nanos = timer_end(vartime);
    printf("elapsed time : %lums\n", time_elapsed_nanos/1000);

    return 0;
}
