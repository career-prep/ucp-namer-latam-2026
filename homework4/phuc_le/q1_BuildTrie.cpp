#include <iostream>
#include <vector>
#include <string>
#include <cassert>

using namespace std;

struct TrieNode
{
    vector<TrieNode *> children;
    bool validWord;

    TrieNode()
    {
        children = vector<TrieNode *>(26, nullptr);
        validWord = false;
    }
};

class Trie
{
private:
    TrieNode *root;

public:
    Trie()
    {
        root = new TrieNode();
    }

    /*
        Inserts a word into the trie.
        - Start at the root node.
        - For each character, compute its index (0-25).
        - If the child node does not exist, create it.
        - Move to the child node.
        - After processing all characters, mark the last node as a valid word.

        Time: O(n), where n is the length of the word.
        Space: O(n) worst case if new nodes are created.
    */
    void insert(const string &word)
    {
        TrieNode *curr = root;

        for (char c : word)
        {
            int idx = c - 'a';

            if (curr->children[idx] == nullptr)
                curr->children[idx] = new TrieNode();

            curr = curr->children[idx];
        }

        curr->validWord = true;
    }

    /*
    Returns True if the word exists in the trie.
        - Start at the root node.
        - For each character, compute its index.
        - If the child does not exist, return False.
        - Move to the child node.
        - After processing all characters, return whether the final node
        is marked as a valid word.

        Time: O(n), where n is the length of the word.
        Space: O(1).
    */
    bool isValidWord(const string &word)
    {
        TrieNode *curr = root;

        for (char c : word)
        {
            int idx = c - 'a';

            if (curr->children[idx] == nullptr)
                return false;

            curr = curr->children[idx];
        }

        return curr->validWord;
    }

    /*
        Recursively removes a word from the trie.

        Returns:
        true  -> this node is no longer needed and can be deleted.
        false -> this node must remain in the trie.

        Time: O(n)
        Space: O(n)
    */
    bool removeHelper(TrieNode *node, const string &word, int depth)
    {
        if (node == nullptr)
            return false;

        // Reached end of word
        if (depth == word.size())
        {
            if (!node->validWord)
                return false;
            node->validWord = false;
            // If node has no children, delete it
            for (auto child : node->children)
            {
                if (child != nullptr)
                    return false;
            }
            return true;
        }

        int idx = word[depth] - 'a';
        TrieNode *child = node->children[idx];

        if (child == nullptr)
            return false;

        bool shouldDeleteChild = removeHelper(child, word, depth + 1);

        if (shouldDeleteChild)
        {
            delete child;
            node->children[idx] = nullptr;
        }

        // Never delete root
        if (node == root)
            return false;
        if (node->validWord)
            return false;

        for (auto c : node->children)
        {
            if (c != nullptr)
                return false;
        }

        return true;
    }

    /*
        Removes a word from the trie.
        - Use recursion to reach the end of the word.
        - If the word does not exist, do nothing.
        - Unmark the last node as a valid word.
        - While backtracking, delete nodes that:
            1. Have no children.
            2. Are not the end of another word.
        - Stop deleting once a node is still needed.

        Time: O(n), where n is the length of the word.
        Space: O(n) due to the recursion stack.
    */
    void remove(const string &word)
    {
        removeHelper(root, word, 0);
    }
};

// Tests

int main()
{
    Trie t;

    // Empty trie
    assert(!t.isValidWord("apple"));

    // Insert one word
    t.insert("apple");
    assert(t.isValidWord("apple"));
    assert(!t.isValidWord("app"));

    // Insert multiple words
    t.insert("app");
    t.insert("banana");
    assert(t.isValidWord("app"));
    assert(t.isValidWord("banana"));

    // Remove a word
    t.remove("app");
    assert(!t.isValidWord("app"));
    assert(t.isValidWord("apple"));

    // Remove another word
    t.remove("apple");
    assert(!t.isValidWord("apple"));
    assert(t.isValidWord("banana"));

    // Remove non-existing word
    t.remove("cat");
    assert(t.isValidWord("banana"));

    // Single-character word
    t.insert("a");
    assert(t.isValidWord("a"));
    t.remove("a");
    assert(!t.isValidWord("a"));

    cout << "All tests passed!\n";
    return 0;
}