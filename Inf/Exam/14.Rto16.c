#include <stdio.h>
#include <math.h>

int main() {
    float n;
    int sig;
    printf("Введите вещественное число и количество знаков после запятой у результата: ");
    scanf("%f %d", &n, &sig);

    int cel = trunc(n);
    printf("%x.", cel);
    for (int i = 0; i < sig; i ++) {
        n = n - trunc(n);
        n *= 16;
        printf("%x", (int)trunc(n));
    }
}