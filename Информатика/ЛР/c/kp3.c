#include <stdio.h>
#include <math.h>

const float a = 0.0;
const float b = 1.0;

const int fieldSize = 18;
const int columnsCount = 4;

float getEps() {
    float epsilon = 1.0;
    while ((float)(1.0 + (epsilon / 2.0)) != 1.0) {
        epsilon /= 2.0;
    }
    return epsilon;
}


float myPow(float x, int n) {
    float res = 1.0;
    if (n < 0) return 1 / myPow(x, -n);
    for (int i = 0; i < n; i++) res *= x;
    return res;
}

int myFact(int n) {
    int res = 1;
    for (int i = 1; i <= n; i++) res *= i;
    return res;
}

float calcF(float x) {
    return (1 + x) * exp(-x);
}


float calcFTaylor(float x, int* pn, float eps) {
    int iter = 1;
    int currN = 2;
    float ret = 1;
    float izm = 0;
    do {
        iter += 1;
        izm = myPow(-1, (currN - 1)) * ((currN - 1) / (float)myFact(currN)) * myPow(x, currN);
        ret += izm;
        currN += 1;
    } while (izm > eps);
    *pn = iter;
    return ret;
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
    float step = (b - a) / steps;
    float x = a;
    typeSplitter();
    typeHeader();
    typeSplitter();
    float eps = getEps();
    for (int i = 0; i <= steps; i++) {
        int n = 0;
        int* pn = &n;
        float fVal = calcF(x);
        float fTaylorVal = calcFTaylor(x, pn, eps);
        printf("| %18.3f | %18.15f | %18.15f | %18.3d |\n", x, fVal, fTaylorVal, n);
        x += step;
    }
    typeSplitter();
    return 0;
}