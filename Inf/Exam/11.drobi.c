#include <stdio.h>

int main() {
    float n;
    scanf("%f", &n);
    int zn = 1;
    while (n != (int)n) {
        n *= 10;
        zn *= 10;
    }
    int ch = (int)n;
    while ((ch % 5 == 0) && (zn % 5 == 0)) {
        ch /= 5;
        zn /= 5;
    }
    while ((ch % 2 == 0) && (zn % 2 == 0)) {
        ch /= 2;
        zn /= 2;
    }
    printf("%d/%d", ch, zn);
}