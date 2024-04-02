#include <iostream>
using namespace std;

struct NodeBST {
    int data;
    NodeBST* left = nullptr;
    NodeBST* right = nullptr;
};

void addNodeBST(NodeBST*& node, int value) {
    if (node == nullptr) {
        node = new NodeBST();
        node->data = value;
        node->left = nullptr;
        node->right = nullptr;
    } else if (value <= node->data) {
        addNodeBST(node->left, value);
    } else if (value > node->data) {
        addNodeBST(node->right, value);
    }
}

NodeBST* findMinNode(NodeBST* node);

void deleteNodeBST(NodeBST*& node, int value) {
    if (node == nullptr) {
        return;
    }
    if (value < node->data) {
        deleteNodeBST(node->left, value);
    } else if (value > node->data) {
        deleteNodeBST(node->right, value);
    } else {
        if (node->left == nullptr && node->right == nullptr) {
            // нету потомков
            delete node;
            node = nullptr;
        } else if (node->left == nullptr) {
            // есть только правый потомок
            NodeBST* temp = node;
            node = node->right;
            delete temp;
        } else if (node->right == nullptr) {
            // есть только левый потомок
            NodeBST* temp = node;
            node = node->left;
            delete temp;
        } else {
            // есть 2 потомка
            NodeBST* temp = findMinNode(node->right);
            node->data = temp->data;
            deleteNodeBST(node->right, temp->data);
        }
    }
}

NodeBST* findMinNode(NodeBST* node) {
    while (node->left != nullptr) {
        node = node->left;
    }
    return node;
}

void printTree(NodeBST* node, int space = 0, int indent = 5) {
    if (node == nullptr) return;

    space += indent;

    printTree(node->right, space);

    cout << endl;
    for (int i = indent; i < space; i++) {
        cout << " ";
    }
    cout << node->data;

    printTree(node->left, space);
}

int countNodes(NodeBST* node) {
    if (node == nullptr)
        return 0;
    else
        return countNodes(node->left) + countNodes(node->right) + 1;
}

void clearMemory(NodeBST*& node) {
    if (node == nullptr) return;
    clearMemory(node->left);
    clearMemory(node->right);
    delete node;
    node = nullptr;
}

int main() {
    NodeBST* root = nullptr;
    int arr[8] = {17, 10, 21, 3, 15, 19, 25, 17};
    for (int i = 0; i < 8; i++) {
        addNodeBST(root, arr[i]);
    }
    cout << "Print tree before deletion: " << endl;
    printTree(root);
    cout<<endl;

    // удаление узла
    int valueToDelete = 17;
    deleteNodeBST(root, valueToDelete);

    cout << "Print tree after deletion of " << valueToDelete << ": " << endl;
    printTree(root);
    cout<<endl;
    cout << "Count nodes: " << countNodes(root) << endl;

    clearMemory(root);
    return 0;
}
