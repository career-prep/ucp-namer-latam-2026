#include <iostream>
#include <vector>
using namespace std;

struct Node
{
    int data;
    Node *next;
    Node *prev;
    Node(int v) : data(v), next(nullptr), prev(nullptr) {}
};

/*
    Given a doubly linked list, determine if it is a palindrome.
    Edge case: Empty or single-element list is a palindrome
    Tranverse to the end of the doubly linkedlist to find the tail
    Move both the left and right end until they meet or cross
    If different, not palindrome
    If not return, is palindrome

    Time Complexity: O(n) - n: numbers of node in the linkedlist
    Space Complexity: O(1) - use no extra memory

    Time: 40 mins
*/
bool IsPalindrome(Node *head)
{
    // Edge case
    if (head == nullptr || head->next == nullptr)
    {
        return true;
    }
    // Traverse to the end to find the tail
    Node *left = head;
    Node *right = head;
    while (right->next != nullptr)
    {
        right = right->next;
    }
    // Move pointers towards each other until they meet or cross
    // odd length: meet, even length: cross
    while (left != right && left->prev != right)
    {
        // Not palindrome
        if (left->data != right->data)
        {
            return false;
        }
        // Move the pointers
        left = left->next;
        right = right->prev;
    }
    return true;
}

// Helper to create a doubly linked list from a vector
Node *CreateDoublyList(const vector<int> &vals)
{
    if (vals.empty())
        return nullptr;

    Node *head = new Node(vals[0]);
    Node *current = head;

    for (size_t i = 1; i < vals.size(); ++i)
    {
        Node *newNode = new Node(vals[i]);
        current->next = newNode;
        newNode->prev = current;
        current = newNode;
    }
    return head;
}

// Helper to print the list
void PrintList(Node *head)
{
    if (!head)
    {
        cout << "null" << endl;
        return;
    }

    Node *temp = head;
    Node *tail = nullptr;

    cout << "Forward:  ";
    while (temp != nullptr)
    {
        cout << temp->data;
        if (temp->next != nullptr)
            cout << " <-> ";
        tail = temp;
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
    // Test Case 1: Odd-length Palindrome
    cout << "Test Case 1: Odd-length Palindrome" << endl;
    Node *head1 = CreateDoublyList({9, 2, 4, 2, 9});
    PrintList(head1);
    cout << "Is Palindrome? " << (IsPalindrome(head1) ? "True" : "False") << "\n"
         << endl;

    // Test Case 2: Odd-length Non-Palindrome
    cout << "Test Case 2: Odd-length Non-Palindrome" << endl;
    Node *head2 = CreateDoublyList({9, 12, 4, 2, 9});
    PrintList(head2);
    cout << "Is Palindrome? " << (IsPalindrome(head2) ? "True" : "False") << "\n"
         << endl;

    // Test Case 3: Even-length Palindrome (Exposes the original bug)
    cout << "Test Case 3: Even-length Palindrome" << endl;
    Node *head3 = CreateDoublyList({1, 2, 2, 1});
    PrintList(head3);
    cout << "Is Palindrome? " << (IsPalindrome(head3) ? "True" : "False") << "\n"
         << endl;

    // Test Case 4: Even-length Non-Palindrome (Fails middle check in original code)
    cout << "Test Case 4: Even-length Non-Palindrome (Middle mismatch)" << endl;
    Node *head4 = CreateDoublyList({1, 2, 3, 1});
    PrintList(head4);
    cout << "Is Palindrome? " << (IsPalindrome(head4) ? "True" : "False") << "\n"
         << endl;

    // Test Case 5: Single Element List
    cout << "Test Case 5: Single Element" << endl;
    Node *head5 = CreateDoublyList({5});
    PrintList(head5);
    cout << "Is Palindrome? " << (IsPalindrome(head5) ? "True" : "False") << "\n"
         << endl;

    // Test Case 6: Empty List
    cout << "Test Case 6: Empty List" << endl;
    Node *head6 = nullptr;
    PrintList(head6);
    cout << "Is Palindrome? " << (IsPalindrome(head6) ? "True" : "False") << "\n"
         << endl;

    // Free memory
    FreeList(head1);
    FreeList(head2);
    FreeList(head3);
    FreeList(head4);
    FreeList(head5);

    return 0;
}