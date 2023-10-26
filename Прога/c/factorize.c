#include <stdio.h>

void factorize( int n, int* a, int* b )
{
    for (int i = 2; i <= n / 2; i++){
        if (n % i == 0){
            *a = i;
            *b = n / i;
            break;
        }
    }
    if (*a == -1 && *b == -1){
        *a = 1;
        *b = n;
    }
}

int main(){
    int a = -1, b = -1, n = -1;
    int* A = &a;
    int* B = &b;
    scanf("%d", &n);
    factorize(n, A, B);
    printf("%d, %d", a, b);
    return 0;
}