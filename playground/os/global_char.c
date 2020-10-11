#include <stdio.h>

char *aa = "aa";
char bb[] = "bb";
static char *cc = "cc";
static char dd[] = "dd";
const char *ee = "ee";
const char ff[] = "ff";
const static char *gg = "gg";
const static char hh[] = "hh";

static zz = 1;
static *xx = "xx";

const char *get_which_segment(const void *p) {
    extern char _etext, _edata;

    static char *segments = {&_etext, &_edata, NULL};
    
    char *cur = segments;
    while(*cur){
        printf("%p \n", cur++);
    }
}

int main() {
    printf("\
char *aa = \"aa\";\n\
char bb[] = \"bb\";\n\
static char *cc = \"cc\";\n\
static char dd[] = \"dd\";\n\
const char *ee = \"ee\";\n\
const char ff[] = \"ff\";\n\
const static char *gg = \"gg\";\n\
const static char hh[] = \"hh\";\n\n\
");
    printf("printf(\"aa : %%p %%p\\n\", aa, &aa);\n");
    printf("aa : %p %p %s\n", aa, &aa, get_which_segment(aa));
    printf("bb : %p %p\n", bb, &bb);
    printf("cc : %p %p\n", cc, &cc);
    printf("dd : %p %p\n", dd, &dd);
    printf("ee : %p %p\n", ee, &ee);
    printf("ff : %p %p\n", ff, &ff);
    printf("gg : %p %p\n", gg, &gg);
    printf("hh : %p %p\n", hh, &hh);
}
