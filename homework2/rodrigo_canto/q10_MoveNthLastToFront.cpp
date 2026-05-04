//Technique: Linked list fixed-distance two-pointer.
//Time Complexity: O(n), where n is the number of nodes.
//Space Complexity: O(1).

#include "bits/stdc++.h"
using namespace std;

struct Node {
    int data;
    Node* next;
};

Node* createNode(int val){

    Node* node = new Node;
    node -> data = val;
    node -> next = nullptr;
    return node;
}

Node* insertAtFront(Node* head, int val){

    if(head == nullptr){
        head = createNode(0);
        head -> next = createNode(val);
        return head;
    }

    Node *first = head -> next;
    Node *new_node = createNode(val);

    head -> next = new_node;
    new_node -> next = first;

    return head;
}

Node* insertAtBack(Node* head, int val){

    if(head == nullptr){
        head = createNode(0);
        head -> next = createNode(val);
        return head;
    }

    Node *curr = head;

    while(curr -> next != nullptr){
        curr = curr -> next;
    }

    Node* new_node = createNode(val);

    curr -> next = new_node;

    return head;
}

Node* insertAfter(Node* head, int val, Node* loc){

    Node* sig = loc -> next;

    Node* new_node = createNode(val);

    loc -> next = new_node;
    new_node -> next = sig;

    return head;
}

Node* insertBefore(Node* head, int val, Node* loc){

    Node* curr = head;

    while(curr -> next != loc) {
        curr = curr -> next;
    }

    head = insertAfter(head, val, curr);

    return head;
}

Node* deleteFront(Node* head){

    if(head == nullptr) return head;

    Node* first = head -> next;
    Node* second = first -> next;

    head -> next = second;

    if(head -> next == nullptr) head = nullptr;
    return head;
}

Node* deleteBack(Node* head){

    if(head == nullptr) return head;

    Node* curr = head;

    while(curr -> next -> next != nullptr){
        curr = curr -> next;
    }

    curr -> next = nullptr;

    if(head -> next == nullptr) head = nullptr;
    return head;
}

Node* deleteNode(Node* head, Node* loc){

    if(head == nullptr) return head;

    if(head -> next == loc){
        
        head -> next = head -> next -> next;
        if(head -> next == nullptr) head = nullptr;
        return head;
    }
    else{

        Node* prev = head -> next;
        Node* curr = prev -> next;

        while(curr != loc){
        
            prev = curr;
            curr = curr -> next;
        }

        prev -> next = curr -> next;
        return head;
    }
}

int length(Node* head){

    if(head == nullptr) return 0;

    int len = 0;

    Node* curr = head;

    while(curr -> next != nullptr){
        len++;
        curr = curr -> next;
    }

    return len;
}

Node* reverseIterative(Node* head){

    if(head == nullptr) return head;

    Node* ant = head -> next;
    Node* curr = ant -> next;

    ant -> next = nullptr;
    Node* sig = nullptr;

    while(curr != nullptr){

        sig = curr -> next;
        curr -> next = ant;

        ant = curr;
        curr = sig;
    }

    head -> next = ant;

    return head;
}

Node* reverseLinkedList(Node* head, Node* curr, Node* &prev){

    if(curr -> next == nullptr){
        head -> next = curr;
        prev = curr;
        return head;
    }

    head = reverseLinkedList(head, curr -> next, prev);

    prev -> next = curr;
    prev = curr;

    return head;
}

Node* reverseRecursive(Node* head){

    if(head == nullptr) return head;

    if(head -> next -> next == nullptr) return head;

    Node* prev = nullptr;
    
    head = reverseLinkedList(head, head -> next, prev);

    prev -> next = nullptr;

    return head;
}

void printLinkedList(Node* head){

    if(head == nullptr) return;

    Node* curr = head -> next;

    while(curr != nullptr){
        cout << curr -> data << " ";
        curr = curr -> next;
    }

    cout << "\n";
}

Node* find_Nth(Node* head, int k){

    Node* slow = head;
    Node* fast = head;

    //Declare two pointers and the distance between them is going to be k.
    for(int i = 0; i < k; ++i) fast = fast -> next;

    //When the fast node reach the end of the list, the slow node will be kth node from the last element.

    while(fast != nullptr){

        slow = slow -> next;
        fast = fast -> next;
    }

    return slow;
}

Node* solve_MoveNth(Node *head, int k){

    //Edge cases
    if(head == nullptr || length(head) < k){
        return head;
    }

    //Find the node we need to move.
    Node* loc = find_Nth(head, k);

    //Delete the node and insert it at the beginning of the list.
    head = deleteNode(head, loc);
    head = insertAtFront(head, loc -> data);

    return head;
}

Node* createLinkedList(const vector<int> &array){

    Node* head = nullptr;

    for(int value : array){
        head = insertAtBack(head, value);
    }

    return head;
}

int main(){

    vector<int> array = {15, 2, 8, 7, 20, 9, 11, 6, 19};
    int k = 2;
    //int k = 7;

    Node* head = createLinkedList(array);

    printLinkedList(head);

    head = solve_MoveNth(head, k);

    printLinkedList(head);

    return 0;
}

//Time: 14 minutes.

