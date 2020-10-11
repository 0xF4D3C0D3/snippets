#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    char input[BUFSIZ];
    int numbers[256];

    scanf("%[^\n]", input);

    char *token = strtok(input, " ");
    int idx = 0;
    while(token != NULL) {
        printf("%d: %s\n", idx, token);
        numbers[idx++] = atoi(token);
        token = strtok(NULL, " ");
    }
    const int N = idx;

    int sum = 0;
    for(int i=0; i<N; i++)
        sum += numbers[i];

    printf("sum: %d\n", sum);

    return EXIT_SUCCESS;
}
