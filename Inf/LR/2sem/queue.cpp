#include <iostream>
using namespace std;

struct Queue {
    int length;
    int* data;
    int start;
    int depth;
};


void copyQueue(Queue & qd, const Queue & qs);

bool isEmptyQueue(const Queue & q) {
    return (q.depth == 0);
}

Queue newQueue(int len) {
    if (len < 0) throw - 1;
    Queue q;
    q.length = len;
    q.data = NULL;
    if (len > 0) q.data = new int [len];
    q.start = 0;
    q.depth = 0;
    return q;
}

void deleteQueue(Queue & q) {
    if (q.length != 0) delete [] q.data;
    q.data = NULL;
    q.depth = 0;
    q.start = 0;
    q.length = 0;
}

void resizeQueue(Queue & q, int dl = 10) {
    Queue nq = newQueue(q.length + dl);
    copyQueue(nq, q);
    deleteQueue(q);
    q = nq;
}

void pushQueue(Queue & q, int k) {
    if (q.length == q.depth) resizeQueue(q);
    q.data[(q.start + q.depth) % q.length] = k;
    q.depth++;
}

int topQueue(const Queue & q) {
    if (q.depth == 0) throw -2;
    return q.data[q.start];
}

int pullQueue(Queue & q) {
    if (isEmptyQueue(q)) throw -3;
    int k = q.data[q.start];
    q.depth--;
    q.start = (q.start + 1) % q.length; 
    return k;
}

void copyQueue(Queue & qd, const Queue & qs) {
    if (qd.length < qs.length) resizeQueue(qd, qs.length - qd.length);
    for (int i = 0; i < qs.depth; i++) {
        qd.data[i] = qs.data[(qs.start + i) % qs.length];
        qd.start = 0;
        qd.depth = qs.depth;
    }
}

int main() {
    int Qlen = 5;
    Queue myQueue = newQueue(Qlen);
    for (int i = 0; i < Qlen; i++) {
        pushQueue(myQueue, i+1);
    };
    cout<<topQueue(myQueue);
    return 0;
}