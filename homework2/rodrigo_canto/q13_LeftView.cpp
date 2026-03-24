//Technique: Breadth-first-search traversal.
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

vector<int> solve_LeftView(Node* root){

    //Using queues to process the nodes in order of depth.
    queue<Node*> curr_depth;
    queue<Node*> nxt_depth;

    vector<int> answer;

    curr_depth.emplace(root);

    while(!curr_depth.empty()){
        
        //The first node that appears in the queue if the leftmost in its level of depth.
        answer.emplace_back(curr_depth.front() -> data);

        while(!curr_depth.empty()){

            Node* curr_node = curr_depth.front();
            curr_depth.pop();

            //Processing nodes that are a level below.
            if(curr_node -> left != nullptr) nxt_depth.emplace(curr_node -> left);
            if(curr_node -> right != nullptr) nxt_depth.emplace(curr_node -> right);
        }

        //Swapping queues for next iteration.
        swap(curr_depth, nxt_depth);
    }

    return answer;
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
    vector<Node*> array = {createNode(7),
    createNode(8), createNode(3),
    nullptr, nullptr, createNode(9), createNode(13),
    nullptr, nullptr, nullptr, nullptr, createNode(20), nullptr, createNode(14), nullptr,
    nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, createNode(15), nullptr, nullptr};
    */

    vector<Node*> array = {createNode(7),
    createNode(20), createNode(4),
    createNode(15), createNode(6), createNode(8), createNode(11)};

    Node* root = buildTree(array);

    vector<int> answer = solve_LeftView(root);

    for(auto u: answer) cout << u << " ";
    
    return 0;
}

//Time: 20 minutes.