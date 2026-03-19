// Technique: Search binary search tree (BST)
// Time Complexity: O(log n)
// Space Complexity: O(1)
// Time spent: 22 mins 31 seconds

#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;
};

// Given a target numeric value and a BST, return the floor (greatest element less than or equal to the target).
int FloorInBST(Node* root, int target) {
    int floor = -1;

    while (root != nullptr) {
        if (root->data == target) return root->data;

        if (root->data < target) {
            floor = root->data;
            root = root->right;
        } else {
            root = root->left;
        }
    }

    return floor;
}

int main() {
    //        10
    //       /  \
    //      8    16
    //       \   /
    //       9  13
    Node* root = new Node{10, nullptr, nullptr};
    root->left = new Node{8, nullptr, nullptr};
    root->right = new Node{16, nullptr, nullptr};
    root->left->right = new Node{9, nullptr, nullptr};
    root->right->left = new Node{13, nullptr, nullptr};

    // Example 1: target=13
    // Expected: 13
    cout << "FloorInBST(13): " << FloorInBST(root, 13) << " (expected 13)" << endl;

    // Example 2: target=15
    // Expected: 13
    cout << "FloorInBST(15): " << FloorInBST(root, 15) << " (expected 13)" << endl;

    return 0;
}

/*
Strategy:
so floor means the greatest value thats less than or equal to the target. im thinking we can
just use the bst property here and do a modified search.

if current node = target just return it. if its less than the target then it could be the floor
so we save it and go right to try to find somehting closer. if its bigger than target it cant
be the floor so we go left.

keep going until we hit null and whatever we saved last is the answer. pretty much just a bst
search but we keep track of the best candidate as we go. O(log n) since were just going down
one path of the tree.
*/