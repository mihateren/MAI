#include <stdio.h>
#include <math.h>

double pi = M_PI;

int main() {
    float a = 0.0, b = 4*pi;
    float x = 0.0;

    int counter = 0;
    while (x <= b) {
        if (counter % 4 == 0) {
            printf("|%5s%5s|\n", "*", "");
        }
        if ((counter % 4 == 1) || (counter % 4 == 3)) {
            if (sin(x) > 0) printf("|%7s%3s|\n", "*", "");
            else printf("|%3s%7s|\n", "*", "");
        }
        if (counter % 4 == 2) {
            if (sin(x) > 0) printf("|%10s%s|\n", "*", "");
            else printf("|%s%9s|\n", "*", "");
        }
        x += pi/4;
        counter++;
    }
}