// Technique: Doubly linked list forward-backward two-pointer
// Time Complexity: O(n)
// Space Complexity: O(1)
// Time spent: 24 mins 55 seconds

#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node* prev;
};

// Given a doubly linked list, determine if it is a palindrome.
bool IsPalindrome(Node* head) {
    if(head == nullptr) return false;
    if(head ->next == nullptr) return true;

    Node* tail = head;
    while(tail -> next != nullptr){
        tail = tail->next;
    }

    while(head != tail && head ->prev != tail){
        if(head->data != tail->data) return false;

        head = head->next;
        tail = tail->prev;
    }

    return true;
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
    // Example 1: 9 -> 2 -> 4 -> 2 -> 9 (palindrome)
    Node* a1 = new Node{9, nullptr, nullptr};
    Node* a2 = new Node{2, nullptr, a1};
    Node* a3 = new Node{4, nullptr, a2};
    Node* a4 = new Node{2, nullptr, a3};
    Node* a5 = new Node{9, nullptr, a4};
    a1->next = a2; a2->next = a3; a3->next = a4; a4->next = a5;

    cout << "List 1: ";
    printList(a1);
    cout << "Palindrome? " << (IsPalindrome(a1) ? "true" : "false") << " (expected true)" << endl;

    cout << endl;

    // Example 2: 9 -> 12 -> 4 -> 2 -> 9 (not palindrome)
    Node* b1 = new Node{9, nullptr, nullptr};
    Node* b2 = new Node{12, nullptr, b1};
    Node* b3 = new Node{4, nullptr, b2};
    Node* b4 = new Node{2, nullptr, b3};
    Node* b5 = new Node{9, nullptr, b4};
    b1->next = b2; b2->next = b3; b3->next = b4; b4->next = b5;

    cout << "List 2: ";
    printList(b1);
    cout << "Palindrome? " << (IsPalindrome(b1) ? "true" : "false") << " (expected false)" << endl;

    return 0;
}

/*
Strategy:
since its a doubly linked list we have prev pointers which makes this way easier than if it was
singly linked. my idea is just two pointers one at head one at tail and compare moving inward.

first i gotta get to the tail tho so i traverse to the end. then compare head and tail, if they
match move head forward tail backward keep going.

if at any point they dont match its not a palindrome so return false.

for the stopping condtion like for odd length lists head == tail
when they meet but for even length they actually cross over each other. so i check for both
head != tail and head->prev != tail to catch that

if list is empty return false, one node is automatically a palindrome
*/
