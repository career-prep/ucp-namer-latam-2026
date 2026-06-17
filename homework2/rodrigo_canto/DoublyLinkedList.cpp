#include "bits/stdc++.h"
using namespace std;

struct Node {
    int data;
    Node* next;
    Node* prev;
};

Node* createNode(int val){

    Node* node = new Node;
    node -> data = val;
    node -> next = nullptr;
    node -> prev = nullptr;
    return node;
}

Node* insertAtFront(Node* head, int val){

    if(head == nullptr){
        head = createNode(val);
        return head;
    }

    
    Node *new_node = createNode(val);
    new_node -> next = head;
    head -> prev = new_node;
    head = new_node;

    return head;
}

Node* insertAtBack(Node* head, int val){

    if(head == nullptr){
        head = createNode(val);
        return head;
    }

    Node *curr = head;

    while(curr -> next != nullptr){
        curr = curr -> next;
    }

    Node* new_node = createNode(val);

    curr -> next = new_node;
    new_node -> prev = curr;

    return head;
}

Node* insertAfter(Node* head, int val, Node* loc){

    Node* sig = loc -> next;

    Node* new_node = createNode(val);

    loc -> next = new_node;
    new_node -> prev = loc;

    new_node -> next = sig;
    sig -> prev = new_node;

    return head;
}

Node* insertBefore(Node* head, int val, Node* loc){

    Node* curr = head;

    if(head == loc){
        head = insertAtFront(head, val);
        return head;
    }

    while(curr -> next != loc) {
        curr = curr -> next;
    }

    head = insertAfter(head, val, curr);

    return head;
}

Node* deleteFront(Node* head){

    if(head == nullptr) return head;
    
    if(head -> next == nullptr){
        head = nullptr;
        return head;
    }

    Node* first = head;
    Node* second = first -> next;

    second -> prev = nullptr;
    head = second;

    return head;
}

Node* deleteBack(Node* head){

    if(head == nullptr) return head;

    if(head -> next == nullptr){
        head = nullptr;
        return head;
    }

    Node* curr = head;

    while(curr -> next != nullptr){
        curr = curr -> next;
    }

    Node* ant = curr -> prev;
    ant -> next = nullptr;

    return head;
}

Node* deleteNode(Node* head, Node* loc){

    if(head == nullptr) return head;

    if(head == loc){
        head = deleteFront(head);
        return head;
    }

    Node* curr = head;

    while(curr != loc){
        curr = curr -> next;
    }

    Node* ant = curr -> prev;
    Node* sig = curr -> next;

    if(sig == nullptr){
        head = deleteBack(head);
        return head;
    }

    ant -> next = sig;
    sig -> prev = ant;

    return head;
}

int length(Node* head){

    if(head == nullptr) return 0;

    int len = 0;

    Node* curr = head;

    while(curr != nullptr){
        len++;
        curr = curr -> next;
    }

    return len;
}

Node* reverseIterative(Node* head){

    if(head == nullptr || head -> next == nullptr) return head;

    Node* ant = head;
    Node* curr = ant -> next;

    ant -> next = nullptr;
    Node* sig = nullptr;

    while(curr != nullptr){

        ant -> prev = curr;
        sig = curr -> next;
        curr -> next = ant;

        ant = curr;
        curr = sig;
    }

    ant -> prev = nullptr;
    head = ant;

    return head;
}

Node* reverseLinkedList(Node* head, Node* curr, Node* &ant){

    if(curr -> next == nullptr){
        curr -> prev = nullptr;
        head = curr;
        ant = curr;
        return head;
    }

    head = reverseLinkedList(head, curr -> next, ant);

    ant -> next = curr;
    curr -> prev = ant;
    ant = curr;

    return head;
}

Node* reverseRecursive(Node* head){

    if(head == nullptr || head -> next == nullptr) return head;

    Node* ant = nullptr;
    
    head = reverseLinkedList(head, head, ant);

    ant -> next = nullptr;

    return head;
}

void printLinkedList(Node* head){

    if(head == nullptr) return;

    Node* curr = head;

    while(curr != nullptr){
        cout << curr -> data << " ";
        curr = curr -> next;
    }

    cout << "\n";
}

int main(){

    //Just testing functions.

    vector<int> arr = {1, 2, 3, 4, 5, 6};

    Node* head = nullptr;
    
    for(auto val : arr){
        head = insertAtBack(head, val);
    }

    printLinkedList(head);

    head = reverseRecursive(head);

    head = insertAtFront(head, 54);
    head = insertAtBack(head, 43);

    cout << length(head) << "\n";

    printLinkedList(head);
}

