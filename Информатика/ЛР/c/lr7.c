#include <stdio.h>
#include <stdbool.h>
#include <locale.h>

const int STEPS = 50;

bool funtionArea(int x, int y){
    if ((x >= -10) && (x <= 0) && (y >= x + 10) && (y <= -x + 10)){
        return true;
    }
    return false;
}

int myAbs(int x){
    if (x < 0){
        return -x;
    }
    return x;
}

int mySign(int x){
    if (x > 0){
        return 1;
    }
    if (x < 0){
        return -1;
    }
    return 0;
}

int myMax(int i, int j){
    if (i >= j){
        return i;
    }
    return j;
}

int myMin(int i, int j){
    if (i <= j){
        return i;
    }
    return j;
}

int main(void) 
{
    int i=-12, j=-22, l=11;
    int step=0, tmpI, tmpJ, tmpL;
    while (step <= STEPS){
        tmpI = i;
        tmpJ = j;
        tmpL = l;
        ++step;
        if (funtionArea(i,j)){
            printf("%d", step);
            return 0;
        }
        i = myMax(myMin(tmpI - tmpJ, tmpJ - tmpL) % 20, myMin(tmpI - tmpL, tmpJ - step) % 20) + 10;
        j = mySign(tmpI - tmpJ) * myMin(tmpI % 20, tmpJ % 20) - myMax(myAbs(tmpI - tmpL), myAbs(step - 20)) % 20 + 20;
        l = (tmpI % 10) * (tmpJ % 10) + tmpL % 10;
        // printf("%d, %d, %d, %d\n", step, i, j, l);
    }
    setlocale(LC_ALL, "Rus");
    printf("В цель промах\nШаг %d, %d, %d, %d", step, i, j, l);
    return 0;
}
