#include <stdio.h>

int main() {
    int n;
    printf("%s", "Введите размер матрицы: ");
    scanf("%d", &n);

    int a, b, c;
    printf("%s", "Введите коэффициенты: ");
    scanf("%d %d %d", &a, &b, &c);

    int arr[n][n];
    printf("%s\n", "Введите исходную матрицу: ");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &arr[i][j]);
        }
    }

    int matr[n][n];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            matr[i][j] = 0; 
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                matr[i][j] += arr[i][k] * arr[k][j];
            }
        }
    }

    printf("%s\n", "Квадрат матрицы:");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%d ", matr[i][j]); 
        }
        printf("\n");
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            matr[i][j] = a * matr[i][j] + b * arr[i][j] + c; 
        }
    }
    printf("%s\n", "Квадратный матрочлен:");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%d ", matr[i][j]); 
        }
        printf("\n");
    }
}