#include <stdio.h>

void array_reverse(int* array, int size) {
    int k = 0;
    int* lastItem = array + size - 1;
    for (int* i = array; i <= lastItem; i++){
        int* endPointer = lastItem - k;
        int bubble = *i;
        *i = *endPointer;
        *endPointer = bubble;
        if (k < size / 2 - 1) k++;
        else break;
    }
}

void array_reverse_ptr(int* array, int* limit) {
    int k = 0;
    int size = limit - array;
    for (int* i = array; i <= limit; i++){
        int* endPointer = limit - k - 1;
        int bubble = *i;
        *i = *endPointer;
        *endPointer = bubble;
        if (k < size / 2 - 1) k++;
        else break;
    }
}

int main(){
    int arr[] = {10, 24, 3, 4, 5};
    int* p = arr;
    array_reverse(p, 5);
    int* lastItem = p + 5;
    array_reverse_ptr(p, lastItem);
    for (int i = 0; i < 5; i++){
        printf("%d\n", arr[i]);
    }
    return 0;
}