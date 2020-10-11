#include <stdio.h>

char *reverse(const char *str)
{
    const char *p = str;
    int len = 0;
    while (*p++) len++;

    char rstr[512];
    for (int i=0; i<len; i++) {
        rstr[i] = str[len-1-i];
    }

    rstr[len] = '\0';
    return rstr;
}


int main(int argc, char *argv[])
{
    printf("%s\n", reverse("hello"));

    return 0;
}
