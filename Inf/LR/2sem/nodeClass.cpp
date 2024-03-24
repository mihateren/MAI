#include <iostream>
using namespace std;

class Node{
    Node* next;
    void initNode(int d, Node* next = NULL);
    void deleteNode();

    public:
        int data;
        void printNode(){
            cout<<this<<" ";
            cout<<data<<" ";
            cout<<next<<endl;
        }
        
        Node() {
            cout<<"default constructor \n";
            initNode(0);
            printNode();
        }
        Node(int d) {
            cout<<"parametric constructor \n";
            initNode(d);
            printNode();
        }
        Node(Node &n){
            cout<<"copy constructor \n";
            initNode(n.data);
            printNode();
        }
        ~Node(){
            deleteNode();
            cout<<"destructor \n";
            cout<<this<<endl;
        }

        friend class List;
};

void Node::initNode(int d, Node* next) {
    data = d;
    this->next = next;
}

void Node::deleteNode() {
    data = 0;
    next = NULL;
}

class List {
    Node* head;

public:
    List() {
        cout << "Default constructor for List" << endl;
        head = NULL;
    }

    List(int data) {
        cout << "Parametric constructor for List" << endl;
        head = new Node(data);
    }

    List(const List& otherList) {
        cout << "Copy constructor for List" << endl;
        if (otherList.head == NULL) {
            head = NULL;
        } 
        else {
            head = new Node(*otherList.head);
            Node* curr = head;
            Node* temp = otherList.head->next;
            while (temp != NULL) {
                curr->next = new Node(*temp);
                curr = curr->next;
                temp = temp->next;
            }
        }
    }

    ~List() {
        Node* current = head;
        Node* next = NULL;
        while (current) {
            next = current->next;
            delete current;
            current = next;
        }
        head = NULL;
        cout << "List destructor \n";
    }

    void addToEnd(int data) {
        if (!head) {
            head = new Node(data);
        } else {
            Node* current = head;
            while (current->next) {
                current = current->next;
            }
            current->next = new Node(data);
        }
    }

    void addToStart(int data) {
        Node* newNode = new Node(data);
        newNode->next = head;
        head = newNode;
    }

    bool findNode(int data) {
        Node* current = head;
        while (current) {
            if (current->data == data) {
                return true;
            }
            current = current->next;
        }
        return false;
    }

    Node* findNextNode(Node* current) {
        if (current && current->next) {
            return current->next;
        }
        return NULL;
    }

    Node* findPrevNode(Node* current) {
        Node* prev = head;
        while (prev && prev->next != current) {
            prev = prev->next;
        }
        return prev;
    }

    void deleteNode(int data) {
        Node* current = head;
        Node* prev = NULL;

        while (current) {
            if (current->data == data) {
                if (prev) {
                    prev->next = current->next;
                } else {
                    head = current->next;
                }
                delete current;
                break;
            }
            prev = current;
            current = current->next;
        }
    }

    void printList() {
        Node* current = head;
        while (current) {
            cout << current->data << " ";
            current = current->next;
        }
        cout << endl;
    }

    friend void swap(List& first, List& second) {
        Node* temp = first.head;
        first.head = second.head;
        second.head = temp;
        cout << "Swapped two lists \n";
    }
};

int main() {
    List list1;
    list1.addToEnd(10);
    list1.addToEnd(20);
    list1.addToEnd(30);

    cout << "List 1: ";
    list1.printList();

    List list2(list1);
    list2.addToStart(5);

    cout << "List 2: ";
    list2.printList();

    if (list1.findNode(20)) cout<<"20 was found"<<endl;
    else cout<<"20 was not found"<<endl;

    cout << "Deleting node 10 from List 2: ";
    list2.deleteNode(10);

    cout << "List 2 after deletion: ";
    list2.printList();

    swap(list1, list2);

    cout << "List 1 after swap: ";
    list1.printList();

    cout << "List 2 after swap: ";
    list2.printList();

    return 0;
}