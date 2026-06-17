// Technique: Level-order (breadth-first) traversal
// Time Complexity: O(n)
// Space Complexity: O(n)
// Time spent: 29 mins 19 seconds

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;
};

// Given a binary tree, create an array of the left view (leftmost elements in each level) of the tree.
vector<int> LeftView(Node* root) {

    vector<int> result;
    if (root == nullptr) return result;

    queue<Node*> q;
    q.push(root);

    while (!q.empty()) {
        int levelSize = q.size();

        for (int i = 0; i < levelSize; i++) {
            Node* curr = q.front();
            q.pop();

            if (i == 0) result.push_back(curr->data); 

            if (curr->left) q.push(curr->left);
            if (curr->right) q.push(curr->right);
          }
      }

      return result;
}

int main() {
    // Example 1:
    //        7
    //      /   \
    //     8     3
    //    /     /
    //   9    13
    // Expected: [7, 8, 9]
    Node* root1 = new Node{7, nullptr, nullptr};
    root1->left = new Node{8, nullptr, nullptr};
    root1->right = new Node{3, nullptr, nullptr};
    root1->left->left = new Node{9, nullptr, nullptr};
    root1->right->left = new Node{13, nullptr, nullptr};

    vector<int> res1 = LeftView(root1);
    cout << "Example 1: ";
    for (int i = 0; i < res1.size(); i++) {
        cout << res1[i] << " ";
    }
    cout << endl;
    cout << "Expected:  7 8 9" << endl;

    cout << endl;

    // Example 2:
    //        7
    //      /   \
    //    20     4
    //   /  \
    //  15   6
    // Expected: [7, 20, 15]
    Node* root2 = new Node{7, nullptr, nullptr};
    root2->left = new Node{20, nullptr, nullptr};
    root2->right = new Node{4, nullptr, nullptr};
    root2->left->left = new Node{15, nullptr, nullptr};
    root2->left->right = new Node{6, nullptr, nullptr};

    vector<int> res2 = LeftView(root2);
    cout << "Example 2: ";
    for (int i = 0; i < res2.size(); i++) {
        cout << res2[i] << " ";
    }
    cout << endl;
    cout << "Expected:  7 20 15" << endl;

    return 0;
}


/*
Strategy:

so we need to create an array of the left view of the tree, so like the first node at every level
if your looking from the left side.

im thinking bfs here because we literally need to go level by level. i was trying to think of how
dfs would work but it felt way more complicated for no reason so im sticking with bfs.

so we push root into a queue and then we have an outer while loop, inside that we grab the size
of the queue which tells us how many nodes are at the current level. then we loop through those nodes
and pop each one off, if its the first one (i == 0) we push it into our result. then we add the left
and right children to the queue for next level.

how to know when a new level starts the q.size() handles that
because at the start of each while iteration the queue only has the nodes from that level in it

edge case if root is null just return empty vector.
*/