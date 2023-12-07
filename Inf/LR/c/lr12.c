#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>


char* readFromFile(const char* filename) {
    FILE* file = fopen(filename, "r");
    if (file == NULL) {
        printf("Не удалось открыть файл.\n");
        return NULL;
    }
    // Определяем размер файла
    fseek(file, 0, SEEK_END);
    long fileSize = ftell(file);
    fseek(file, 0, SEEK_SET);
    // Выделяем память для считываемого текста
    char* text = (char*)malloc(fileSize + 1);
    if (text == NULL) {
        printf("Не удалось выделить память.\n");
        fclose(file);
        return NULL;
    }
    // Считываем текст из файла
    size_t bytesRead = fread(text, 1, fileSize, file);
    // Добавляем завершающий нулевой символ
    text[bytesRead] = '\0';
    fclose(file);
    return text;
}


int countWord(const char* text) {
    int count = 0;
    bool in_word = false;
    int word_length = 0;

    for (int i = 0; text[i] != '\0'; i++) {
        if (text[i] != ' ' && text[i] != '\n' && text[i] != '\t') {
            word_length++;
            in_word = true;
        } else {
            if (in_word && word_length >= 3) {
                count++;
            }
            in_word = false;
            word_length = 0;
        }
    }

    if (in_word && word_length >= 3) {
        count++;
    }
    return count;
}


int main() {
    char filename[256];
    printf("Введите название файла: ");
    scanf("%s", filename);

    char* text = readFromFile(filename);
    printf("%d", countWord(text));

    free(text); // Освобождение памяти
    return 0;
}
