#include <stdio.h>
#include <stdlib.h>

typedef struct Node
{
    char op;
    int numerator;
    int denominator;
    struct Node *left;
    struct Node *right;
} Node;

Node *createNode(char op, int numerator, int denominator)
{
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->op = op;
    newNode->numerator = numerator;
    newNode->denominator = denominator;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// No changes made here, assuming only "+" operation.
// For additional operations (-, *, /), you'd include more conditions to handle them.
void calculateTree(Node *node, int *resultNumerator, int *resultDenominator)
{
    if (node->op == '+')
    {
        int leftNumerator = 0, leftDenominator = 1, rightNumerator = 0, rightDenominator = 1;
        calculateTree(node->left, &leftNumerator, &leftDenominator);
        calculateTree(node->right, &rightNumerator, &rightDenominator);

        // Find a common denominator
        int commonDenominator = leftDenominator * rightDenominator;
        int leftMultiplier = commonDenominator / leftDenominator;
        int rightMultiplier = commonDenominator / rightDenominator;

        // Add the numerators after adjusting for the common denominator
        *resultNumerator = leftNumerator * leftMultiplier + rightNumerator * rightMultiplier;
        *resultDenominator = commonDenominator;
    }
    else
    {
        *resultNumerator = node->numerator;
        *resultDenominator = node->denominator;
    }
}

// No changes made to simplifyFraction.
void simplifyFraction(int *numerator, int *denominator)
{
    int a = abs(*numerator);
    int b = abs(*denominator);
    while (b)
    {
        int temp = a % b;
        a = b;
        b = temp;
    }
    *numerator /= a;
    *denominator /= a;
}

// Adjusted printTree for better readability.
void printTree(Node *node, int level)
{
    if (node == NULL)
        return;

    // Вывод правого поддерева
    printTree(node->right, level + 1);

    // Вывод текущего узла
    for (int i = 0; i < level; i++)
    {
        printf("    "); // Количество пробелов для отступа
    }
    if (node->op == '/')
    {
        printf("%c\n", node->op);
        for (int i = 0; i < level + 1; i++)
        {
            printf("    "); // Отступ для дочерних узлов
        }
        printf("%d\n", node->left->numerator);
        for (int i = 0; i < level + 1; i++)
        {
            printf("    "); // Отступ для дочерних узлов
        }
        printf("%d\n", node->right->numerator);
    }
    else if (node->op != 0)
    {
        printf("%c\n", node->op);
    }
    else
    {
        printf("%d/%d\n", node->numerator, node->denominator);
    }

    // Вывод левого поддерева
    printTree(node->left, level + 1);
}

// No changes made to freeTree.
void freeTree(Node *node)
{
    if (node == NULL)
        return;
    freeTree(node->left);
    freeTree(node->right);
    free(node);
}

int main()
{
    int a, b, c, d;
    printf("Enter expr in form a/b+c/d: ");

    scanf("%d/%d+%d/%d", &a, &b, &c, &d);

    Node *root = createNode('+', 0, 0);
    root->left = createNode(0, a, b);
    root->right = createNode(0, c, d);

    printf("Tree structure:\n");
    printTree(root, 0);

    int resultNumerator, resultDenominator;
    calculateTree(root, &resultNumerator, &resultDenominator);
    simplifyFraction(&resultNumerator, &resultDenominator);

    printf("Result: %d/%d\n", resultNumerator, resultDenominator);

    freeTree(root);

    return 0;
}