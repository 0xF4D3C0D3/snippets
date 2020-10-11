#include <stdio.h>
#include <stdlib.h>

char *repeat_char_n(char c, int n)
{
    int i;
    char *str = (char *)malloc(sizeof(char) * n + 1);

    for(i = 0; i < n; i++)
        str[i] = c;

    str[i] = '\0';
    return str;
}

int main(void)
{
    char *str = repeat_char_n('X', 5);
    
    printf("repeat_char_n address: %p %p\n", repeat_char_n, &repeat_char_n);
    printf("str: %s\n", str);

    return 0;
}
