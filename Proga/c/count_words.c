#include <stdio.h>


int is_whitespace(char c) { return c == ' ' || c == '\t' || c == '\n'; }

int string_count(char* str) { 
   int counter = 0;
   for (char* i = str; *i != 0; i++){
        counter++;
   }
   return counter;
}

int string_words(char* str)  {
    int count_words = 0;
    int flag = 0;
    for (char* i = str; *i != 0; i++){
        if (is_whitespace(*i)){
            if (flag) count_words++;
            flag = 0;
        }
        else {
            flag = 1;
        }
    }
    if (flag) count_words++;
    return count_words;
}

int main(){
    char s[] = "hello  world";
    printf("%d\n", string_count(s));
    printf("%d\n", string_words(s));
    return 0;
}