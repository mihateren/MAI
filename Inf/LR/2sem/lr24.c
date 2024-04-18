#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int value;
    struct Node *left;
    struct Node *right;
} Node;

Node *createNode(int value) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->value = value;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

void calculateTree(Node *node, int *resultNumerator, int *resultDenominator) {
    if (node->left == NULL && node->right == NULL) {
        *resultNumerator = node->value;
        *resultDenominator = 1;
    } else {
        int leftNumerator, leftDenominator, rightNumerator, rightDenominator;
        calculateTree(node->left, &leftNumerator, &leftDenominator);
        calculateTree(node->right, &rightNumerator, &rightDenominator);

        switch (node->value) {
            case '+':
                *resultNumerator = leftNumerator * rightDenominator + rightNumerator * leftDenominator;
                *resultDenominator = leftDenominator * rightDenominator;
                break;
            case '/':
                *resultNumerator = leftNumerator * rightDenominator;
                *resultDenominator = leftDenominator * rightNumerator;
                break;
            default:
                printf("Unsupported operation: %c\n", node->value);
                exit(1);
        }
    }
}

void simplifyFraction(int *numerator, int *denominator) {
    int a = abs(*numerator);
    int b = abs(*denominator);
    while (b) {
        int temp = a % b;
        a = b;
        b = temp;
    }
    *numerator /= a;
    *denominator /= a;
}

void printTree(Node *node, int level) {
    if (node == NULL)
        return;

    printTree(node->right, level + 1);

    for (int i = 0; i < level; i++) {
        printf("             ");
    }
    if (node->left == NULL && node->right == NULL) {
        printf("%d\n", node->value);
    } else if (level != 0) {
        printf("%d%c%d\n", (int)node->left->value,node->value,(int)node->right->value);
    } else {
        printf("%d/%d%c%d/%d\n", (int)node->left->left->value, (int)node->left->right->value,node->value,(int)node->right->left->value, (int)node->right->right->value);
    }

    printTree(node->left, level + 1);
}

void freeTree(Node *node) {
    if (node == NULL)
        return;
    freeTree(node->left);
    freeTree(node->right);
    free(node);
}

int main() {
    int a, b, c, d;
    printf("Enter expr in form a/b+c/d: ");
    scanf("%d/%d+%d/%d", &a, &b, &c, &d);

    Node *root = createNode('+');
    root->left = createNode('/');
    root->right = createNode('/');
    root->left->left = createNode(a);
    root->left->right = createNode(b);
    root->right->left = createNode(c);
    root->right->right = createNode(d);

    printf("Tree structure:\n");
    printTree(root, 0);

    int resultNumerator, resultDenominator;
    calculateTree(root, &resultNumerator, &resultDenominator);
    simplifyFraction(&resultNumerator, &resultDenominator);

    printf("Result: %d/%d\n", resultNumerator, resultDenominator);

    freeTree(root);

    return 0;
}