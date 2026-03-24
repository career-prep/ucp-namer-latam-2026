//Technique: Linked list fast-slow two pointer.
//Time Complexity: O(n), where n is the number of nodes in the linked list.
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

Node* nodeAtPosition(Node* head, int idx){

    if(length(head) < idx) return nullptr;

    int position = 0;

    Node* curr = head;

    while(position != idx){
        curr = curr -> next;
        position++;
    }

    return curr;
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

Node* startOfCycle(Node* head, Node* slow, Node* fast){

    //We reset the slow pointer and then move both pointers at the same speed.
    slow = head;

    while(slow != fast){
        slow = slow -> next;
        fast = fast -> next;
    }

    //The pointers will meet at the beginning of the cycle and we return that node.
    return slow;
}

/*
    This function uses Floyd´s algorithm to find the existence
    of a cycle in a linked list.
*/

Node* findStartOfCycle(Node* head){

    //We set two pointers.
    //At each time the fast pointer moves two positions and the slow one position.

    Node* slow = head;
    Node* fast = head;

    while(slow != nullptr && fast -> next != nullptr){
        slow = slow -> next;
        fast = fast -> next -> next;

        //If there is a cycle, the pointers will meet eventually.
        if(slow == fast){
            return startOfCycle(head, slow, fast);
        }
    }

    //If there is no cycle we return null.
    return nullptr;
}

void solve_DisconnectCycle(Node* head){

    //Since we know the node that is the beginning of the cycle, we need to find
    //the next node that has this one as next, so we can delete that connection.
    Node* start = findStartOfCycle(head);

    if(start == nullptr) return;

    Node* curr = start;

    while(curr -> next != start){
        curr = curr -> next;
    }

    //Delete the connection and set it to null.
    curr -> next = nullptr;
    return;
}

int main(){

    vector<int> array = {10, 18, 12, 9, 11, 4};

    Node* head = createLinkedList(array);

    //Generating cycle

    int position = 3;
    //int position = 6;
    nodeAtPosition(head, length(head)) -> next = nodeAtPosition(head, position);

    solve_DisconnectCycle(head);

    printLinkedList(head);

    return 0;
}

//Time: 15 minutes.
