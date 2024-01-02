#include <stdio.h>

int main() {
    int n = -1, m = -1;
    int flag = 0;
    char c;
    while (c != EOF){
        c = getchar();
        if (c == '|') {
            if (!flag) n++;
            else m++;
        }
        else {
            if (!flag) flag = 1;
            else break;;
        }
    }
    printf("%d", n / m);
}