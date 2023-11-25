#include <stdio.h>
#include <math.h>

const double a = 0.0;
const double b = 1.0;

const int fieldSize = 18;
const int columnsCount = 4;


double getEps() { 
    double eps = 1.0; 
    while (1.0 + eps > 1.0) eps /= 2.0; 
    return eps * 2.0; 
}

float myPow(float x, int n) {
    float res = 1.0;
    if (n < 0) return 1 / myPow(x, -n);
    for (int i = 0; i < n; i++) res *= x;
    return res;
}

float myFact(int n) {
    float res = 1;
    for (int i = 1; i <= n; i++) res *= i;
    return res;
}

double calcF(double x) {
    return (1 + x) * exp(-x);
}

double calcFTaylor(double x, double eps) {
    double result = 0, lastResult = 0;
    int n = 1;
    do {
        if (n == 0) lastResult = 1;
        else lastResult += myPow(-1, n - 1) * myPow(x,n) * (float)(n - 1) / myFact(n);
        result = lastResult;
        n += 1;
    } while (fabs(result - lastResult) >= eps);
    return lastResult;
}

void typeSplitter() {
    int columnWidth = fieldSize + 3;

    for (int i = 0; i < columnWidth * columnsCount; i++) {
        if (i % columnWidth == 0) {
            printf("+");
            continue;
        } 

        printf("-");
    }

    printf("+\n");
}

void typeHeader() {
    printf("| %18s | %18s | %18s | %18s |\n", "x value", "f(x) - function", "f(x) - Taylor", "Iteration");
}

int main() {
    int steps = 100;
    double step = (b - a) / steps;
    double x = a;
    double eps = getEps();
    typeSplitter();
    typeHeader();
    typeSplitter();
    for (int i = 0; i <= steps; i++) {
        int n = 0;
        double fVal = calcF(x);
        double fTaylorVal = calcFTaylor(x, eps);
        printf("| %18.3f | %18.15f | %18.15f | %18.3d |\n", x, fVal, fTaylorVal, n);
        x += step;
    }
    typeSplitter();
    return 0;
}