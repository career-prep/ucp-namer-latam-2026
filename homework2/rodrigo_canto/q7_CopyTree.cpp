//Technique - Pre-order Traversal.
//Time Complexity: O(n), where n is the number of nodes in the binary tree.
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

Node* solve_copyTree(Node *curr){

    //When the node does not exist
    if(curr == nullptr) return nullptr;

    Node* new_node = createNode(curr -> data);

    //Left child
    new_node -> left = solve_copyTree(curr -> left);

    //Right child
    new_node -> right = solve_copyTree(curr -> right);

    return new_node;
}

//Function to check if two trees are equal in structure.
//It allows me to see if the solution is working.

bool equal_tree(Node *curr_node, Node* curr_other_node){

    if(curr_node == nullptr && curr_other_node == nullptr) return true;

    if(curr_node == nullptr || curr_other_node == nullptr) return false;

    if(curr_node -> data != curr_other_node -> data) return false;

    return ((equal_tree(curr_node -> left, curr_other_node -> left)) && (equal_tree(curr_node -> right, curr_other_node -> right)));
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

    vector<Node*> array = {createNode(10), 
    createNode(8), createNode(16),
    nullptr, createNode(9), createNode(13), createNode(17),
    nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, createNode(20)};

    Node* root = buildTree(array);

    Node* new_root = solve_copyTree(root);

    if(equal_tree(root, new_root)) cout << 1 << "\n";
    else cout << 0 << "\n";

    return 0;
}

//Time: 7 minutes