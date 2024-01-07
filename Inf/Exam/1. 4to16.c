#include <stdio.h>


int main() {
    int n = 0;
    scanf("%d", &n);

    char ans[500] = "";
    int i = 0;
    while (n > 0) {
        int ost = n % 100;
        if (ost == 0) ans[i] = 0;
        else if (ost == 1) ans[i] = '1';
        else if (ost == 2) ans[i] = '2';
        else if (ost == 3) ans[i] = '3';
        else if (ost == 10) ans[i] = '4';
        else if (ost == 11) ans[i] = '5';
        else if (ost == 12) ans[i] = '6';
        else if (ost == 13) ans[i] = '7';
        else if (ost == 20) ans[i] = '8';
        else if (ost == 21) ans[i] = '9';
        else if (ost == 22) ans[i] = 'A';
        else if (ost == 23) ans[i] = 'B';
        else if (ost == 30) ans[i] = 'C';
        else if (ost == 31) ans[i] = 'D';
        else if (ost == 32) ans[i] = 'E';
        else if (ost == 33) ans[i] = 'F';
        i++;
        n /= 100;
    }
    for (int j = i - 1; j >= 0; j--){
        printf("%c", ans[j]);
    }
}