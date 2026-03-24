#include <iostream>
#include <stdexcept>
#include <vector>
#include <queue>

using namespace std;

struct TreeNode
{
    int data;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int v) : data(v), left(nullptr), right(nullptr) {}
};

/*
    Search binary search tree (BST)

    Given a target numeric value and a binary search tree, return the floor (greatest element less than or equal to the target) in the BST.
    - If node->data == target, we found the exact floor. Return it.
    - If node->data > target, the current node is too big. Move left.
    - If node->data < target, this node can be the answer. Save it,
      and move right to check for other floor.
    Return the answer

    Time Complexity:    O(h) - h: height of the tree, balance tree, O(log(n)), worst case O(n)
    Space Complexity:   O(1) - use no extra memory

    Time: 25 mins
*/
int FloorInBST(TreeNode *root, int target)
{
    int ans;
    // Check if there is a valid floor
    bool isFloor = false;
    // Check all valid branch
    while (root != nullptr)
    {
        // Found the exact floor
        if (root->data == target)
        {
            return root->data;
        }
        // Too big
        else if (root->data > target)
        {
            root = root->left;
        }
        // Valid floor, save it and move the root->right for checking
        else
        {
            ans = root->data;
            isFloor = true;
            root = root->right;
        }
    }
    // Edge case: Target < smallest number in tree or empty tree
    if (!isFloor)
    {
        throw runtime_error("No floor exists");
    }
    return ans;
}

// Helper to print a vector
void printVector(const vector<int> &v)
{
    cout << "[";
    for (size_t i = 0; i < v.size(); i++)
    {
        cout << v[i];
        if (i < v.size() - 1)
            cout << ", ";
    }
    cout << "]" << endl;
}

// Helper to safely free allocated memory
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
    /* BST:
             10
            /  \
           8    16
            \   / \
             9 13 17
                    \
                    20
    */
    TreeNode *root = new TreeNode(10);
    root->left = new TreeNode(8);
    root->left->right = new TreeNode(9);
    root->right = new TreeNode(16);
    root->right->left = new TreeNode(13);
    root->right->right = new TreeNode(17);
    root->right->right->right = new TreeNode(20);

    // Test Case 1: Target = 13 (Exact match)
    cout << "Test Case 1 (target = 13): ";
    try
    {
        cout << FloorInBST(root, 13) << endl; // Expected: 13
    }
    catch (const exception &e)
    {
        cout << e.what() << endl;
    }

    // Test Case 2: Target = 15
    cout << "Test Case 2 (target = 15): ";
    try
    {
        cout << FloorInBST(root, 15) << endl; // Expected: 13
    }
    catch (const exception &e)
    {
        cout << e.what() << endl;
    }

    // Test Case 3: Target = 25 (Larger than max element)
    cout << "Test Case 3 (target = 25): ";
    try
    {
        cout << FloorInBST(root, 25) << endl; // Expected: 20
    }
    catch (const exception &e)
    {
        cout << e.what() << endl;
    }

    // Test Case 4: Target = 5 (Smaller than min element)
    cout << "Test Case 4 (target = 5):  ";
    try
    {
        cout << FloorInBST(root, 5) << endl; // Expected: Error thrown
    }
    catch (const exception &e)
    {
        cout << e.what() << endl;
    }

    // Test Case 5: Edge Case - Empty Tree
    cout << "Test Case 5 (Empty Tree):  ";
    TreeNode *emptyRoot = nullptr;
    try
    {
        cout << FloorInBST(emptyRoot, 10) << endl; // Expected: Error thrown
    }
    catch (const exception &e)
    {
        cout << e.what() << endl;
    }

    // Free allocated memory
    FreeTree(root);

    return 0;
}