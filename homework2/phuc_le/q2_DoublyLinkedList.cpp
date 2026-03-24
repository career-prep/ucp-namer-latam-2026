#include <stdlib.h>
#include <iostream>
using namespace std;

struct Node
{
    int data;
    Node *next;
    Node *prev;
    Node(int v) : data(v), next(nullptr), prev(nullptr) {}
};

// creates new Node with data val at front; returns head. O(1) time.
Node *insertAtFront(Node *head, int val)
{
    // Check if no head (no need because if there is no head it is just a nullptr)
    Node *newNode = new Node(val);
    if (head != nullptr)
    {
        head->prev = newNode;
    }
    newNode->next = head;
    return newNode;
}

// creates new Node with data val at end; returns head. O(n) time.
Node *insertAtBack(Node *head, Node *&tail, int val)
{
    // Check if no head
    Node *newNode = new Node(val);
    // Check if the list is empty
    if (head == nullptr)
    {
        tail = newNode;
        return newNode;
    }
    tail->next = newNode;
    newNode->prev = tail;
    tail = newNode;
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
    newNode->prev = loc;
    if (loc->next != nullptr)
    {
        loc->next->prev = newNode;
    }
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
    // curr -> newNode -> loc
    Node *newNode = new Node(val);
    newNode->prev = loc->prev;
    newNode->next = loc;
    loc->prev->next = newNode;
    loc->prev = newNode;

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
    if (head != nullptr)
    {
        head->prev = nullptr;
    }
    delete temp;
    return head;
}

// removes last Node; returns head. O(n) time.
// Find the second to last node and delete the last node
Node *deleteBack(Node *head, Node *&tail)
{
    // Check if the list is empty
    if (head == nullptr)
    {
        return head;
    };
    // List has only 1 node
    if (head == tail)
    {
        return deleteFront(head);
    }
    // Find the node before the last node
    // curr -> deleteNode -> nullptr
    Node *temp = tail;
    tail = tail->prev;
    tail->next = nullptr;
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
        return deleteFront(head);
    }
    // prev -> curr -> next
    loc->prev->next = loc->next;
    if (loc->next != nullptr)
    {
        loc->next->prev = loc->prev;
    }
    delete loc;

    return head;
}

// returns length of the list. O(n) time. Optional can just keep track length while doing insert/deletion. Techincally O(1) ?
int length(Node *head)
{
    int size = 0;
    while (head != nullptr)
    {
        size++;
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
    Node *temp = nullptr;
    Node *curr = head;
    // Swap the prev and next
    while (curr != nullptr)
    {
        temp = curr->prev;
        curr->prev = curr->next;
        curr->next = temp;
        curr = curr->prev;
    }
    // temp now hold the second to last node, so temp->prev is now the head
    if (temp != nullptr)
    {
        head = temp->prev;
    }
    return head;
}

// reverses the linked list recursively (Hint: you will need a helper function.)  O(n) time.
Node *reverseRecursiveHelper(Node *curr)
{
    if (curr == nullptr)
    {
        return nullptr;
    }
    // Swap next and prev node
    Node *temp = curr->prev;
    curr->prev = curr->next;
    curr->next = temp;
    // Reach the end of list (new head)
    if (curr->prev == nullptr)
    {
        return curr;
    }
    return reverseRecursiveHelper(curr->prev);
}

Node *reverseRecursive(Node *head)
{
    // Check if the list is empty
    if (head == nullptr || head->next == nullptr)
    {
        return head;
    }
    return reverseRecursiveHelper(head);
}

// Helper function to keep main() clean
void printList(const string &action, Node *head)
{
    cout << action << ":\n";
    while (head != nullptr)
    {
        cout << head->data << "<->";
        head = head->next;
    }
    cout << "nullptr\n\n";
}

int main()
{
    Node *head = nullptr;
    Node *tail = nullptr;

    cout << "--- 1. Testing Insertions ---\n";

    // Test insertAtBack
    head = insertAtBack(head, tail, 30);
    head = insertAtBack(head, tail, 40);
    head = insertAtBack(head, tail, 50);
    printList("After insertAtBack (30, 40, 50)", head);

    // Test insertAtFront
    head = insertAtFront(head, 20);
    head = insertAtFront(head, 10);
    printList("After insertAtFront (10, 20)", head);

    cout << "--- 2. Testing Search and Mid-List Insertions ---\n";

    // Test findNode & insertAfter
    Node *loc = findNode(head, 30);
    if (loc != nullptr)
    {
        head = insertAfter(head, 35, loc);
    }
    printList("After findNode(30) and insertAfter(35)", head);

    // Test findNode & insertBefore
    loc = findNode(head, 50);
    if (loc != nullptr)
    {
        head = insertBefore(head, 45, loc);
    }
    printList("After findNode(50) and insertBefore(45)", head);

    cout << "--- 3. Testing Deletions ---\n";

    // Test deleteFront
    head = deleteFront(head);
    printList("After deleteFront (removes 10)", head);

    // Test deleteBack
    head = deleteBack(head, tail);
    printList("After deleteBack (removes 50)", head);

    // Test deleteNode (Middle node)
    loc = findNode(head, 35);
    if (loc != nullptr)
    {
        head = deleteNode(head, loc);
    }
    printList("After deleteNode (removes 35)", head);

    cout << "--- 4. Testing List Utility ---\n";

    // Test length
    int size = length(head);
    cout << "Current List Size: " << size << "\n\n";

    cout << "--- 5. Testing Reversals ---\n";

    // Test Iterative Reverse
    head = reverseIterative(head);
    printList("After reverseIterative", head);

    // Test Recursive Reverse
    head = reverseRecursive(head);
    printList("After reverseRecursive (back to original order)", head);

    // Clean up remaining memory before exiting
    while (head != nullptr)
    {
        head = deleteFront(head);
    }

    return 0;
}