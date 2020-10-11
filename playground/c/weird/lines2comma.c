#include <stdio.h>

int main(void)
{
    char ch;
    char str[256];
    char *p = str;

    while((ch = getchar()) != EOF) {
        if (ch == '\n')
            ch = ',';
        *p++ = ch;
    }
    *--p = '\0';

    printf("%s\n", str);
}
