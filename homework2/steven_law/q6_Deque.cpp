// Time spent: 24 mins 7 seconds

#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node* prev;
};

class Deque {
private:
    Node* head;
    Node* tail;

public:
    Deque() : head(nullptr), tail(nullptr) {}
    // returns the first item in the deque. O(1) time.
    int front() {
        if(head == nullptr) return -1;
        return head->data;
    }

    // returns the last item in the deque. O(1) time.
    int back() {
        if(tail == nullptr) return -1;
        return tail->data;
    }

    // adds x to the back of the deque. O(1) time.
    void pushBack(int x) {
        if(head == nullptr){
            Node* newNode = new Node();
            newNode->data = x;
            newNode->next = nullptr;
            newNode->prev = nullptr;
            head = newNode;
            tail = newNode;
            return;
        }

        Node* newNode = new Node();
        newNode ->data = x;
        newNode->next = nullptr;
        newNode->prev = tail;

        tail->next = newNode;
        tail = newNode;
        return;
    }

    // adds x to the front of the deque. O(1) time.
    void pushFront(int x) {
        if(head == nullptr){
            Node* newNode = new Node();
            newNode->data = x;
            newNode->next = nullptr;
            newNode->prev = nullptr;
            head = newNode;
            tail = newNode;
            return;
        }

        Node* newNode = new Node();
        newNode ->data = x;
        newNode->next = head;
        newNode->prev = nullptr;

        head->prev = newNode;
        head = newNode;
        return;

    }

    // removes and returns the first item in the deque. O(1) time.
    int popFront() {
        if(head == nullptr) return -1;

        int val = head->data;
        Node* temp = head;

        head = head->next;
        if (head == nullptr) {
            tail = nullptr;
        } else{
            head->prev = nullptr;
        }
        
        delete temp;
        return val;
    }

    // removes and returns the last item in the deque. O(1) time.
    int popBack() {
        if(tail == nullptr) return -1;
        int val = tail -> data; 

        Node* temp = tail;
        tail = tail->prev;

        if(tail == nullptr){
            head = nullptr;
        }

        else{
                tail->next = nullptr;
        }
        

        delete temp;
        return val;

    }

    // returns a boolean indicating whether the deque is empty. O(1) time.
    bool isEmpty() {
        return head == nullptr;

    }
};

int main() {

    return 0;
}
