#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int checkSize(const char *filename) {
    FILE *file;
    char line[100]; // Максимальная длина строки
    int count = 0;
    file = fopen(filename, "r");
    if (file == NULL) {
        printf("Ошибка открытия файла\n");
        return -1; // Возвращаем -1 в случае ошибки открытия файла
    }
    if (fgets(line, 100, file) != NULL) { // Считываем первую строку из файла
        char *token = strtok(line, " "); // Разбиваем строку на отдельные слова
        while (token != NULL) {
            count++;
            token = strtok(NULL, " ");
        }
    }
    fclose(file);
    return count;
}


int** createDynamicMatrix(int n) {
    int** array = (int**)malloc(n * sizeof(int*)); // Выделяем память под указатели на строки
    for (int i = 0; i < n; i++) {
        array[i] = (int*)malloc(n * sizeof(int)); // Выделяем память под каждую строку
    }
    return array;
}


int readMatrix(int** matrix, int size, const char *filename) {
    FILE* f = fopen(filename, "r"); // Открываем файл для чтения
    if (f == NULL) {
        printf("Ошибка открытия файла\n");
        return -1; // Возвращаем -1 в случае ошибки открытия файла
    }
    fseek(f, 0, SEEK_SET); // Ставим указатель в начало файла для считывания
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++)
            fscanf(f, "%d", &matrix[i][j]);
    }
    fclose(f);
}


int* initArray(int size) {
    int *arr = (int *)malloc(size * sizeof(int));
    for (int i = 0; i < size; i++) {
        arr[i] = 0;
    }
    return arr;
}


int findMinElem(int** matrix, int size) {
    int min = INT_MAX;
    int i,j;
    for (i = 0; i < size; i++){
        for (j = 0; j < size; j++){
            if (matrix[i][j] < min){
                min = matrix[i][j];
            }
        }
    }
    return min;
}


void findMinStr(int** matrix, int* line, int size, int minim) {
    for (int i = 0; i < size; i++){
        for (int j = 0; j < size; j++){
            if (minim == matrix[i][j]){
                line[i] = 1;
                break;
            }
        }
    }
}


void printMatrix(int** matrix, int size) {
    int i, j;
    for (i = 0; i < size; i++){
        for (j = 0; j < size; j++){
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
}


void reverseStr(int** matrix, int* line, int size) {
    for (int i = 0; i < size; i++){
        int start = 0;
        int end = size - 1;
        while (start < end) {
            int temp = matrix[i][start];
            matrix[i][start] = matrix[i][end];
            matrix[i][end] = temp;
            start++;
            end--;
        }
    }
    
}


void freeMatrix(int** matrix, int size) {
    for (int i = 0; i < size; i++) {
        free(matrix[i]);
    }
    free(matrix);
}

int main() {
    char filename[256];
    printf("Введите название файла: ");
    scanf("%s", filename);

    int size = checkSize(filename); // узнаем порядок матрицы
    int** matrix = createDynamicMatrix(size); // создаем двумерный массив заданного порядка
    readMatrix(matrix, size, filename); // считываем в матрицу данные из файла

    printf("Изначальная матрица: \n");
    printMatrix(matrix, size);
    printf("\n");

    int* line = initArray(size); // инициализируем массив, инициализированный нулем
    int minim = findMinElem(matrix, size); // находим минимальный элемент матрицы
    findMinStr(matrix, line, size, minim); // находим строки, в которых содержится минимальный элемент
    reverseStr(matrix, line, size); // реверсим строки с минимальным элементом

    printf("Матрица после преобразований: \n");
    printMatrix(matrix, size); // смотрим результат

    freeMatrix(matrix, size); // очищаем память
    free(line);
    return 0;
}