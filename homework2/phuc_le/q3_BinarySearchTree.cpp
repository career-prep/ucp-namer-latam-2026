#include <stdlib.h>
#include <iostream>
#include <stdexcept>
using namespace std;

struct Node
{
    int data;
    Node *left;
    Node *right;
    Node(int v) : data(v), left(nullptr), right(nullptr) {}
};

class BinarySearchTree
{
private:
    Node *root;
    // Require root
    Node *deleteNode(Node *root, int val)
    {
        if (root == nullptr)
        {
            return root;
        }
        // Find the node to delete
        if (val > root->data)
        {
            root->right = deleteNode(root->right, val);
        }
        else if (val < root->data)
        {
            root->left = deleteNode(root->left, val);
        }
        else
        {
            // Find the node to delete and it only have right child or left child
            if (root->left == nullptr)
            {
                Node *temp = root->right;
                delete root;
                return temp;
            }
            else if (root->right == nullptr)
            {
                Node *temp = root->left;
                delete root;
                return temp;
            }
            // Has both left and right child
            Node *curr = root->right;
            // Find the min on the right subtree
            while (curr->left != nullptr)
            {
                curr = curr->left;
            }
            // Replace the delete node
            root->data = curr->data;
            // Recursively delete the duplicate node in the right subtree
            root->right = deleteNode(root->right, curr->data);
        }
        // Also cover if no left and right children, then the root will be nullptr
        return root;
    }

    // Function helper for in-order printing
    void printInOrder(Node *node)
    {
        if (node != nullptr)
        {
            printInOrder(node->left);
            cout << node->data << " ";
            printInOrder(node->right);
        }
    }

public:
    // Constructor (init the empty tree)
    BinarySearchTree() : root(nullptr) {}
    ~BinarySearchTree() {}

    // returns the minimum value in the BST.  O(logn) time.
    int min()
    {
        // The minimum is always on the left of a BST tree
        if (root == nullptr)
        {
            throw runtime_error("Tree is empty.");
        }
        Node *curr = root;
        // The minimum is always on the left of a BST tree
        while (curr->left != nullptr)
        {
            curr = curr->left;
        }
        return curr->data;
    }
    // returns the maximum value in the BST.  O(logn) time.
    int max()
    {
        if (root == nullptr)
        {
            throw runtime_error("Tree is empty.");
        }
        Node *curr = root;
        // The maximum is always on the right of a BST tree
        while (curr->right != nullptr)
        {
            curr = curr->right;
        }
        return curr->data;
    }
    // returns a boolean indicating whether val is present in the BST.O(logn) time.
    bool contains(int val)
    {
        // Check both left and right
        // If val > curr, right, else left, do unil nullptr
        Node *curr = root;
        while (curr != nullptr)
        {
            if (val > curr->data)
            {
                curr = curr->right;
            }
            else if (val < curr->data)
            {
                curr = curr->left;
            }
            else
            {
                return true;
            }
        }
        return false;
    }
    // creates a new Node with data val in the appropriate location. For simplicity, do not allow duplicates.If val is already present, insert is a no - op. O(logn) time.
    void insert(int val)
    {
        // Find the location to insert, where curr is nullptr and it is appropriated following BST left < curr < right
        Node *newNode = new Node(val);
        if (root == nullptr)
        {
            root = newNode;
            return;
        }
        Node *curr = root;
        Node *parentNode = nullptr;
        // Find the place to add
        while (curr != nullptr)
        {
            parentNode = curr;
            if (val > curr->data)
            {
                curr = curr->right;
            }
            else if (val < curr->data)
            {
                curr = curr->left;
            }
            else
            {
                // Cant be duplicate
                delete newNode;
                return;
            }
        }
        // Add the new node
        if (val < parentNode->data)
        {
            parentNode->left = newNode;
        }
        else
        {
            parentNode->right = newNode;
        }
        return;
    }
    // deletes the Node with data val, if it exists. O(logn) time.
    void deleteVal(int val)
    {
        root = deleteNode(root, val);
    }

    void print()
    {
        if (root == nullptr)
        {
            cout << "Tree is empty.";
        }
        else
        {
            printInOrder(root);
        }
        cout << endl;
    }
};

int main()
{
    BinarySearchTree tree;

    cout << "--- 1. Testing Insertions ---\n";
    tree.insert(50);
    tree.insert(30);
    tree.insert(70);
    tree.insert(20);
    tree.insert(40);
    tree.insert(60);
    tree.insert(80);

    cout << "In-order traversal (should be sorted): ";
    tree.print();

    cout << "\n--- 2. Testing Duplicates ---\n";
    cout << "Attempting to insert 40 again (should no-op).\n";
    tree.insert(40);
    cout << "Tree remains: ";
    tree.print();

    cout << "\n--- 3. Testing Min and Max ---\n";
    cout << "Minimum value: " << tree.min() << " (Expected 20)\n";
    cout << "Maximum value: " << tree.max() << " (Expected 80)\n";

    cout << "\n--- 4. Testing Contains ---\n";
    cout << "Contains 60? " << (tree.contains(60) ? "True" : "False") << " (Expected True)\n";
    cout << "Contains 90? " << (tree.contains(90) ? "True" : "False") << " (Expected False)\n";

    cout << "\n--- 5. Testing Deletions ---\n";

    // Case 1: Delete a leaf node
    cout << "Deleting 20 (Leaf node)...\n";
    tree.deleteVal(20);
    tree.print();

    // Case 2: Delete a node with one child
    cout << "Inserting 85 to give 80 one child...\n";
    tree.insert(85);
    cout << "Deleting 80 (One child)...\n";
    tree.deleteVal(80);
    tree.print();

    // Case 3: Delete a node with two children
    cout << "Deleting 50 (Root node, Two children)...\n";
    tree.deleteVal(50);
    cout << "New Tree: ";
    tree.print();

    return 0;
}