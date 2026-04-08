// Time spent: 22 mins 23 seconds

#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

class Queue {
private:
    Node* front;
    Node* back;

public:
    Queue() : front(nullptr), back(nullptr) {}

    // returns the first item in the queue. O(1) time.
    int peek() {
        return front->data;
    }

    // adds x to the back of the queue. O(1) time.
    void enqueue(int x) {

        

        Node* newNode = new Node();
        newNode->data = x;
        newNode->next = nullptr;

        if(back->next == nullptr){
            back = newNode;
            front = newNode;
            return;
        }

        back->next = newNode;
        back = newNode;

    }

    // removes and returns the first item in the queue. O(1) time.
    int dequeue() {
        if(front == nullptr) return -1;

        int first = front ->data;
        
        if(front->next == nullptr){
            delete front;
            front = nullptr;
            back = nullptr;
            return first;

        }
        Node* temp = front;
        front = front->next;
        delete temp; 

        return first;
    }

    // returns a boolean indicating whether the queue is empty. O(1) time.
    bool isEmpty() {
        return front == nullptr;
    }
};

int main() {

    return 0;
}
