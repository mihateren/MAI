#include <iostream>
using namespace std;

struct Point
{
    float x;
    float y;
};

Point operator + (Point p1, Point p2){
    Point res;
    res.x = p1.x + p2.x;
    res.y = p1.y + p2.y;
    return res;
}


struct Stack
{
    int length;
    int *data;
    int top;

};

bool isEmptyStack(const Stack &s) {
    return (s.top == -1);
}

void newStack(Stack &s, int l) {
    if (l < 0) throw -1;
    s.length = l;
    s.top = -1;
    if (!l) s.data = NULL;
    else s.data = new int[l];
}

Stack newStack(int l) {
    if (l < 0) throw -1;
    Stack res;
    res.length = l;
    res.top = -1;
    if (!l) res.data = NULL;
    else res.data = new int[l];
    return res;
}

void deleteStack(Stack &s) {
    if (s.length == 0) return;
    s.length = 0;
    delete[] s.data;
    s.data = NULL;
    s.top = -1;
}

Stack copyStack(Stack &sd, Stack ss) {
    if (ss.top < sd.length) {
        for (int i=0; i<=ss.top;++i) {
            sd.data[i] = ss.data[i];
        }
        sd.top = ss.top;
    } else {
        deleteStack(sd);
        sd = newStack(ss.length);
    }
    return sd;
}

void resizeStack(Stack &s) {
    Stack tempS = newStack(s.length + 10);
    copyStack(tempS, s);
    deleteStack(s);
    s = tempS;
}

void pushStack(Stack &s, int e) {
    s.top++;
    if ((s.length == 0) || (s.top == s.length)) resizeStack(s);
    s.data[s.top] = e;
}

int pullStack(Stack &s) {
    if (isEmptyStack(s)) throw -1;
    s.top--;
    return s.data[s.top];
}

int topStack(Stack s) {
    if (isEmptyStack(s)) throw -1;
    return s.data[s.top];
}





int main() {
    Stack myStack = newStack(3);
    pushStack(myStack, 1);
    pushStack(myStack, 2);
    pushStack(myStack, 3);
    cout<<pullStack(myStack);

}
