#include <iostream>
using namespace std;

struct Node {
    int data;
    Node * next;
};

void push(Node* head, int x) {
    Node* current = head;
    while (current->next != NULL) {
        current = current->next;
    }
    Node* temp = new Node;
    current->next = temp;
    temp->data = x;
    temp->next = NULL;
}

void pop(Node* head) {
    Node* current = head;
    while (current->next != NULL) {
        current = current->next;    
    }
    cout<<current->data;
    Node* preLast = head;
    while (preLast->next != current){
        preLast = preLast->next;
    }
    preLast->next = NULL;
    delete current;
}

int main() {
    Node* head1 = new Node;
    head1->data = 0;
    head1->next = NULL;

    // создаем список head1
    Node* ptn = head1;
    int n;
    cin >> n;
    for (int i = 1; i < n; i++) {
        ptn->next = new Node;
        ptn = ptn->next;  // Переходим к новому узлу
        ptn->data = i * i;
        ptn->next = NULL;
    }

    // создаем список head2
    Node* head2 = NULL;
    Node* temp = NULL;
    head2 = new Node;
    head2->data = 0;
    head2->next = NULL;

    for (int i = 1; i < n; i++) {
        temp = new Node;
        temp->data = i * i;
        temp->next = head2;
        head2 = temp;
    }

    push(head2, -100);
    pop(head2);
    // Вывод значений списка head1
    // cout<<"first list"<<endl;
    // Node* current = head1;
    // while (current != NULL) {
    //     cout << current->data << endl;
    //     current = current->next;
    // }
    // // Вывод значений списка head2
    // cout<<"second list"<<endl;
    // current = head2;
    // while (current != NULL) {
    //     cout << current->data << endl;
    //     current = current->next;
    // }

    // Очистка памяти
    while (head1 != NULL) {
        ptn = head1->next;
        delete head1;
        head1 = ptn;
    }

    while (head2 != NULL) {
        temp = head2->next;
        delete head2;
        head2 = temp;
    }

    return 0;
}
