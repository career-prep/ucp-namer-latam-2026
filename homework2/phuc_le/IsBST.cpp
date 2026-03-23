#include <iostream>
#include <limits>
using namespace std;

struct TreeNode
{
    int data;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int v) : data(v), left(nullptr), right(nullptr) {}
};

/*
    Core logic
    For each node, check if strictly within the allowed boundary
    Each node must be greater than every node in the left subtree and smaller than every node in the right subtree
    When go to left tree, same minVal, maxVal == curr
    When go to right tree, minVal == curr, same maxVal
    Assume no duplicate valid in the tree
    base case: Empty tree is a valid BST

    Time Complexity: O(n) - n: numbers of nodes, worst case visited every node
    Space:  O(H) H = height of the tree - maximum depth of the recursive stack
            Ranging from O(log(n)) for balance tree to O(n) for skewed tree

    Time: 40 mins
*/
bool IsBST(TreeNode *root, long long minVal, long long maxVal)
{
    // Base case: Empty tree is a valid BST
    if (!root)
    {
        return true;
    }
    // Not within the allowed boundaryn if leftMax < currVal < rightMin
    if (root->data <= minVal || root->data >= maxVal)
    {
        return false;
    }
    // Recursively check the left and right subtree for BST
    return IsBST(root->left, minVal, root->data) && IsBST(root->right, root->data, maxVal);
}

bool IsBSTWrapper(TreeNode *root)
{
    return IsBST(root, numeric_limits<long long>::min(), numeric_limits<long long>::max());
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

// Helper to safely free allocated memory (Post-Order to access the children)
void FreeTree(TreeNode *node)
{
    if (!node)
        return;
    FreeTree(node->left);
    FreeTree(node->right);
    delete node;
}

int main()
{
    // ---------------------------------------------------------
    // Test Case 1: Valid BST
    // ---------------------------------------------------------
    // Constructing the tree:
    //         10
    //        /  \
    //       8    16
    //        \  /  \
    //         9 13  17
    //                 \
    //                 20

    TreeNode *root1 = new TreeNode(10);
    root1->left = new TreeNode(8);
    root1->right = new TreeNode(16);
    root1->left->right = new TreeNode(9);
    root1->right->left = new TreeNode(13);
    root1->right->right = new TreeNode(17);
    root1->right->right->right = new TreeNode(20);

    cout << "Test Case 1 (Valid Tree):" << endl;
    cout << "In-Order Traversal: ";
    PrintInOrder(root1);
    cout << "\nIs BST? " << (IsBSTWrapper(root1) ? "True" : "False") << "\n\n";

    // ---------------------------------------------------------
    // Test Case 2: Invalid BST
    // ---------------------------------------------------------
    // Constructing the tree:
    //         10
    //        /  \
    //       8    16
    //        \  /  \
    //         9 13  17
    //                 \
    //                 15  <-- INVALID (Right child must be > 17)

    TreeNode *root2 = new TreeNode(10);
    root2->left = new TreeNode(8);
    root2->right = new TreeNode(16);
    root2->left->right = new TreeNode(9);
    root2->right->left = new TreeNode(13);
    root2->right->right = new TreeNode(17);
    root2->right->right->right = new TreeNode(15);

    cout << "Test Case 2 (Invalid Tree):" << endl;
    cout << "In-Order Traversal: ";
    PrintInOrder(root2);
    cout << "\nIs BST? " << (IsBSTWrapper(root2) ? "True" : "False") << "\n\n";

    // ---------------------------------------------------------
    // Test Case 3: Edge Case (Empty Tree)
    // ---------------------------------------------------------
    TreeNode *root3 = nullptr;

    cout << "Test Case 3 (Empty Tree):" << endl;
    cout << "Is BST? " << (IsBSTWrapper(root3) ? "True" : "False") << "\n\n";

    // Free allocated memory to prevent memory leaks
    FreeTree(root1);
    FreeTree(root2);

    return 0;
}