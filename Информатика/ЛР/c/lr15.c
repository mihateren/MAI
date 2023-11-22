#include <stdio.h>

#define SIZE 5

void scanMatrix (FILE * fp, int ** matrix)
{
    int i,j;
    for(i=0; i < SIZE; i++)
        for(j=0; j < SIZE; j++)
            fscanf(fp, "%Lf", &matrix[i][j]);
}


int main() {
    FILE * file = fopen("matrix.txt", "r");
    char matrix[SIZE][SIZE];
    scanMatrix(file, matrix);
    return 0;
}