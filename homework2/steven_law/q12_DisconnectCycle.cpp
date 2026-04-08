// Technique: Linked list fast-slow two-pointer / reset-catch-up two-pointer
// Time Complexity: O(n)
// Space Complexity: O(1)
// Time spent: 35 mins 3 seconds

#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

// Given a singly linked list, disconnect the cycle, if one exists.
Node* DisconnectCycle(Node* head) {
    if (head == nullptr) return nullptr;

    Node* fast = head;
    Node* slow = head;

    do{
        if (fast == nullptr || fast->next == nullptr) return head;
        fast = fast->next->next;
        slow = slow->next;

    } while(fast != slow);

    Node* entry = head;

    while(entry != slow){
        entry = entry -> next;
        slow = slow -> next;
    }
    while(slow->next != entry){
        slow = slow->next;
    }
    slow->next = nullptr;

    return head;

}

void printList(Node* head, int maxPrint = 20) {
    int count = 0;
    while (head != nullptr && count < maxPrint) {
        cout << head->data;
        if (head->next != nullptr) cout << " -> ";
        head = head->next;
        count++;
    }
    cout << endl;
}

int main() {
    // Example 1: 10 -> 18 -> 12 -> 9 -> 11 -> 4 -> cycle back to 12
    Node* c1 = new Node{10, nullptr};
    Node* c2 = new Node{18, nullptr};
    Node* c3 = new Node{12, nullptr};
    Node* c4 = new Node{9, nullptr};
    Node* c5 = new Node{11, nullptr};
    Node* c6 = new Node{4, nullptr};
    c1->next = c2; c2->next = c3; c3->next = c4;
    c4->next = c5; c5->next = c6; c6->next = c3; // cycle back to 12

    cout << "Example 1 (cycle to 12):" << endl;
    c1 = DisconnectCycle(c1);
    cout << "After: ";
    printList(c1);
    // Expected: 10 -> 18 -> 12 -> 9 -> 11 -> 4

    cout << endl;

    // Example 2: 10 -> 18 -> 12 -> 9 -> 11 -> 4 -> cycle back to 4 (self-loop)
    Node* d1 = new Node{10, nullptr};
    Node* d2 = new Node{18, nullptr};
    Node* d3 = new Node{12, nullptr};
    Node* d4 = new Node{9, nullptr};
    Node* d5 = new Node{11, nullptr};
    Node* d6 = new Node{4, nullptr};
    d1->next = d2; d2->next = d3; d3->next = d4;
    d4->next = d5; d5->next = d6; d6->next = d6; // self-loop

    cout << "Example 2 (self-loop on 4):" << endl;
    d1 = DisconnectCycle(d1);
    cout << "After: ";
    printList(d1);
    // Expected: 10 -> 18 -> 12 -> 9 -> 11 -> 4

    return 0;
}

/*
Strategy: 
so i think the first step is to identify the cycle entry and exit using the fast slow pointer method 
once we know the cycle entry point we can set a node = to that point and then move forward until the
next node is that point and then point that node to null instead of that node 

so like 

10 -> 18 -> 12 -> 9 -> 11 -> 4
             ^---------------|
we get the entry point by resetting one pointer to head and then moving both forward until they meet
thats where the cycle starts. then from there we just move forward until we find the node whos next
is the entry and set that to null to break the cycle. the do while was important because fast and slow
both start at head so a regular while would just immediately be false.
*/