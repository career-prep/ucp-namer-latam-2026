//Technique: Search binary search tree.
//Time Complexity: O(n), where is the number of nodes in the tree.
//In the worst case the tree is not balanced.
//Space Complexity: O(1).

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

        int floorInBST(Node* curr, int val){

            if(curr == nullptr) return INT_MIN;

            //If the value of the node is less than or equal to our value, then we can take the maximum
            //between that value, and the maximum value in its right subtree.
            if(curr -> data <= val){
                return std::max(curr -> data, floorInBST(curr -> right, val));
            }
            else{
                //In this case we only take the maximum in its left subtree.
                return floorInBST(curr -> left, val);
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

        //void delete();

        int solve_floorInBST(int val){

            Node* curr = root;
            return floorInBST(curr, val);
        }
};


int main(){

    vector<int> array = {10, 8, 16, 9, 13, 17, 20};
    //int k = 13;
    int k = 15;

    BinarySearchTree bst;

    for(auto value : array){
        bst.insert(value);
    }

    cout << bst.solve_floorInBST(k) << "\n";

    return 0;
}

//Time: 13 minutes.