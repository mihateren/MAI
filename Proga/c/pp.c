#include <stdio.h>
int predicate(int n){
    return n > 4;
}
// position -- адрес указателя на первый элемент E в массиве,
// для которого predicate(E) выполняется.
// Функция возвращает 0 если элемент не найден.
int array_contains(int* array, int* limit, int** position) {
    if (array > limit) return 0;
    int k = 0;
    for (int* i = array; i < limit; i++){
        if (predicate(*i)){
            *position = k;
            break;
            k++;
        }
    }
    return 1;
}

int main(){
    int arr[] = {4, 29, 42, 2, 3};
    int* ans = NULL;
    array_contains(arr, arr + sizeof(arr) / sizeof(arr[0]), &ans);
    printf("%d", ans);
    return 0;
}