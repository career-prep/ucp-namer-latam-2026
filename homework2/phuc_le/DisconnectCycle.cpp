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
    Given a singly linked list, disconnect the cycle, if one exists.
    Use Floyd theorem, fast and slow pointer method to detect the cycle
    If fast reach null, no cycle detected
    If detect the cycle, 2 cases:
        -   fast = head: Full loop cycle, find the tail of the linkedlist then break
        -   fast != head: P shaped cycle, use the fact that slow = fast when start of the cycle
                            find the node before that, break it and return the head
    Edge cases: empty list or single-element list cant have cycles

    Time Complexity: O(n) - n is the number of nodes.
    Space Complexity: O(1) - use no extra memory

    Time: 40 mins
*/
Node *DisconnectCycle(Node *head)
{
    // Edge case: empty list or single-element list
    if (head == nullptr || head->next == nullptr)
    {
        return head;
    }
    // Initialize the pointer for cycle detection
    Node *slow = head;
    Node *fast = head;
    bool cycleDetect = false;
    // Fast and slow pointers to detect cycle
    while (fast != nullptr && fast->next != nullptr)
    {
        slow = slow->next;
        fast = fast->next->next;
        // Cycle detect
        if (slow == fast)
        {
            // Break the cycle
            cycleDetect = true;
            break;
        }
    }
    // No cycle detect
    if (!cycleDetect)
    {
        return head;
    }
    // Break the cycle, 2 cases
    slow = head;
    // If the cycle begins at the head node
    if (slow == fast)
    {
        // Find the tail node
        while (fast->next != slow)
        {
            fast = fast->next;
        }
        fast->next = nullptr;
    }
    else
    // General case, when the loop is inside the linkedlist, Floyd's theorem make sure that when fast == slow is the start of the cycle
    {
        // Find the node before the start of the cycle
        while (fast->next != slow->next)
        {
            slow = slow->next;
            fast = fast->next;
        }
        fast->next = nullptr;
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
    // ---------------------------------------------------------
    // Test Case 1: General "P-Shape" Cycle
    // 10 -> 18 -> 12 -> 9 -> 11 -> 4 -> (loops back to 12)
    // ---------------------------------------------------------
    cout << "Test Case 1: General Cycle (loops to middle)" << endl;
    Node *head1 = new Node(10);
    head1->next = new Node(18);
    Node *cycleStart1 = new Node(12); // Node to loop back to
    head1->next->next = cycleStart1;
    cycleStart1->next = new Node(9);
    cycleStart1->next->next = new Node(11);
    Node *tail1 = new Node(4);
    cycleStart1->next->next->next = tail1;

    tail1->next = cycleStart1; // CREATE THE CYCLE

    head1 = DisconnectCycle(head1);
    cout << "Output: ";
    PrintList(head1); // Expected: 10 -> 18 -> 12 -> 9 -> 11 -> 4
    cout << "-----------------------" << endl;

    // ---------------------------------------------------------
    // Test Case 2: Self-Loop
    // 10 -> 18 -> 12 -> 9 -> 11 -> 4 -> (loops back to 4)
    // ---------------------------------------------------------
    cout << "Test Case 2: Self-Loop (tail points to itself)" << endl;
    Node *head2 = new Node(10);
    head2->next = new Node(18);
    head2->next->next = new Node(12);
    head2->next->next->next = new Node(9);
    head2->next->next->next->next = new Node(11);
    Node *tail2 = new Node(4);
    head2->next->next->next->next->next = tail2;

    tail2->next = tail2; // CREATE THE SELF-CYCLE

    head2 = DisconnectCycle(head2);
    cout << "Output: ";
    PrintList(head2); // Expected: 10 -> 18 -> 12 -> 9 -> 11 -> 4
    cout << "-----------------------" << endl;

    // ---------------------------------------------------------
    // Test Case 3: Edge Case - Entire List is a Circle
    // 1 -> 2 -> 3 -> (loops back to 1)
    // ---------------------------------------------------------
    cout << "Test Case 3: Circular List (tail points to head)" << endl;
    Node *head3 = new Node(1);
    head3->next = new Node(2);
    Node *tail3 = new Node(3);
    head3->next->next = tail3;

    tail3->next = head3; // CREATE THE CYCLE to head

    head3 = DisconnectCycle(head3);
    cout << "Output: ";
    PrintList(head3); // Expected: 1 -> 2 -> 3
    cout << "-----------------------" << endl;

    // ---------------------------------------------------------
    // Test Case 4: Edge Case - No Cycle
    // 1 -> 2 -> 3 -> 4 -> 5 -> null
    // ---------------------------------------------------------
    cout << "Test Case 4: No Cycle" << endl;
    Node *head4 = CreateList({1, 2, 3, 4, 5}); // No cycle created

    head4 = DisconnectCycle(head4);
    cout << "Output: ";
    PrintList(head4); // Expected: 1 -> 2 -> 3 -> 4 -> 5
    cout << "-----------------------" << endl;

    // ---------------------------------------------------------
    // Test Case 5: Edge Case - Empty List
    // ---------------------------------------------------------
    cout << "Test Case 5: Empty List" << endl;
    Node *head5 = nullptr;

    head5 = DisconnectCycle(head5);
    cout << "Output: ";
    PrintList(head5); // Expected: null
    cout << "-----------------------" << endl;

    // Free allocated memory safely (all cycles are now broken)
    FreeList(head1);
    FreeList(head2);
    FreeList(head3);
    FreeList(head4);

    return 0;
}