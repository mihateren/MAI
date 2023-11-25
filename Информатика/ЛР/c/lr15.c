#include <stdio.h>
#include <stdbool.h>

#define SIZE 5  
int matrix[SIZE][SIZE];


void read_matrix() {
    FILE* f = fopen("matrix.txt", "r");
    fseek(f, 0, SEEK_SET);
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++)
            fscanf(f, "%d", &matrix[i][j]);
    }
}

int main() {
    int a, b;
    read_matrix();
    for (a = 0; a < SIZE; a++){
        for (b = 0; b < SIZE; b++){
            printf("%d ", matrix[a][b]);
        }
        printf("\n");
    }
    return 0;
}