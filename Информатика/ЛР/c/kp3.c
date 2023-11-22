#include <stdio.h>
#include <math.h>

const double a = 0.0;
const double b = 1.0;
const int n = 100;

const int fieldSize = 18;
const int columnsCount = 4;

float myPow(float x, int n) {
    float res = 1.0;
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
    double result, lastResult;
    lastResult = 0;
    int n = 2;
    do {
        result = lastResult;
        lastResult = myPow(-1, n - 1) * ((float)(n - 1) / myFact(n)) * myPow(x, n);
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
    double step = (b - a) / n;
    double x = a;
    double eps = 0.0001;

    typeSplitter();
    typeHeader();
    typeSplitter();
    for (int i = 0; i <= n; i++) {
        double fVal = calcF(x);
        double fTaylorVal = calcFTaylor(x, eps);
        printf("| %18.3f | %18.15f | %18.15f | %18.3d |\n", x, fVal, fTaylorVal, i);
        x += step;
    }
    typeSplitter();
    return 0;
}