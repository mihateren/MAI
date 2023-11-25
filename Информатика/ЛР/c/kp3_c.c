#include <stdio.h>
#include <math.h>

// Функция для вычисления факториала числа
int myFact(int n) {
    if (n <= 1)
        return 1;
    else
        return n * myFact(n - 1);
}

// Функция для вычисления степени числа
double myPow(double x, int n) {
    double result = 1.0;
    for (int i = 0; i < n; i++) {
        result *= x;
    }
    return result;
}

// Функция для вычисления значения ряда Тейлора
double taylorSeries(double x, int n) {
    return myPow(-1, n - 1) * (n - 1) * myPow(x, n) / myFact(n - 1);
}

int main() {
    double x = 0.0;
    double step = 0.01;

    printf("x\t\t(1+x)*e^(-x)\t\tTaylor Series\n");
    for (x = 0.0; x <= 1.0; x += step) {
        double fx = (1 + x) * exp(-x);
        double taylor = 0.0;
        for (int n = 1; n <= 10; n++) {  // Вычисляем 10 членов ряда Тейлора
            taylor += taylorSeries(x, n);
        }
        printf("%.2f\t\t%.6f\t\t%.6f\n", x, fx, taylor);
    }

    return 0;
}
