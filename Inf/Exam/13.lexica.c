#include <stdio.h>

int main() {
    char c;
    char prev;
    prev = getchar();

    while ((c = getchar()) != '\n') {
        if (c == ' ') {
            continue;
        }
        if (prev > c) {
            printf("NO");
            return 0;
        }
        prev = c;
    }
    printf("YES");
}