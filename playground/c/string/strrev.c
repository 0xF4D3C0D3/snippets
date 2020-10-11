#include <stdio.h>
#include <stdlib.h>

char *strrev(const char *str)
{
    const char *p = str;
    int len = 0; while(*p++) len++;

    char *rstr = (char *)malloc(sizeof(char) * len + 1);
    for(int i=0; i<len; i++) rstr[i] = str[len-1-i];
    rstr[len] = '\0';

    return rstr;
}

int main(int argc, char *argv[])
{
    char *s = strrev("Hello, world!");
    printf("%s\n", s);
    free(s);
}
