#include <stdio.h>

void array_fib(int* array, int* limit) {
    int lenArr = limit - array;
    int k = 1;
    if (lenArr == 0) return;
    for (int* i = array; i < limit; i++){
        if (k < 3) *i = 1;
        else {
            *i = *(i - 1) + *(i - 2);
        }
        k++;
    }
}

int main(){
    int arr[1] = {0};
    int* p = arr;
    int* limit = p + 1;
    array_fib(p, limit);
    for (int i = 0; i < 1; i++){
        printf("%d\n", arr[i]);
    }
    return 0;
}