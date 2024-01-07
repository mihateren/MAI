#include <stdio.h>
#include <math.h>

int main() {
    float n;
    scanf("%f", &n);
    int cel = trunc(n);

    int counter = 0;
    while (n != (int)n) {
        n *= 10;
        counter++;
    }
    int drob = (int)n - cel * pow(10, counter);

    char cel16[33] = {};
    int i = 0;
    while (cel > 0) {
        int ost = cel % 16;
        if (ost <= 9) cel16[i] = '0' + ost;
        else if (ost == 10) cel16[i] = 'A';
        else if (ost == 11) cel16[i] = 'B';
        else if (ost == 12) cel16[i] = 'C';
        else if (ost == 13) cel16[i] = 'D';
        else if (ost == 14) cel16[i] = 'E';
        else if (ost == 15) cel16[i] = 'F';
        i++;
        cel /= 16;
    }
    for (i; i >= 0; i--) printf("%c", cel16[i]);
    printf(".");

    // ЗАДАЧА ГРОБ
}