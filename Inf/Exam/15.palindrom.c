#include <stdio.h>
#include <math.h>

int main() {
    int n;
    scanf("%d", &n);
    int n1 = n;
    int counter = 0;

    while (n1 > 0) {
        counter++;
        n1 /= 10;
    }

    int temp;
    int razr;
    while (n > 0) {
        int ost = n % 10;
        razr = pow(10, counter - 1);
        temp = (n % razr) / 10;
        n /= razr;
        if (ost != n) {
            printf("NO");
            return 0;
        }
        counter -= 2;
        n = temp;
    }
    printf("YES");
}