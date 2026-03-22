#include <stdio.h>
#include <stdexcept>
#include <iostream>
using namespace std;

struct Node
{
    int data;
    Node *next;
    Node(int v) : data(v), next(nullptr) {}
};

class Stack
{
public:
    Node *head = nullptr;

public:
    // Initialize the Stack
    Stack() : head(nullptr) {}
    ~Stack()
    {
        while (!isEmpty())
        {
            pop();
        }
    }

    // returns the top item in the stack. O(1) time.
    int top()
    {
        if (isEmpty())
        {
            throw runtime_error("Stack is empty.");
        }
        return head->data;
    }

    // adds x to the top of the stack. O(1) time.
    void push(int x)
    {
        Node *newNode = new Node(x);
        newNode->next = head;
        head = newNode;
    }

    // removes and returns the top item in the stack. O(1) time.
    int pop()
    {
        if (isEmpty())
        {
            throw runtime_error("Stack is empty.");
        }
        Node *temp = head;
        int popValue = temp->data;
        head = head->next;
        delete temp;
        return popValue;
    }

    bool isEmpty()
    {
        return head == nullptr;
    }
};

int main()
{
    Stack s;

    cout << "--- 1. Testing Push ---" << endl;
    cout << "Pushing 10, 20, 30..." << endl;
    s.push(10);
    s.push(20);
    s.push(30);

    cout << "\n--- 2. Testing Top ---" << endl;
    cout << "Top of stack: " << s.top() << " (Expected 30)" << endl;

    cout << "\n--- 3. Testing Pop ---" << endl;
    cout << "Popped: " << s.pop() << " (Expected 30)" << endl;
    cout << "Popped: " << s.pop() << " (Expected 20)" << endl;

    cout << "Top of stack after two pops: " << s.top() << " (Expected 10)" << endl;

    cout << "\n--- 4. Testing Empty States ---" << endl;
    cout << "Is stack empty? " << (s.isEmpty() ? "Yes" : "No") << " (Expected No)" << endl;

    cout << "Popped: " << s.pop() << " (Expected 10)" << endl;
    cout << "Is stack empty now? " << (s.isEmpty() ? "Yes" : "No") << " (Expected Yes)" << endl;

    cout << "\n--- 5. Testing Re-Push after Empty ---" << endl;
    s.push(99);
    cout << "Pushed 99. Top: " << s.top() << " (Expected 99)" << endl;

    return 0;
}