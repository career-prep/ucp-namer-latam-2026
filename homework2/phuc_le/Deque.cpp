#include <stdio.h>
#include <stdexcept>
#include <iostream>
using namespace std;

// Must use Doubly Linked List Node to achieve O(1) popBack
struct Node
{
    int data;
    Node *next;
    Node *prev;
    Node(int v) : data(v), next(nullptr), prev(nullptr) {}
};

class Deque
{
private:
    Node *head;
    Node *tail;

public:
    Deque() : head(nullptr), tail(nullptr) {}
    ~Deque()
    {
        if (!isEmpty())
        {
            popFront();
        }
    }

    // returns the first item in the deque. O(1) time
    int front()
    {
        if (isEmpty())
        {
            throw runtime_error("Stack is empty.");
        }
        return head->data;
    }
    // returns the last item in the deque. O(1) time.
    int back()
    {
        if (isEmpty())
        {
            throw runtime_error("Stack is empty.");
        }
        return tail->data;
    }
    // adds x to the back of the deque. O(1) time.
    void pushBack(int x)
    {
        Node *newNode = new Node(x);
        if (isEmpty())
        {
            head = tail = newNode;
            return;
        }
        tail->next = newNode;
        newNode->prev = tail;
        tail = newNode;
    }
    // adds x to the front of the deque. O(1) time
    void pushFront(int x)
    {
        Node *newNode = new Node(x);
        if (isEmpty())
        {
            head = tail = newNode;
            return;
        }
        newNode->next = head;
        head->prev = newNode;
        head = newNode;
    }
    // removes and returns the first item in the deque. O(1) time.
    int popFront()
    {
        if (isEmpty())
        {
            throw runtime_error("Stack is empty.");
        }
        Node *temp = head;
        int popValue = temp->data;

        head = head->next;
        if (head != nullptr)
        {
            head->prev = nullptr;
        }
        else
        {
            // Empty linked list
            tail = nullptr;
        }
        delete temp;
        return popValue;
    }
    // removes and returns the last item in the deque. O(1) time.
    int popBack()
    {
        if (isEmpty())
        {
            throw runtime_error("Stack is empty.");
        }
        Node *temp = tail;
        int popValue = temp->data;

        tail = tail->prev;
        if (tail != nullptr)
        {
            tail->next = nullptr;
        }
        else
        {
            // Empty linkedlist
            head = nullptr;
        }
        delete temp;
        return popValue;
    }
    // returns a boolean indicating whether the deque is empty. O(1) time.
    bool isEmpty()
    {
        return head == nullptr;
    }
};

int main()
{
    Deque dq;

    cout << "--- Testing pushBack and pushFront ---" << endl;
    dq.pushBack(20);
    dq.pushBack(30);
    dq.pushFront(10);

    cout << "Front: " << dq.front() << " (Expected 10)" << endl;
    cout << "Back: " << dq.back() << " (Expected 30)" << endl;

    cout << "\n--- Testing popBack ---" << endl;
    cout << "Popped Back: " << dq.popBack() << " (Expected 30)" << endl;
    cout << "New Back: " << dq.back() << " (Expected 20)" << endl;

    cout << "\n--- Testing popFront ---" << endl;
    cout << "Popped Front: " << dq.popFront() << " (Expected 10)" << endl;
    cout << "New Front: " << dq.front() << " (Expected 20)" << endl;

    cout << "\n--- Testing Emptying Deque ---" << endl;
    cout << "Popped Front: " << dq.popFront() << " (Expected 20)" << endl;
    cout << "Is Empty? " << (dq.isEmpty() ? "Yes" : "No") << " (Expected Yes)" << endl;

    return 0;
}