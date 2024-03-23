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
};

void Node::initNode(int d, Node* next) {
    data = d;
    this->next = next;
}

void Node::deleteNode() {
    data = 0;
    next = NULL;
}

int main() {
    Node * ptn = new Node(7);
    delete ptn;
}