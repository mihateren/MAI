#include <iostream>
using namespace std;

struct Tree {
    int data[156] = {-1};
    int parents[156] = {-1};
};

void addNode(int value, Tree* tree, int parent = 0) {
    if (tree->data[parent] == -1) {
        tree->data[parent] = value;
    } else {
        bool added = false;
        int indexMinValue = 0;
        int minValue = tree->data[parent + 1];
        for (int i = parent + 1; i < parent + 6; i++) {
            if (i > 156) {
                break;
            }
            if (tree->data[i] > minValue) {
                minValue = tree->data[i];
                indexMinValue = i;
            }
            if (tree->data[i] == -1) {
                tree->data[i] = value;
                tree->parents[i] = parent;
                added = true;
                break;
            }
        }
        if (!added) {
            addNode(value, tree, indexMinValue);
        }
    }
}

void printTree(Tree* tree, int node = 0, int level = 0) {
    if (tree->data[node] == -1) {
        return;
    }

    for (int i = 0; i < level; ++i) {
        cout << "  ";
    }
    cout << tree->data[node] << endl;

    for (int i = 1; i <= 5; ++i) {
        int child = node * 5 + i;
        if (child < 156 && tree->data[child] != -1) {
            printTree(tree, child, level + 1);
        }
    }
}

int main() {
    Tree* myTree = new Tree;
    for (int i = 0; i < 20; i++) {
        addNode(i, myTree);
    }
    printTree(myTree);
    delete myTree; // Освобождаем память
    return 0;
}