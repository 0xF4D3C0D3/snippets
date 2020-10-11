#include <stdio.h>

int main()
{
	int base = 0;
#ifdef CONST
	const int i = 0x42;
#endif
	register unsigned long int rbp asm("%rbp"); 

	printf("stack size: %lu\n", rbp - (unsigned long int)&base);

	return 0;
}
