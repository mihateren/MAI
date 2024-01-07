#include <stdio.h>

int main() {
    int num1, num2=0, byte, reverse=0;
    scanf("%d",&num1);

    while (num1 > 0) {
        byte = num1 % 256;
        reverse = 0;  // Сброс значения перед внутренним циклом

        int i = 128;
        while (byte > 0) {
            reverse += ((byte % 2) * i);
            i /= 2;
            byte /= 2;
        }

        num2 = num2 * 256 + reverse;
        num1 /= 256;
    }

    printf("%d", num2);
    
    return 0;
}
