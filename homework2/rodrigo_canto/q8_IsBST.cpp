//Technique Pre-Order Traversal.
//Time Complexity: O(n), where n is the number of nodes in the tree.
//Space Complexity: O(n).

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

/*
    For every node in the BST, there is a range of values that it can retrieve,
    so we need to check for every node if its value belongs to that range, if that does not
    ocurr then, the binary tree is not a BST.

    The range for a node is directly defined by the value of its ancestors in the tree.
*/

bool solve_IsBST(Node* curr, long long l, long long r){

    //If there is no child the requirement is not being violated.
    if(curr == nullptr) return true;

    //If the value does not belong to the range we return false.
    if(curr -> data <= l || curr -> data >= r) return false;

    //We need the AND operator because both subtrees must be valid.
    return solve_IsBST(curr -> left, l, curr -> data) && solve_IsBST(curr -> right, curr -> data, r);
}

//Function that builds a tree to create inputs.

Node* buildTree(vector<Node*> array){

    for(int i = 0; i < array.size(); ++i){

        Node* curr_node = array[i];

        if(curr_node == nullptr) continue;

        if(2 * i + 1 < array.size()){
            curr_node -> left = array[2 * i + 1];
        }

        if(2 * i + 2 < array.size()){
            curr_node -> right = array[2 * i + 2];
        }
    }

    return array[0];
}

int main(){

    /*
    vector<Node*> array = {createNode(10), 
    createNode(8), createNode(16),
    nullptr, createNode(9), createNode(13), createNode(17),
    nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, createNode(20)};
    */

    vector<Node*> array = {createNode(10), 
    createNode(8), createNode(16),
    nullptr, createNode(9), createNode(13), createNode(17),
    nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, createNode(15)};
    

    Node* root = buildTree(array);

    //For the root there is no restriction so we set the range to be extremely large.
    if(solve_IsBST(root, LLONG_MIN, LLONG_MAX)) cout << 1 << "\n";
    else cout << 0 << "\n";

    return 0;
}

//Time: 14 minutes.