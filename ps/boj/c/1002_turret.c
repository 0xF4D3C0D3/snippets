#include <math.h>
#include <stdio.h>
#include <stdlib.h>

double get_dist(int x1, int y1, int x2, int y2)
{
	return sqrt((double)(x2-x1)*(x2-x1) + (y2-y1)*(y2-y1));
}

int main()
{
	int T;
	scanf("%d", &T);

	for (int i=0; i<T; i++) {
		int x1, y1, r1, x2, y2, r2;
		scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);

		double dist = get_dist(x1, y1, x2, y2);

		if (r1 + r2 < dist || abs(r1 - r2) > dist)
			printf("0\n");
		else if (r1 + r2 > dist && dist > abs(r1 - r2))
			printf("2\n");
		else if (dist != 0 && (r1 + r2 == dist || r1 + r2 == abs(r1 - r2)))
			printf("1\n");
		else
			printf("-1\n");

	}

	return 0;
}
