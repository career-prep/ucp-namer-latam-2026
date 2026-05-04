//Technique: General linked list iteration.
//Time Complexity: O(n), where is the number of nodes.
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

Node* createLinkedList(const vector<int> &array){

    Node* head = nullptr;

    for(int value : array){
        head = insertAtBack(head, value);
    }

    return head;
}

Node* solve_DedupSortedList(Node* head){

    //Handle empty list or with a single element
    if(head == nullptr || head -> next -> next == nullptr){
        return head;
    }

    //We keep track of the last node and the value of that node
    int last_value = head -> next -> data;
    Node* last_node = head -> next;

    Node* curr = head -> next -> next;

    while(curr != nullptr){

        //If the value for this node is equal to the one we already have, we ignore that node.
        if(curr -> data == last_value){
            curr = curr -> next;
        }
        else{
            //We update our variables if the value is different.
            last_node -> next = curr;
            last_node = last_node -> next;
            last_value = last_node -> data;
        }
    }

    last_node -> next = nullptr;

    return head;
}

int main(){

    vector<int> array = {1, 2, 2, 4, 5, 5, 5, 10, 10};
    //vector<int> array = {8, 8, 8, 8};

    Node* head = createLinkedList(array);

    printLinkedList(head);

    head = solve_DedupSortedList(head);

    printLinkedList(head);

    return 0;
}


//Time: 11 minutes
