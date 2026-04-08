//Technique: Doubly linked list forward-backward two pointer.
//Time Complexity: O(n), where n is the number of nodes.
//Space Complexity: O(1).


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

Node* find_LastElement(Node* head){

    Node* curr = head;

    while(curr -> next != nullptr){
        curr = curr -> next;
    }

    return curr;
}

Node* createLinkedList(const vector<int> &array){

    Node* head = nullptr;

    for(int value : array){
        head = insertAtBack(head, value);
    }

    return head;
}

bool solve_IsPalindrome(Node* head){

    //Handle empty list or list with a single element.
    if(head == nullptr || head -> next -> next == nullptr) return true;

    /*
        We have a doubly linked list. We set two pointers, one at the beginning and the other one
        at the end of the list, and keep iterating while the pointers are different.

        During the iteration we need to check if the value in both pointers is the same.
        If they are different, then the linked list is not a palindrome.
    */

    Node* node_l = head;
    Node* node_r = find_LastElement(head);

    while(node_l != node_r){

        if(node_l -> data != node_r -> data) return false;
        node_l = node_l -> next;

        //We can access the previous node because it is a doubly linked list.
        node_r = node_r -> prev;
    }

    return true;
}

int main(){

    vector<int> array = {9, 2, 4, 2, 9};
    //vector<int> array = {9, 12, 4, 2, 9};

    Node* head = createLinkedList(array);

    if(solve_IsPalindrome(head)) cout << 1 << "\n";
    else cout << 0 << "\n";
    
}

