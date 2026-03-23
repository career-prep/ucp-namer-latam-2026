#include <iostream>
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
    Implement Breadth-First Search (Level Order Traversal)
    For each level in the BFS, append the first element into the result list
    Return the ans list with all the leftView elements

    Time Complexity:    O(n) - n: is the number of nodes
    Space Complexity:   O(w) - w: is the maximum width of the tree at any given time.
                                Worst case is O(n/2) = O(n) for a balanced tree.

    Time: 35 mins
*/
vector<int> leftView(TreeNode *root)
{
    // Base case: Empty tree
    if (root == nullptr)
    {
        return {};
    }
    // Queue for BFS
    queue<TreeNode *> q;
    vector<int> res;
    // Append the root node as the first one
    q.push(root);
    // Do BFS on the whole tree, visited every node atlease once
    while (!q.empty())
    {
        // Numbers of node in each level
        int levelSize = q.size();
        // Go through every node, check for its children
        for (int i = 0; i < levelSize; i++)
        {
            TreeNode *curr = q.front();
            q.pop();
            // First node of every level is in the leftView list
            if (i == 0)
            {
                res.push_back(curr->data);
            }
            // Push children to queue for the next level
            if (curr->left != nullptr)
            {
                q.push(curr->left);
            }
            if (curr->right != nullptr)
            {
                q.push(curr->right);
            }
        }
    }
    return res;
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
    /* Test Case 1:
             7
            / \
           8   3
              / \
             9  13
            /   /
           20  14
                 \
                 15
    */
    TreeNode *root1 = new TreeNode(7);
    root1->left = new TreeNode(8);
    root1->right = new TreeNode(3);
    root1->right->left = new TreeNode(9);
    root1->right->right = new TreeNode(13);
    root1->right->left->left = new TreeNode(20);
    root1->right->right->left = new TreeNode(14);
    root1->right->right->left->right = new TreeNode(15);

    cout << "Test Case 1 (Image Example 1):" << endl;
    vector<int> result1 = leftView(root1);
    cout << "Output: ";
    printVector(result1); // Expected: [7, 8, 9, 20, 15]
    cout << "-----------------------" << endl;

    /* Test Case 2:
             7
            / \
          20   4
         /  \ / \
        15  6 8 11
    */
    TreeNode *root2 = new TreeNode(7);
    root2->left = new TreeNode(20);
    root2->right = new TreeNode(4);
    root2->left->left = new TreeNode(15);
    root2->left->right = new TreeNode(6);
    root2->right->left = new TreeNode(8);
    root2->right->right = new TreeNode(11);

    cout << "Test Case 2 (Image Example 2):" << endl;
    vector<int> result2 = leftView(root2);
    cout << "Output: ";
    printVector(result2); // Expected: [7, 20, 15]
    cout << "-----------------------" << endl;

    /* Test case 3:
        1
         \
          2
           \
            3
    */
    TreeNode *root3 = new TreeNode(1);
    root3->right = new TreeNode(2);
    root3->right->right = new TreeNode(3);

    cout << "Test Case 3 (Right Skewed Tree):" << endl;
    vector<int> result3 = leftView(root3);
    cout << "Output: ";
    printVector(result3); // Expected: [1, 2, 3]
    cout << "-----------------------" << endl;

    // Test Case 4: Edge Case - Empty Tree
    TreeNode *root4 = nullptr;

    cout << "Test Case 4 (Empty Tree):" << endl;
    vector<int> result4 = leftView(root4);
    cout << "Output: ";
    printVector(result4); // Expected: []
    cout << "-----------------------" << endl;

    // Free allocated memory
    FreeTree(root1);
    FreeTree(root2);
    FreeTree(root3);

    return 0;
}