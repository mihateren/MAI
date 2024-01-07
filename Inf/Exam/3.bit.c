#include <stdio.h>

int main() {
    int n, pos;
    scanf("%d %d", &n, &pos);

    int n1 = n;
    int len = 0;
    while (n1 > 0) {
        len++;
        n1 /= 2;
    }

    int i = 0;
    int ost;
    while (i != (len - pos - 1)) {
        ost = n % 2;
        n /= 2;
        i++;
    }
    printf("%d", ost);
}