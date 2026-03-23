#include <iostream>
using namespace std;

struct TreeNode
{
    int data;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int v) : data(v), left(nullptr), right(nullptr) {}
};

/*
    From each node, create a copy of that node, assign it as the new root
    Recursively check for the left and right subtree
    Time: O(n) - n: numbers of nodes, each is visited once
    Space: O(log(n)) or O(H) H = height of the tree - maximum depth of the recursive stack
*/
TreeNode *DeepCopy(TreeNode *root)
{
    // Base case: Empty tree
    if (!root)
    {
        return nullptr;
    }
    // Create the node
    TreeNode *newRoot = new TreeNode(root->data);
    // Recursively copy children
    newRoot->left = DeepCopy(root->left);
    newRoot->right = DeepCopy(root->right);
    return newRoot;
}

// Helper to print the tree in order
void PrintInOrder(TreeNode *node)
{
    if (!node)
        return;
    PrintInOrder(node->left);
    cout << node->data << " ";
    PrintInOrder(node->right);
}

// Helper to safely free allocated memory (In-order)
void FreeTree(TreeNode *node)
{
    if (!node)
        return;
    FreeTree(node->left);
    delete node;
    FreeTree(node->right);
}

int main()
{
    // --- Test Case Construction (Binary Search Tree) ---
    //        4
    //       / \
    //      2   6
    //     / \ /
    //    1  3 5

    TreeNode *root = new TreeNode(4);

    // Level 1
    root->left = new TreeNode(2);
    root->right = new TreeNode(6);

    // Level 2
    root->left->left = new TreeNode(1);
    root->left->right = new TreeNode(3);
    root->right->left = new TreeNode(5);

    cout << "Original Tree (In-Order): ";
    PrintInOrder(root);
    cout << endl;

    // Create a deep copy
    TreeNode *clonedRoot = DeepCopy(root);

    // Test case
    cout << "Cloned Tree (In-Order):   ";
    PrintInOrder(clonedRoot);
    cout << endl;

    // Modify original to prove deep copy (cloned tree should remain unchanged)
    root->data = 99;
    cout << "\nAfter modifying original root to 99:" << endl;
    cout << "Original root data: " << root->data << endl;
    cout << "Cloned root data:   " << clonedRoot->data << " (Should still be 4)" << endl;

    // --- Memory Cleanup ---
    FreeTree(root);
    FreeTree(clonedRoot);

    return 0;
}