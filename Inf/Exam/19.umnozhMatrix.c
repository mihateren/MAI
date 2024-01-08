#include <stdio.h>

int main() {
    int m1, n1;
    printf("Введите размеры первой матрицы: ");
    scanf("%d %d", &m1, &n1);
    int m2, n2;
    printf("Введите размеры второй матрицы: ");
    scanf("%d %d", &m2, &n2);

    if (n1 != m2) {
        printf("Нельзя такие матрицы умножить");
        return 0;
    }

    int arr1[m1][n1];
    printf("Введите первую матрицу: \n");
    for (int i = 0; i < m1; i++) {
        for (int j = 0; j < n1; j++) {
            scanf("%d", &arr1[i][j]);
        }
    }
    int arr2[m2][n2];
    printf("Введите вторую матрицу: \n");
    for (int i = 0; i < m2; i++) {
        for (int j = 0; j < n2; j++) {
            scanf("%d", &arr2[i][j]);
        }
    }

    for (int i = 0; i < m1; i++) {
        for (int j = 0; j < n2; j ++) {
            int res = 0;
            for (int k = 0; k < n1; k++) {
                res += arr1[i][k] * arr2[k][j];
            }
            printf("%d ", res);
        }
        printf("\n");
    }
}