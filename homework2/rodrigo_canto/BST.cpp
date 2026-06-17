#include "bits/stdc++.h"
using namespace std;

struct Node{
    int data;
    Node* left;
    Node* right;
};

Node* createNode(int val){
    
    Node* node = new Node;
    node -> data = val;
    node -> left = nullptr;
    node -> right = nullptr;

    return node;
}

class BinarySearchTree {
    
    private:

        Node* root = nullptr;

        void insert(int val, Node* curr){

            if(curr -> data == val) return;

            if(val > curr -> data){

                if(curr -> right == nullptr){

                    Node* new_node = createNode(val);

                    curr -> right = new_node;
                    return;
                }
                else{

                    insert(val, curr -> right);
                }
            }
            else{

                if(curr -> left == nullptr){

                    Node* new_node = createNode(val);

                    curr -> left = new_node;
                    return;
                }
                else{

                    insert(val, curr -> left);
                }
            }
        }

    public:
        
        int min(){

            Node* curr = root;

            while(curr -> left != nullptr){
                curr = curr -> left;
            }
            
            return curr -> data;
        }

        int max(){

            Node* curr = root;

            while(curr -> right != nullptr){
                curr = curr -> right;
            }

            return curr -> data;
        }

        bool contains(int val){

            Node* curr = root;

            while(curr != nullptr){

                if(curr -> data == val) return true;

                if(val > curr -> data){
                    curr = curr -> right;
                }
                else{
                    curr = curr -> left;
                }
            }

            return false;
        }

        void insert(int val){

            if(root == nullptr){
                root = createNode(val);
            }
            else{

                Node* curr = root;
                insert(val, curr);
            }
        }
};

int main(){

    BinarySearchTree bst;
    
    return 0;
}