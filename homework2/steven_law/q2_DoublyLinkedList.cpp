// Time spent: 25 mins 12 seconds

#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node* prev;
};

// creates new Node with data val at front; returns head. O(1) time.
Node* insertAtFront(Node* head, int val) {
    Node* newNode = new Node();                                                                                                                                                        
    newNode->data = val;                                       
    newNode->prev = nullptr;                                                                                                                                                           
    newNode->next = head;                                                                                                                                                              
                                                                                                                                                                                     
    if (head != nullptr) {                                                                                                                                                             
      head->prev = newNode;                                  
    }                                            
                                                                                                                                                                                     
    return newNode;
}

// creates new Node with data val at end; returns head. O(1) time.
Node* insertAtBack(Node* head, Node* tail, int val) {

    Node* newNode = new Node();                                                                                                                                                        
    newNode->data = val; 
    newNode->next = nullptr;

    if(head == nullptr){
        newNode ->prev = nullptr;
        return newNode;
    }

    newNode ->prev = tail;
    tail -> next = newNode;

    

    return head;
}

// creates new Node with data val after Node loc; returns head. O(1) time.
Node* insertAfter(Node* head, int val, Node* loc) {
    Node* newNode = new Node();                                                                                                                                                        
    newNode->data = val;

    newNode->next = loc->next;
    newNode->prev = loc;

    if (loc->next != nullptr) {                                                                                                                                                        
      loc->next->prev = newNode;
    }

    loc->next = newNode;

    return head; 
}

// creates new Node with data val before Node loc; returns head. O(1) time.
Node* insertBefore(Node* head, int val, Node* loc) {

    Node* newNode = new Node();                                                                                                                                                        
    newNode->data = val;

    if (loc == head) {
      newNode->prev = nullptr;
      newNode->next = head;
      head->prev = newNode;
      return newNode;
  }

    

    loc->prev->next = newNode;
    newNode->prev = loc->prev;
    newNode->next = loc;

    loc->prev = newNode;

    return head;
}

// removes first Node; returns head. O(1) time.
Node* deleteFront(Node* head) {
    if(head == nullptr) return nullptr;
    if(head->next == nullptr){
        delete head;
        return nullptr;
    } 

    Node* temp = head;
    head = head->next;
    head->prev = nullptr;
    delete temp;
    return head;
}

// removes last Node; returns head. O(1) time. null 1 null
Node* deleteBack(Node* head, Node* tail) {
    if(head == nullptr) return nullptr;
    if(tail->prev == nullptr){
        delete tail;
        return nullptr;
    }
    Node* temp = tail;

    tail = tail->prev;
    tail->next = nullptr;
    delete temp;
    return head;
}

// deletes Node loc; returns head. O(1) time.
Node* deleteNode(Node* head, Node* loc) {

    if (head == nullptr) return nullptr;

    if (loc == head) {
      head = head->next;
      if (head != nullptr) head->prev = nullptr;
      delete loc;
      return head;
    }

    if (loc->next == nullptr) {
      loc->prev->next = nullptr;
      delete loc;
      return head;
    }

    loc->prev->next = loc->next;
    loc->next->prev = loc->prev;
    delete loc;
    return head;

}

// returns length of the list. O(n) time.
int length(Node* head) {
    if(head == nullptr) return 0;

    int count = 0;

    while(head != nullptr){
        head = head->next;
        count++;
    }

    return count;
}

// reverses the linked list iteratively. O(n) time.
Node* reverseIterative(Node* head) {
    if (head == nullptr) return nullptr;

    Node* curr = head;
    Node* previous = nullptr;
    Node* temp = curr;

    while(curr != nullptr){
       

        temp = curr->next;
        curr->next = previous;
        curr->prev = temp;
        previous = curr;
        curr = temp;
    }

    return previous;
}

// reverses the linked list recursively (Hint: you will need a helper function.) O(n) time.
Node* reverseRecursive(Node* head) {
    return reverseHelper(head);
}

Node* reverseHelper(Node* curr) {
    if (curr == nullptr || curr->next == nullptr) {
        if (curr != nullptr) curr->prev = nullptr;
        return curr;
    }

    Node* newHead = reverseHelper(curr->next);
    curr->next->next = curr;
    curr->prev = curr->next;
    curr->next = nullptr;
    return newHead;
  }

int main() {

    return 0;
}
