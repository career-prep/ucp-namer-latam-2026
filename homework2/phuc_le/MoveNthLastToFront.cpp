#include <iostream>
#include <vector>
using namespace std;

struct Node
{
    int data;
    Node *next;
    Node(int v) : data(v), next(nullptr) {}
};

/*
    Edge case: Empty linkedlistt, 1 node linkedlist, invalid k
    Given a singly linked list, move the nth from the last element to the front of the list.
    Use fast and slow pointer for to fix the window size of k
    Make the slow node (kth node) the new head node
    Return the new head

    Time Complexity: O(n) - n is the number of nodes.
    Space Complexity: O(1) - use no extra memory

    Time: 40 mins
*/
Node *MoveNthLastToFront(Node *head, int k)
{
    // Edge case: empty list or single-element list or invalid input k
    if (head == nullptr || head->next == nullptr || k <= 0)
    {
        return head;
    }
    // [slow, fast] window to find the kth node from the end
    Node *slow, *fast, *prev;
    slow = fast = head;
    // The node before the kth node
    prev = nullptr;
    // Move the fast pointer by k step
    for (int i = 0; i < k; i++)
    {
        // If k > linkedlist length, return unchanged linkedlist
        if (fast == nullptr)
        {
            return head;
        }
        // Premove the fast node
        fast = fast->next;
    }
    // If fast == nullptr -> kth node from the end is the head node, no change is made
    if (fast == nullptr)
    {
        return head;
    }
    // Tranverse the remaining elements of the linked list
    while (fast != nullptr)
    {
        prev = slow;
        slow = slow->next;
        fast = fast->next;
    }
    // After this step, slow node should be our needed kth node
    // Move the prev pointer to skip the kth node
    prev->next = slow->next;
    // Make the kth node point to the head node
    slow->next = head;
    // kth node is now the new head
    head = slow;
    // Return the new Head
    return head;
}

// Helper to create a linked list from a vector of integers
Node *CreateList(const vector<int> &vals)
{
    if (vals.empty())
        return nullptr;
    Node *head = new Node(vals[0]);
    Node *current = head;
    for (size_t i = 1; i < vals.size(); ++i)
    {
        current->next = new Node(vals[i]);
        current = current->next;
    }
    return head;
}

// Helper to print the linked list
void PrintList(Node *head)
{
    if (!head)
    {
        cout << "null" << endl;
        return;
    }
    Node *temp = head;
    while (temp != nullptr)
    {
        cout << temp->data;
        if (temp->next != nullptr)
            cout << " -> ";
        temp = temp->next;
    }
    cout << endl;
}

// Helper to free allocated memory
void FreeList(Node *head)
{
    Node *temp;
    while (head != nullptr)
    {
        temp = head;
        head = head->next;
        delete temp;
    }
}

int main()
{
    // Test Case 1: (k = 2)
    cout << "Test Case 1: k = 2" << endl;
    Node *head1 = CreateList({15, 2, 8, 7, 20, 9, 11, 6, 19});
    cout << "Input:  ";
    PrintList(head1);
    head1 = MoveNthLastToFront(head1, 2);
    cout << "Output: ";
    PrintList(head1);
    cout << "-----------------------" << endl;

    // Test Case 2: (k = 7)
    cout << "Test Case 2: k = 7" << endl;
    Node *head2 = CreateList({15, 2, 8, 7, 20, 9, 11, 6, 19});
    cout << "Input:  ";
    PrintList(head2);
    head2 = MoveNthLastToFront(head2, 7);
    cout << "Output: ";
    PrintList(head2);
    cout << "-----------------------" << endl;

    // Test Case 3: Edge Case (k = 1, Move the very last element)
    cout << "Test Case 3: k = 1 (Move last element)" << endl;
    Node *head3 = CreateList({1, 2, 3, 4, 5});
    cout << "Input:  ";
    PrintList(head3);
    head3 = MoveNthLastToFront(head3, 1);
    cout << "Output: ";
    PrintList(head3);
    cout << "-----------------------" << endl;

    // Test Case 4: Edge Case (k == length of list)
    // If k equals the length of the list, the nth-from-last node is already the head. The list should remain unchanged.
    cout << "Test Case 4: k = 5 (Length of list)" << endl;
    Node *head4 = CreateList({1, 2, 3, 4, 5});
    cout << "Input:  ";
    PrintList(head4);
    head4 = MoveNthLastToFront(head4, 5);
    cout << "Output: ";
    PrintList(head4);
    cout << "-----------------------" << endl;

    // Test Case 5: Error Case (k > length of list)
    // The function handles this by returning the list unchanged.
    cout << "Test Case 5: k = 10 (Out of bounds)" << endl;
    Node *head5 = CreateList({1, 2, 3});
    cout << "Input:  ";
    PrintList(head5);
    head5 = MoveNthLastToFront(head5, 10);
    cout << "Output: ";
    PrintList(head5);
    cout << "-----------------------" << endl;

    // Free allocated memory
    FreeList(head1);
    FreeList(head2);
    FreeList(head3);
    FreeList(head4);
    FreeList(head5);

    return 0;
}