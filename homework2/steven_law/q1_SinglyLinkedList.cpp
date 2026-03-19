// Time spent: 29 mins 35 seconds

#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

// creates new Node with data val at front; returns head. O(1) time.
Node* insertAtFront(Node* head, int val) {

    Node* newNode = new Node();

    newNode -> data = val; 
    newNode -> next = head;
    head = newNode;

    return head;
}

// creates new Node with data val at end; returns head. O(n) time.
Node* insertAtBack(Node* head, int val) {

    Node* newNode = new Node();

    newNode -> data = val;

    if(head == nullptr){ // if head is null return newNode
        newNode -> next = nullptr;
        return newNode;
    }

    Node* temp = head;

    while(temp -> next != nullptr ){
        temp = temp->next;
    }

    temp->next = newNode;
    temp->next->next = nullptr;

    return head;
}

// creates new Node with data val after Node loc; returns head. O(1) time.
Node* insertAfter(Node* head, int val, Node* loc) {

    Node* newNode = new Node();                                                                                                                                                        
    newNode->data = val;

    newNode->next = loc->next;                                                                                                                                                         
    loc->next = newNode;        

    return head;
}

// creates new Node with data val before Node loc; returns head. O(n) time.
Node* insertBefore(Node* head, int val, Node* loc) {

    Node* newNode = new Node();
    newNode->data = val;

    Node* temp = head;

    if (head == loc) {                                                                                                                                                                 
      newNode->next = head;                                                                                                                                                          
      return newNode;                                                                                                                                                                
    } 

    while(temp -> next != loc ){
        temp = temp->next;
    }

    newNode->next = loc;
    temp->next = newNode;

    return head;
 
}

// removes first Node; returns head. O(1) time.
Node* deleteFront(Node* head) {
    if(head == nullptr){
        return head;
    }

    Node* temp = head;                                                                                                                                                                 
    head = head->next;

    delete temp;      //can't leak memory

    return head;
}

// removes last Node; returns head. O(n) time.
Node* deleteBack(Node* head) {
 
     if (head == nullptr) return nullptr; 
     
     if (head->next == nullptr) {                                                                                                                                                       
        delete head;                                                                                                                                                                   
        return nullptr;                                                                                                                                                                
    }                                                                                                                                                                                  
                                                                                                       
  Node* temp = head;        

  while (temp->next->next != nullptr) {                                                                
      temp = temp->next;                       
    }

  delete temp->next;
  temp->next = nullptr;

  return head;
}

// deletes Node loc; returns head. O(n) time.
Node* deleteNode(Node* head, Node* loc) {

  if (head == nullptr) return nullptr;

  if (head == loc) {                                                                                                                                                                 
      Node* newHead = head->next;                                                                      
      delete head;                                                                                                                                                                   
      return newHead;                                                                                                                                                                
  }  
    
    Node* temp = head;

    while(temp->next != loc){
        temp = temp->next;
    }

    Node* temp2 = temp->next->next;

    delete temp->next;
    temp->next = temp2;

    return head;
}

// returns length of the list. O(n) time.
int length(Node* head) {
    int count = 0;

    while(head != nullptr){
        head = head->next;
        count++;
    }

    return count;
}

// reverses the linked list iteratively. O(n) time.
Node* reverseIterative(Node* head) {
    if(head == nullptr || head->next == nullptr ) return head;
    

    Node* prev = nullptr;
    Node* curr = head;
    Node* temp = curr;

    while(curr != nullptr){
        temp = curr->next;
        curr->next = prev;
        prev = curr;
        curr = temp;
    }

    return prev;
}

// reverses the linked list recursively (Hint: you will need a helper function.) O(n) time.
Node* reverseRecursive(Node* head) {
    return reverseHelper(head);
}

Node* reverseHelper(Node* curr) {  
    if (curr == nullptr || curr->next == nullptr) return curr;                                                                                                                     
                                                                                                                                                                                     
    Node* newHead = reverseHelper(curr->next);                                                       
    curr->next->next = curr;                                                                                                                                                       
    curr->next = nullptr;    
                                                                            
    return newHead;
}




int main() {

    return 0;
}
