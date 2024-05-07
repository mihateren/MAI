#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>


#define CONSONANTS_MASK ((1UL << ('b' - 'a')) | (1UL << ('c' - 'a')) | \
                         (1UL << ('d' - 'a')) | (1UL << ('f' - 'a')) | \
                         (1UL << ('g' - 'a')) | (1UL << ('h' - 'a')) | \
                         (1UL << ('j' - 'a')) | (1UL << ('k' - 'a')) | \
                         (1UL << ('l' - 'a')) | (1UL << ('m' - 'a')) | \
                         (1UL << ('n' - 'a')) | (1UL << ('p' - 'a')) | \
                         (1UL << ('q' - 'a')) | (1UL << ('r' - 'a')) | \
                         (1UL << ('s' - 'a')) | (1UL << ('t' - 'a')) | \
                         (1UL << ('v' - 'a')) | (1UL << ('w' - 'a')) | \
                         (1UL << ('x' - 'a')) | (1UL << ('y' - 'a')) | \
                         (1UL << ('z' - 'a')))


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


int checkForConsonants(const char* inputString) {
    unsigned long consonants = 0;
    char buffer[256] = "";
    strncat(buffer, inputString, 256);

    if (strlen(inputString) == 0) {
        return 0;
    }

    for (int i = 0; inputString[i] != '\0'; i++) {
        tolower(inputString[i]);
        char sym = inputString[i];
        if (sym >= 'a' && sym <= 'z') {
            consonants |= (1UL << (sym - 'a'));
        }
    }
    printf("Дана строка %s", buffer);
    if (consonants & CONSONANTS_MASK) {
        printf(" - Найдена согласная буква.\n");
    } 
    else {
        printf(" - Нет согласных букв.\n");
    }
    return 1;
}


void checkStrings(const char* text, int size) {
    char buffer[256] = ""; 
    for (int i = 0; i < size; i++) {
        if (text[i] != '\n') {
            strncat(buffer, &text[i], 1);
        } 
        else {
            strncat(buffer, "\0", 1);
            checkForConsonants(buffer);
            memset(buffer, 0, sizeof(buffer));
        }
    }
    checkForConsonants(buffer);
    memset(buffer, 0, sizeof(buffer));
}


int main() {
    char filename[256];
    printf("Введите название файла: ");
    scanf("%s", filename);

    char* text = readFromFile(filename);
    int size = strlen(text);

    checkStrings(text, size);

    free(text);
    return 0;
}