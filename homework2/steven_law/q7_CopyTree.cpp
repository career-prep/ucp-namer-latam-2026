// Technique: Linked list recursion / DFS Generic
// Time Complexity: O(n)
// Space Complexity: O(n)
// Time spent: 21 mins 24 seconds

#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;
};

// Given a binary tree, create a deep copy. Return the root of the new tree.
Node* copyTree(Node* root) {
    if(root == nullptr) return nullptr;
    Node* newTree = new Node();

    newTree -> data = root -> data;

    newTree -> left = copyTree(root->left);
    newTree -> right = copyTree(root->right);

    return newTree;


}

int main() {
    // Example 1:
    //        10
    //       /  \
    //      5    15
    //     / \     \
    //    3   7    20
    Node* root1 = new Node{10, nullptr, nullptr};
    root1->left = new Node{5, nullptr, nullptr};
    root1->right = new Node{15, nullptr, nullptr};
    root1->left->left = new Node{3, nullptr, nullptr};
    root1->left->right = new Node{7, nullptr, nullptr};
    root1->right->right = new Node{20, nullptr, nullptr};

    // Example 2:
    //      1
    //     /
    //    2
    //   /
    //  3
    Node* root2 = new Node{1, nullptr, nullptr};
    root2->left = new Node{2, nullptr, nullptr};
    root2->left->left = new Node{3, nullptr, nullptr};

    Node* copy1 = copyTree(root1);
    Node* copy2 = copyTree(root2);

    // verify its a deep copy
    cout << "Copy1 root: " << copy1->data << " original root: " << root1->data << endl;
    cout << "Same pointer? " << (copy1 == root1 ? "yes (wrong)" : "no (correct)") << endl;

    cout << "Copy2 root: " << copy2->data << " original: " << root2->data << endl;

    cout << "Same pointer? " << (copy2 == root2 ? "yes (wrong)" : "no (correct)") << endl;

    return 0;
}

/*
Strategy: so this one is basically just a recursive approach, if the root is null we return null as our base case
and from there we just create a new node, copy the data over and then recursively do the same thing for the left
and right children. pretty straightforward honestly, the key thing here is that we are creating NEW nodes
so its a deep copy and not just pointing to the same nodes in memory.

to structure the recursion i think we can just do preorder traversal but instead of
printing we can copying the data into a new node.
*/
