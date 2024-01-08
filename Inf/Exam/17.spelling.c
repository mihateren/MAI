#include <stdio.h>

char *d0_9[10] = {"ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"};
char *d10_19[10] = {"десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"};
char *d20_99[9] = {"двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"};
char *d100_999[9] = {"сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"};

void pr0_10(int n) {
    printf("%s", d0_9[n]);
}

void pr10_19(int n) {
    printf("%s", d10_19[n % 10]);
}

void pr20_99(int n) {
    printf("%s ", d20_99[(n / 10) - 2]);
    if (n % 10 > 0) printf("%s", d0_9[n % 10]);
}
    
void pr100_999(int n) {
    printf("%s ", d100_999[n / 100 - 1]);
    int ost = n % 100;
    if (ost > 0) {
        if (ost < 10) pr0_10(ost);
        else if (ost < 20) pr10_19(ost);
        else pr20_99(ost);
    }
}


void prLess1000(int n) {
    if (n < 10) pr0_10(n);
    else if (n < 20) pr10_19(n);
    else if (n < 100) pr20_99(n);
    else if (n < 1000) pr100_999(n);
}


void prMore1000(int n) {
    int elder = n / 1000;
    if (elder > 1000) {
        printf("Ввели много");  
        return;
    } 
    if (elder == 1) printf("%s ", "тысяча");
    else if (elder == 2) printf("%s ", "две тысячи");
    else if (elder <= 4) {
        pr0_10(elder);
        printf("тысячи");
    }
    else {
        if (elder < 1000) prLess1000(elder);
        if (elder % 10 >= 2 && elder % 10 <= 4 && (elder < 12 || elder > 14)) printf(" %s ", "тысячи");
        else printf(" %s ", "тысяч");
    }
    int ost = n % 1000;
    prLess1000(ost);
}


int main() {
    int n;
    scanf("%d", &n);
    if (n < 1000) prLess1000(n);
    else prMore1000(n);
}