#include <stdio.h>
#include <stdbool.h>
#include <math.h>

// функция acos(x) - sqrt(1 - 0.3 * x * x * x);

const double eps = 0.0001;
const double ans = 0.5629;

double fi(double x){
    return cos(sqrt(1 - 0.3 * x * x * x));
}

double myAbs(double x) {
    if (x < 0) return -x;
    return x;
}

double iter(int a, int b) {
    double x0 = (a + b) / 2.0;
    double xi = x0;
    while (myAbs(xi - ans) > eps){
        xi = fi(x0);
        x0 = xi;
    }
    return xi;
}

int main(void) {
    int a = 0, b = 1;
    printf("%f", iter(a, b));
    return 0;
}
