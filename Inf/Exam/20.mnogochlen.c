#include <stdio.h>

int main() {
    int n, m;
    printf("Введите наибольшую степень первого и второго многочлена соответственно: ");
    scanf("%d %d", &n, &m);

    int arr1[n + 1];
    int arr2[m + 1];
    for (int i = n; i >= 0; i--) {
        printf("Введите коэффициент при x^%d первого многочлена: ", i);
        scanf("%d", &arr1[i]);
    }
    for (int i = m; i >= 0; i--) {
        printf("Введите коэффициент при x^%d второго многочлена: ", i);
        scanf("%d", &arr2[i]);
    }

    int res[n * m + 1];
    for (int i = 0; i < n * m + 1; i++) {
        res[i] = 0;
    }
    for (int i = n; i >= 0; i--) {
        for (int j = m; j >= 0; j--) {
            res[i + j] += arr1[i] * arr2[j];
        }
    }

    printf("\nРезультат перемножения: ");
    int flag = 1;
    for (int i = m * n; i >= 0; i--) {
        if (i != 0) {
            if (res[i] > 0 && flag) {
                printf("%d*x^%d", res[i], i);
                flag = 0;
            }
            else if (res[i] > 0 && i != m * n) {
                printf("+%d*x^%d", res[i], i);
                flag = 0;
            }
            else if (res[i] < 0) {
                printf("%d*x^%d", res[i], i);
                flag = 0;
            }
        }
        else {
            printf("%d", res[i]);
            flag = 0;
        }
    }
}