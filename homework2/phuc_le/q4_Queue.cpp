#include <stdlib.h>
#include <iostream>
#include <stdexcept>
using namespace std;

struct Node
{
    int data;
    Node *next;
    Node(int v) : data(v), next(nullptr) {}
};

class Queue
{
private:
    Node *head;
    Node *tail;

public:
    //  Initialize in the Queue
    Queue() : head(nullptr), tail(nullptr) {}
    // Clean up memory
    ~Queue()
    {
        while (!isEmpty())
        {
            dequeue();
        }
    }

    int peek()
    {
        // returns the first item in the queue. O(1) time.
        if (isEmpty())
        {
            throw runtime_error("Queue is empty.");
        }
        return head->data;
    }

    // adds x to the back of the queue. O(1) time.
    void enqueue(int x)
    {
        Node *newNode = new Node(x);
        if (isEmpty())
        {
            head = tail = newNode;
            return;
        }
        tail->next = newNode;
        tail = tail->next;
        return;
    }

    // removes and returns the first item in the queue. O(1) time.
    int dequeue()
    {
        if (isEmpty())
        {
            throw runtime_error("Queue is empty.");
        }
        Node *temp = head;
        int dequeueValue = temp->data;
        head = head->next;

        // Edge case, dequeue the tail
        if (head == nullptr)
        {
            tail = nullptr;
        }

        delete temp;
        return dequeueValue;
    }

    bool isEmpty()
    {
        return head == nullptr;
    }
};

int main()
{
    // Initialize the queue
    Queue q;

    cout << "--- 1. Testing Enqueue ---" << endl;
    cout << "Enqueueing 10, 20, 30..." << endl;
    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);

    cout << "\n--- 2. Testing Peek ---" << endl;
    cout << "Front of queue (Peek): " << q.peek() << " (Expected 10)" << endl;

    cout << "\n--- 3. Testing Dequeue ---" << endl;
    cout << "Dequeued: " << q.dequeue() << " (Expected 10)" << endl;
    cout << "Dequeued: " << q.dequeue() << " (Expected 20)" << endl;

    cout << "Front of queue after two dequeues: " << q.peek() << " (Expected 30)" << endl;

    cout << "\n--- 4. Testing Empty States ---" << endl;
    cout << "Is queue empty? " << (q.isEmpty() ? "Yes" : "No") << " (Expected No)" << endl;

    cout << "Dequeued: " << q.dequeue() << " (Expected 30)" << endl;
    cout << "Is queue empty now? " << (q.isEmpty() ? "Yes" : "No") << " (Expected Yes)" << endl;

    cout << "\n--- 5. Testing Re-Enqueue after Empty ---" << endl;
    q.enqueue(99);
    cout << "Enqueued 99. Peek: " << q.peek() << " (Expected 99)" << endl;

    return 0;
}