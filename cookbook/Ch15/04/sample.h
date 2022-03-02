/* sample.h */

#include <math.h>

extern int gcd(int,int);
extern int in_mandel(double x0, double y0, int n);
extern int divide(int a, int b, int *remainder);

typedef struct Point {
	double x, y;
} Point;
extern double distance(Point *p1, Point *p2);
