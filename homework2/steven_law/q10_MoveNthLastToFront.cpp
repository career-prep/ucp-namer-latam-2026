// Technique: Linked list fixed-distance two-pointer
// Time Complexity: O(n)
// Space Complexity: O(1)
// Time spent: 27 mins 17 seconds

#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

// Given a singly linked list, move the nth from the last element to the front of the list.
Node* MoveNthLastToFront(Node* head, int k) {
    if(head == nullptr) return nullptr;
    Node* right = head;
    Node* left = head;

    while(k > 0){
        right = right->next;
        k--;
    }
    if(right == nullptr) return head;

    while(right->next != nullptr){
        right = right->next;
        left = left->next;
    }

    Node* target = left->next;
    left->next = left->next->next;

    target->next = head;
    head = target;

    return head;

}

void printList(Node* head) {
    while (head != nullptr) {
        cout << head->data;
        if (head->next != nullptr) cout << " -> ";
        head = head->next;
    }
    cout << endl;
}

int main() {
    // Example 1: k=2
    // 15 -> 2 -> 8 -> 7 -> 20 -> 9 -> 11 -> 6 -> 19
    // Expected: 6 -> 15 -> 2 -> 8 -> 7 -> 20 -> 9 -> 11 -> 19
    Node* head1 = new Node{15, new Node{2, new Node{8, new Node{7, new Node{20, new Node{9, new Node{11, new Node{6, new Node{19, nullptr}}}}}}}}};

    cout << "Before: ";
    printList(head1);
    head1 = MoveNthLastToFront(head1, 2);
    cout << "After (k=2):  ";
    printList(head1);

    cout << endl;

    // Example 2: k=7
    // 15 -> 2 -> 8 -> 7 -> 20 -> 9 -> 11 -> 6 -> 19
    // Expected: 8 -> 15 -> 2 -> 7 -> 20 -> 9 -> 11 -> 6 -> 19
    Node* head2 = new Node{15, new Node{2, new Node{8, new Node{7, new Node{20, new Node{9, new Node{11, new Node{6, new Node{19, nullptr}}}}}}}}};

    cout << "Before: ";
    printList(head2);
    head2 = MoveNthLastToFront(head2, 7);
    cout << "After (k=7):  ";
    printList(head2);

    return 0;
}

/*
Stratergy: 

this feels a lot like the fixed distance two pointer strat, we start by moving the first pointer k
times to the right, then keep move both pointers to the right at the same time until the right = nullptr

for example if k = 2 and we have 1 2 3 4 5 6 we need 5 1 2 3 4 6
so l = 1 and r = 3 . now we move to the right one by one 
l = 2, r = 4
l = 3, r = 5
l = 4, r = 6
l = 5, r = nullptr

now we unlink 5 and make it the new head 

we point 4 to 6 and then point 5 to 1 or in this case head.

esdge cases: if head = nullptr, if k = the size of the list we move head to the front , alr there
so we must return head instead of checking for right->next because itll crash
*/