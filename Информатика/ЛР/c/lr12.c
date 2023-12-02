#include <stdio.h>


int main(void)
{
    double a = 0.1;
    double fix = (0.6 - 0.1) / 100;
    printf("    x      taylor   cosh   i\n");
    while (a <= 0.6)
    {
        printf("%f", a);
        printf(" ");
        printf("%f", Teylor(a));
        printf(" ");
        printf("%f", cosh(a));
        printf(" ");
        printf("%d", iter);
        printf("\n");
        a += fix;
    }
}