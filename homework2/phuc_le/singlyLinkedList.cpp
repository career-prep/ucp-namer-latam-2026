#include <stdlib.h>
#include <iostream>
using namespace std;

struct Node
{
    int data;
    Node *next;
    Node(int v) : data(v), next(nullptr) {}
};

// creates new Node with data val at front; returns head. O(1) time.
Node *insertAtFront(Node *head, int val)
{
    // Check if no head (no need because if there is no head it is just a nullptr)
    Node *newNode = new Node(val);
    newNode->next = head;
    return newNode;
}

// creates new Node with data val at end; returns head. O(n) time.
Node *insertAtBack(Node *head, int val)
{
    // Check if no head
    Node *newNode = new Node(val);
    // Check if the list is empty
    if (head == nullptr)
    {
        return newNode;
    }
    Node *temp = head;
    // Find the tail
    while (temp->next != nullptr)
    {
        temp = temp->next;
    }
    temp->next = newNode;
    return head;
}

// find node helper (O(n) time complexity)
Node *findNode(Node *head, int target)
{
    Node *curr = head;
    while (curr != nullptr)
    {
        if (curr->data == target)
        {
            return curr;
        }
        curr = curr->next;
    }
    // if no target Node in linkedlist
    return nullptr;
}

// creates new Node with data val after Node loc; returns head. O(1) time (If only located the node beforehand, else O(n)).
Node *insertAfter(Node *head, int val, Node *loc)
{
    // Check if list is not empty
    if (head == nullptr)
    {
        return head;
    }
    // loc -> newNode -> loc->next
    Node *newNode = new Node(val);
    newNode->next = loc->next;
    loc->next = newNode;
    return head;
}

// creates new Node with data val before Node loc; returns head. O(n) time.
Node *insertBefore(Node *head, int val, Node *loc)
{
    // Check if the list is empty and loc node not in list
    if (head == nullptr)
    {
        return head;
    }
    // loc node is head
    if (loc == head)
    {
        return insertAtFront(head, val);
    }
    // Find the node before loc node
    Node *curr = head;
    while (curr != nullptr && curr->next != loc)
    {
        curr = curr->next;
    }
    // curr -> newNode -> loc
    Node *newNode = new Node(val);
    newNode->next = loc;
    curr->next = newNode;
    return head;
}

// removes first Node; returns head. O(1) time.
Node *deleteFront(Node *head)
{
    // Check if the list is empty
    if (head == nullptr)
    {
        return head;
    };
    Node *temp = head;
    head = head->next;
    delete temp;
    return head;
}

// removes last Node; returns head. O(n) time.
// Find the second to last node and delete the last node
Node *deleteBack(Node *head)
{
    // Check if the list is empty
    if (head == nullptr)
    {
        return head;
    };
    // List has only 1 node
    if (head->next == nullptr)
    {
        delete head;
        return nullptr;
    }
    // Find the node before the last node
    Node *curr = head;
    while (curr->next->next != nullptr)
    {
        curr = curr->next;
    }
    // curr -> deleteNode -> nullptr
    Node *temp = curr->next;
    curr->next = nullptr;
    delete temp;
    return head;
}

// deletes Node loc; returns head. O(1) time. Technically still O(n) because we still need to find the node before the loc node
Node *deleteNode(Node *head, Node *loc)
{
    // Check if the list is empty
    if (head == nullptr)
    {
        return head;
    }
    // If head is loc
    if (loc == head)
    {
        Node *temp = head;
        head = head->next;
        delete temp;
        return head;
    }
    // Find the node before loc
    Node *curr = head;
    while (curr != nullptr && curr->next != loc)
    {
        curr = curr->next;
    }
    Node *temp = curr->next;
    curr->next = curr->next->next;
    delete temp;
    return head;
}

// returns length of the list. O(n) time. Optional can just keep track length while doing insert/deletion. Techincally O(1) ?
int lenght(Node *head)
{
    int size = 0;
    while (head != nullptr)
    {
        size += 1;
        head = head->next;
    }
    return size;
}

// reverses the linked list iteratively. O(n) time.
Node *reverseIterative(Node *head)
{
    // Check if the list is empty
    if (head == nullptr || head->next == nullptr)
    {
        return head;
    }
    // 2 pointers, one is prev and one is curr
    // prev <- curr <- next pointer
    Node *prev = nullptr;
    Node *curr = head;
    while (curr != nullptr)
    {
        Node *nxt = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nxt;
    }
    return prev;
}

// reverses the linked list recursively (Hint: you will need a helper function.)  O(n) time.
Node *reverseRecursive(Node *head)
{
    // Check if the list is empty
    if (head == nullptr || head->next == nullptr)
    {
        return head;
    }
    Node *reverseHead = reverseRecursive(head->next);
    head->next->next = head;
    head->next = nullptr;
    return reverseHead;
}

int main()
{
    Node *head = nullptr;
    head = insertAtBack(head, 10);
    head = insertAtBack(head, 20);
    head = insertAtBack(head, 30);
    head = insertAtBack(head, 40);

    Node *temp = head;
    cout << "Linked List: ";
    while (temp != nullptr)
    {
        cout << temp->data << "->";
        temp = temp->next;
    }
    cout << "nullptr" << endl;

    Node *loc = findNode(head, 10);
    if (loc != nullptr)
    {
        head = insertBefore(head, 90, loc);
    }

    temp = head;
    cout << "Linked List after added: ";
    while (temp != nullptr)
    {
        cout << temp->data << "->";
        temp = temp->next;
    }
    cout << "nullptr" << endl;

    if (loc != nullptr)
    {
        head = deleteNode(head, loc);
    }
    temp = head;
    cout << "Linked List after deleted: ";
    while (temp != nullptr)
    {
        cout << temp->data << "->";
        temp = temp->next;
    }
    cout << "nullptr" << endl;

    head = reverseIterative(head);
    temp = head;
    cout << "Linked List after reversed: ";
    while (temp != nullptr)
    {
        cout << temp->data << "->";
        temp = temp->next;
    }
    cout << "nullptr" << endl;

    int size = lenght(head);
    cout << "Size: " << size << endl;

    head = reverseRecursive(head);
    temp = head;
    cout << "Linked List after reversed: ";
    while (temp != nullptr)
    {
        cout << temp->data << "->";
        temp = temp->next;
    }
    cout << "nullptr" << endl;
    return 0;
}