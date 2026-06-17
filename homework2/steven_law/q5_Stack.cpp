// Time spent: 20 mins 51 seconds

#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

class Stack {
private:
    Node* head;

public:
    Stack() : head(nullptr) {}
    // returns the top item in the stack. O(1) time.
    int top() {
        if(head == nullptr) return -1;
        return head ->data;
    }

    // adds x to the top of the stack. O(1) time.
    void push(int x) {
        Node* newNode = new Node();
        newNode->data = x;
        newNode->next = head;
        head = newNode;
         
    }

    // removes and returns the top item in the stack. O(1) time.
    int pop() {
        if(head ==nullptr) return -1;

        int val = head->data;

        Node* temp = head;
        head = head->next; 
        delete temp;

        return val;

    }

    // returns a boolean indicating whether the stack is empty. O(1) time.
    bool isEmpty() {
        if(head == nullptr) return true;
        return false;
    }
};

int main() {

    return 0;
}
