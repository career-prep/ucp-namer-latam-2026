// Time spent: 36 mins 48 seconds

#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;
};

class BinarySearchTree {
private:
    Node* root;

public:
    BinarySearchTree() : root(nullptr) {}

    // returns the minimum value in the BST. O(logn) time.
    int min() {
        if(root == nullptr) return -1;
        Node* temp = root;

        while(temp->left != nullptr){
            temp = temp->left;
        }
        return temp->data;
    }

    // returns the maximum value in the BST. O(logn) time.
    int max() {
        if(root == nullptr) return -1;
        Node* temp = root;

        while(temp->right != nullptr){
            temp = temp->right;
        }
        return temp->data;

    }

    // returns a boolean indicating whether val is present in the BST. O(logn) time.
    bool contains(int val) {
        
        Node* temp = root;
        while (temp != nullptr) {
            if (val == temp->data) return true;
            else if (val < temp->data) temp = temp->left;
            else temp = temp->right;
        }

        return false;

    }

    // creates a new Node with data val in the appropriate location.
    // For simplicity, do not allow duplicates. If val is already present, insert is a no-op. O(logn) time.
    void insert(int val) {

        Node* newNode = new Node();
        newNode->data = val;
        newNode->left = nullptr;
        newNode->right = nullptr;

        if (root == nullptr){
            root = newNode;
            return;
        }
            
        Node* temp = root;
        while (true) {
            if (val == temp->data) return; // duplicate. no op
            if (val < temp->data) {
            if (temp->left == nullptr) {
                    temp->left = newNode;
                    return;
               }
               temp = temp->left;
           } else {
                 if (temp->right == nullptr) {
                    temp->right = newNode;
                    return;
                }
               temp = temp->right;
            }
        }

    }

    // deletes the Node with data val, if it exists. O(logn) time.
    void deleteNode(int val) { //stuck

        Node* temp = root;
        Node* previous = root;

        while(temp != nullptr){
            if(temp->data == val){

            }
            if(temp->data < val ){
                previous = temp;
                temp = temp->left;
            }

        }

        
        return;

    }
};

int main() {

    return 0;
}
