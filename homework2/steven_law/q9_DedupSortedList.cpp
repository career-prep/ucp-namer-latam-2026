// Technique: Simultaneous iteration two-pointer
// Time Complexity: O(n)
// Space Complexity: O(1)
// Time spent: 23 mins 42 seconds

#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

// Given a sorted singly linked list, remove any duplicates so that no value appears more than once.
Node* DedupSortedList(Node* head) {
    if(head == nullptr) return nullptr;

    Node* curr = head;

    while(curr != nullptr && curr->next != nullptr){
        if(curr->next->data == curr->data){
            Node* temp = curr->next; // temp is a dupe
            curr->next = curr ->next -> next; // skip over the dupe
            delete temp; //delete the dupe;
        }else{
            curr = curr-> next; //not a dupe so we continue 
        }
    }

    return head;

}

//helper to print the list
void printList(Node* head) {
    while (head != nullptr) {
        cout << head->data;
        if (head->next != nullptr) cout << " -> ";
        head = head->next;
    }
    cout << endl;
}

int main() {
    // Example 1: 1 -> 2 -> 2 -> 4 -> 5 -> 5 -> 5 -> 10 -> 10
    // Expected:  1 -> 2 -> 4 -> 5 -> 10
    Node* head1 = new Node{1, new Node{2, new Node{2, new Node{4, new Node{5, new Node{5, new Node{5, new Node{10, new Node{10, nullptr}}}}}}}}};

    cout << "Before: ";
    printList(head1);
    head1 = DedupSortedList(head1);
    cout << "After:  ";
    printList(head1);

    cout << endl;

    // Example 2: 8 -> 8 -> 8 -> 8
    // Expected:  8
    Node* head2 = new Node{8, new Node{8, new Node{8, new Node{8, nullptr}}}};

    cout << "Before: ";
    printList(head2);
    head2 = DedupSortedList(head2);
    cout << "After:  ";
    printList(head2);

    return 0;
}


/*
Strategy: so my logic for this is fairly simple, just check if the next elemnt is = to the current element,
if it is connect the current element to the next next element, skipping over the next one and then delete the
next one. 

edge cases, head being null to start off with, setting the while condition to curr->next != nullptr
deleting the data


*/