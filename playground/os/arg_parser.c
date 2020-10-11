#include <argp.h>
#include <stdio.h>
#include <stdlib.h>

const char *argp_program_version = "0.1.0";
const char *argp_program_bug_address = "<dongho971220@gmail.com>";

static char doc[] = ""

int main(int argc, char *argv[])
{
    argp_parse(0, argc, argv, 0, 0, 0);

    return EXIT_SUCCESS;
}
