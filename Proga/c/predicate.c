#include <stdlib.h>
#include <stdio.h>


int predicate(int num) {
    if (num % 2 == 0) return 1;
    return 0;
}


int array_contains(int* array, int* limit, int** position) {
    if (array >= limit) return 0;
    for (int* i = array; i < limit; i++){
        if (predicate(*i)){
            *position = i;
            return 1;   
        }
    }
    return 1;
}


int main() {
    int array[4] = {1, 2, 3, 4};
    int size = sizeof(array) / sizeof(int); 
    int* limit = array + size - 1;
    int* position = NULL;
    printf("%d", &limit);
    // printf("%d", array_contains(*array, *limit, ))
    return 0;
}

