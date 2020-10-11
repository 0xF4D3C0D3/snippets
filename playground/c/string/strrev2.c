#include <stdio.h>
#include <stdlib.h>

char *strrev(char *str)
{
    const char *p = str;
    int len = 0; while(*p++) len++;

    char tmp;
    for(int i=0; i<len/2; i++){
        tmp = str[i];
        str[i] = str[len-1-i];
        str[len-1-i] = tmp;
    }

    return str;
}

int main(int argc, char *argv[])
{
    char s[] = "Hello, world!";
    strrev(s);
    printf("%s\n", s);

    char s2[] = "Hello, world";
    printf("%s\n", strrev(strrev(s2)));
}
