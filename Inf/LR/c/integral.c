#include <stdio.h>
#include <stdbool.h>
#include <math.h>

const int N = 10;

double f(double x){
    return 2 * x * x + x + 1;
}

double f1(double x){
    return cos(x);
}

double square(double x0, double x1){
    return (x1 - x0) * f((x0 + x1) / 2);
}

int main(void) 
{
    int a = 0, b = 5;
    double sum = 0;
    double step = (double)(b - a) / N;
    double tempX = a;
    for (int i = 0; i < N; i++){
        sum = sum + square(tempX, tempX + step);
        printf("%f\n", tempX);
        tempX += step;
    }
    printf("%f", sum);
    return 0;
}
