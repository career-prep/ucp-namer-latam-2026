// Technique: Depth-first traversal (Generic)
// Time Complexity: O(n)
// Space Complexity: O(n)
// Time spent: 28 mins 8 seconds

#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;
};

bool IsBST(Node* root, int minVal, int maxVal){
    if(root == nullptr) return true;

    if(root->data <= minVal || root->data >= maxVal) return false;

    return IsBST(root->left, minVal, root->data) && IsBST(root->right, root->data, maxVal);
}

int main(){ 
// question for kyle, during interview will i have to write out all the test cases and everything...
//is there a more efficient way of doing this? writing everything out takes a lot of time,
// inclduing the struct, the main with print statements and the sig for the IsBST
//usually when I did leetcode they give u everything and test cases and most interviews in my exp
// usually do that as well, but i know ill have to test the code so if theres a faster way plz lmk

    //is a BST
    //        10
    //      /    \
    //     5      15
    //   /  \    /  \
    //  3    6  11   20
    
    
    Node* root1 = new Node {10, nullptr, nullptr };
    root1->left = new Node {5, nullptr, nullptr };
    root1->left->left = new Node {3, nullptr, nullptr };
    root1->left->right = new Node {6, nullptr, nullptr };
    root1->right = new Node {15, nullptr, nullptr };
    root1->right->left = new Node {11, nullptr, nullptr };
    root1->right->right = new Node {20, nullptr, nullptr };

     //is NOT a BST
    //        10
    //      /    \
    //    15      5
    //   /  \    /  \
    //  3    6  11   20

    Node* root2 = new Node {10, nullptr, nullptr };
    root2->left = new Node {15, nullptr, nullptr };
    root2->left->left = new Node {3, nullptr, nullptr };
    root2->left->right = new Node {6, nullptr, nullptr };
    root2->right = new Node {5, nullptr, nullptr };
    root2->right->left = new Node {11, nullptr, nullptr };
    root2->right->right = new Node {20, nullptr, nullptr };

    bool ex1 = IsBST(root1, INT_MIN, INT_MAX);
    bool ex2 = IsBST(root2, INT_MIN, INT_MAX);


    cout << "Example 1 (should be true): " << (ex1 ? "true" : "false") << endl;
    cout << "Example 2 (should be false): " << (ex2 ? "true" : "false") << endl;

    return 0;
}

/*
Must follow rule: Everything in the left subtree must be smaller and everything in the right
subtree must be bigger.

Strategy: So we need to ensure left tree is less i'll start with that,
to start we simply need root->left < root

from there it gets harder because the next layer on the left should be smaller than that first root,
and the next root. so im assuming we use something to keep track of that root value, that value
will be the max value the left side can go up to 

maxVal = root, 

each time we go down a new layer that max value shrinks with the parent for that set of children so 
we set maxVal to root again at each layer, if this ever breaks we know its not a valid bst.

now for the right side of the left sub tree,
we know it must be bigger than the parent but still smaller than the root from before

so we can compare it to the root from before ensuring its smaller and comparing it to the current root
to make sure that its greater, we can do this before updating the maxval 

and then for the right side i think we just flip the logic and it should workout so we need a minVal
*/