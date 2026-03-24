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
    Given a sorted singly linked list, remove any duplicates so that no value appears more than once.
    Maintain pointers at the current node and next node
    If find duplicate, move the curr next pointer to the next-next-node
    Only move the curr pointer when there is no duplicate.

    Time Complexity: O(n) - n is the number of nodes.
    Space Complexity: O(1) - use no extra memory

    Time: 35 mins
*/
Node *DedupSortedList(Node *head)
{
    // Edge case: empty list or single-element list
    if (head == nullptr || head->next == nullptr)
    {
        return head;
    }
    Node *curr = head;
    // Traverse the list to find duplicated.
    while (curr != nullptr && curr->next != nullptr)
    {
        // If a duplicate is found
        if (curr->data == curr->next->data)
        {
            // Identify the duplicate node
            Node *dupNode = curr->next;
            // Skip the dup node
            curr->next = curr->next->next;
            // Delete it
            delete dupNode;
        }
        else
        {
            // Move curr pointer if no duplicate was found
            curr = curr->next;
        }
    }
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
    // Test Case 1: Duplicate in sorted list
    cout << "Test Case 1: Image Example" << endl;
    Node *head1 = CreateList({1, 2, 2, 4, 5, 5, 5, 10, 10});
    cout << "Input:  ";
    PrintList(head1);
    head1 = DedupSortedList(head1);
    cout << "Output: ";
    PrintList(head1);
    cout << "-----------------------" << endl;

    // Test Case 2: No duplicates
    cout << "Test Case 2: No Duplicates" << endl;
    Node *head2 = CreateList({1, 2, 3, 4, 5});
    cout << "Input:  ";
    PrintList(head2);
    head2 = DedupSortedList(head2);
    cout << "Output: ";
    PrintList(head2);
    cout << "-----------------------" << endl;

    // Test Case 3: All duplicates
    cout << "Test Case 3: All Duplicates" << endl;
    Node *head3 = CreateList({7, 7, 7, 7});
    cout << "Input:  ";
    PrintList(head3);
    head3 = DedupSortedList(head3);
    cout << "Output: ";
    PrintList(head3);
    cout << "-----------------------" << endl;

    // Test Case 4: Empty list
    cout << "Test Case 4: Empty List" << endl;
    Node *head4 = nullptr;
    cout << "Input:  ";
    PrintList(head4);
    head4 = DedupSortedList(head4);
    cout << "Output: ";
    PrintList(head4);
    cout << "-----------------------" << endl;

    // Free allocated memory
    FreeList(head1);
    FreeList(head2);
    FreeList(head3);
    FreeList(head4);

    return 0;
}