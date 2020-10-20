#include "algo.h"

#include <string.h>

int max(int a, int b)
{
	return a > b ? a : b;
}

void strrev(char *str)
{
	int len = strlen(str);
	char tmp;
	for (int i=0; i<len/2; i++) {
		tmp = str[i];
		str[i] = str[len-1-i];
		str[len-1-i] = tmp;
	}
}

int digit_sum(const char *str1, const char *str2, int idx)
{
	int len1 = strlen(str1);
	int len2 = strlen(str2);

	if (idx >= len1)
		return str2[idx] - '0';
	else if (idx >= len2)
		return str1[idx] - '0';
	else
		return str1[idx] + str2[idx] - '0'*2;
}

int main(int argc, char *argv[])
{
	if (argc != 3) {
		fprintf(stderr, "usage: ./add binary_number1 binary_number2\n");
		return EXIT_FAILURE;
	}

	int n = max(strlen(argv[1]), strlen(argv[2]));

	printf("   %0*lu\n", n, atol(argv[1]));
	printf("+  %0*lu\n", n, atol(argv[2]));

	strrev(argv[1]);
	strrev(argv[2]);

	char *sum = malloc(sizeof(char) * (n+1+1));
	int carry = 0;
	for (int i=0; i < n; i++) {
		int tmp = digit_sum(argv[1], argv[2], i) + carry;
		sum[i] = '0' + (tmp % 2);
		carry = floor(tmp/2);
	}
	sum[n] = '0' + carry;
	sum[n+1] = '\0';

	strrev(sum);

	printf("= %s\n", sum);
	return EXIT_SUCCESS;
}
