#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int** createDynamicMatrix(int n) {
    int** array = (int**)malloc(n * sizeof(int*)); // Выделяем память под указатели на строки
    for (int i = 0; i < n; i++) {
        array[i] = (int*)malloc(n * sizeof(int)); // Выделяем память под каждую строку
    }
    return array;
}


void fillMatrix(int** matrix, int size){
    int value = 1;
    int topRow = 0, bottomRow = size - 1, leftCol = 0, rightCol = size - 1;

    while ((topRow <= bottomRow) && (leftCol <= rightCol)) {
        for (int i = topRow; i <= bottomRow; i++) {
            matrix[i][leftCol] = value;
            value++;
        }
        leftCol++;

        for (int i = leftCol; i <= rightCol; i++) {
            matrix[bottomRow][i] = value;
            value++;
        }
        bottomRow--;

        for (int i = bottomRow; i >= topRow; i--) {
            matrix[i][rightCol] = value;
            value++;
        }
        rightCol--;

        for (int i = rightCol; i >= leftCol; i--) {
            matrix[topRow][i] = value;
            value++;
        }
        topRow++;
    }
}


void printMatrix(int** matrix, int size) {
    int i, j;
    for (i = 0; i < size; i++){
        for (j = 0; j < size; j++){
            printf("%2d ", matrix[i][j]);
        }
        printf("\n");
    }
}


void freeMatrix(int** matrix, int size) {
    for (int i = 0; i < size; i++) {
        free(matrix[i]);
    }
    free(matrix);
}


int main() {
    int size;
    printf("Введите размер матрицы: ");
    scanf("%d", &size);

    int** matrix = createDynamicMatrix(size); // создаем двумерный массив заданного порядка
    fillMatrix(matrix, size); // заполняем матрицу нужными значениями

    printf("Матрица нужного шаблона: \n");
    printMatrix(matrix, size); // смотрим результат

    freeMatrix(matrix, size); // очищаем память
    return 0;
}