/*
    Technique:
    - Trie as a parameter
    - DFS/Backtracking on the board

    - Insert all dictionary words into a Trie.
    - Start a DFS from every cell on the board.
    - While exploring, follow the Trie simultaneously.
    - If the next character does not exist in the Trie, stop exploring
    - When a Trie node represents a complete word, add the current string to the answer.
    - Use a visited array so that a cell cannot be reused in the same word.

    Time Complexity:
    - Building the Trie: O(D)
    where D is the total number of characters in the dictionary.

    - DFS Search:
    In the worst case, each cell can branch to at most 8 neighbors, giving O(R * C * 8^L),
    where:
        R = number of rows,
        C = number of columns,
        L = maximum word length.

    Overall: O(D + R * C * 8^L)

    Space Complexity:
    - Trie: O(D)
    - Visited array: O(R * C)
    - Recursion stack: O(L)
    - Answer set: O(K), where K is the number of words found.

    Overall: O(D + R * C + L + K)

    Time spent: 40 minutes
*/

#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
#include <algorithm>

using namespace std;

struct TrieNode
{
    TrieNode *children[26];
    bool isWord;

    TrieNode()
    {
        isWord = false;
        for (int i = 0; i < 26; i++)
            children[i] = nullptr;
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

    TrieNode *getRoot()
    {
        return root;
    }

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

        curr->isWord = true;
    }
};

class Boggle
{
private:
    int rows;
    int cols;

    vector<vector<bool>> visited;
    unordered_set<string> answer;

    vector<pair<int, int>> directions = {
        {-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

    void dfs(
        vector<vector<char>> &board,
        int r,
        int c,
        TrieNode *node,
        string current)
    {
        char ch = board[r][c];
        int idx = ch - 'a';

        if (node->children[idx] == nullptr)
            return;

        node = node->children[idx];
        current += ch;

        if (node->isWord && current.size() >= 3)
            answer.insert(current);

        visited[r][c] = true;

        for (auto [dr, dc] : directions)
        {
            int nr = r + dr;
            int nc = c + dc;

            if (nr < 0 || nr >= rows ||
                nc < 0 || nc >= cols)
                continue;

            if (visited[nr][nc])
                continue;

            dfs(board, nr, nc, node, current);
        }

        visited[r][c] = false;
    }

public:
    vector<string> findWords(
        vector<vector<char>> &board,
        vector<string> &dictionary)
    {
        rows = board.size();
        cols = board[0].size();

        Trie trie;

        for (string word : dictionary)
            trie.insert(word);

        visited = vector<vector<bool>>(rows, vector<bool>(cols, false));

        answer.clear();

        for (int r = 0; r < rows; r++)
        {
            for (int c = 0; c < cols; c++)
            {
                dfs(board, r, c,
                    trie.getRoot(),
                    "");
            }
        }

        return vector<string>(
            answer.begin(),
            answer.end());
    }
};

// Example Usage
int main()
{
    vector<string> dictionary = {
        "ace",
        "ape",
        "cape",
        "clap",
        "clay",
        "gape",
        "grape",
        "lace",
        "lap",
        "lay",
        "mace",
        "map",
        "may",
        "pace",
        "pay",
        "race",
        "rap",
        "ray",
        "tap",
        "tape",
        "trace",
        "trap",
        "tray",
        "yap"};

    vector<vector<char>> board = {
        {'a', 'd', 'e'},
        {'r', 'c', 'p'},
        {'l', 'a', 'y'}};

    Boggle solver;

    vector<string> words =
        solver.findWords(board, dictionary);

    sort(words.begin(), words.end());

    cout << "Words found:\n";
    for (const string &w : words)
        cout << w << endl;

    return 0;
}