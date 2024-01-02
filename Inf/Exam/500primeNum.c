#include <stdio.h>

int main() {
    int resheto[100000] = {0};
    for (int i = 2; i < 100000; i++) {
        if (resheto[i] == 1) continue;
        for (int j = 2; i * j < 100000; j++) {
            resheto[i * j] = 1;
        }
    }
    int counter = 0;
    for (int i = 2; i < 100000; i ++) {
        if (resheto[i] == 0) {
            printf("%d ", i);
            counter++;
        }
        if (counter == 500) break;
    }
    return 0;
}