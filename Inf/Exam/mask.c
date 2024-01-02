#include <stdio.h>


int main() {
    int n = 0, mask = 0;
    scanf("%d", &n);
    scanf("%d", &mask);   

    int ans[500] = {0};
    int i = 500;
    int ostN = 0, ostM = 0;

    while (n > 0 && mask > 0) {
        ostN = n % 10;
        n /= 10;
        ostM = mask % 10;
        mask /= 10;

        ans[i] = ostN * ostM;
        i--;
    }

    if (mask == 0 && n != 0) {
        printf("%d", n);
    }
    for (int j = i + 1; j < 501; j++){
        printf("%d", ans[j]);
    }

}