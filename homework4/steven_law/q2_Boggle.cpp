/*Data Structure: Trie
Algorithm: Trie as a parameter + DFS/backtracking over the board
Technique: Trie as a parameter
Time Complexity: O(D*L) build + O(R*C * 8^maxLen) worst case DFS (trie pruning cuts it way down)
Space Complexity: O(total dict chars) trie + O(maxLen) recursion
Time Taken: 33 mins 41 seconds
*/

#include<iostream>
#include<vector>
#include <string>
#include <set>

using namespace std;

/*
1. dump every dict word into a trie (lowercased).
2. dfs from every cell, walking the board + the trie in lockstep.
3. if the trie has no child for the current letter -> prune, no word goes this way.
4. mark cell used, append to path. if trie node is a word end + path >= 3, record it.
5. recurse into the 8 neighbors that arent used yet, then backtrack (unmark + pop).
6. set dedupes (same word reachable multiple ways).
*/

struct TrieNode {
    vector<TrieNode*> children;
    bool validWord;
    TrieNode() : children(26, nullptr), validWord(false) {}
};

void insertWord(TrieNode* root, const string& w){
    TrieNode* curr = root;
    for(char ch : w){
        int idx = ch - 'a';
        if(curr->children[idx] == nullptr) curr->children[idx] = new TrieNode();
        curr = curr->children[idx];
    }
    curr->validWord = true;
}

void dfs(vector<vector<char>>& board, int r, int c, TrieNode* node,
         string& path, vector<vector<bool>>& used, set<string>& found){

    TrieNode* next = node->children[board[r][c] - 'a'];
    if(next == nullptr) return; //no dict word continues with this prefix, prune

    path.push_back(board[r][c]);
    used[r][c] = true;

    if(next->validWord && path.size() >= 3) found.insert(path);

    int R = board.size(), C = board[0].size();
    for(int dr = -1; dr <= 1; dr++){
        for(int dc = -1; dc <= 1; dc++){
            if(dr == 0 && dc == 0) continue;
            int nr = r + dr, nc = c + dc;
            if(nr >= 0 && nr < R && nc >= 0 && nc < C && !used[nr][nc]){
                dfs(board, nr, nc, next, path, used, found);
            }
        }
    }

    used[r][c] = false; //backtrack
    path.pop_back();
}

vector<string> Boggle(vector<vector<char>> board, vector<string> dictionary){
    TrieNode* root = new TrieNode();
    for(string w : dictionary){
        for(char& ch : w) ch = tolower(ch);
        insertWord(root, w);
    }

    int R = board.size(), C = board[0].size();
    vector<vector<bool>> used(R, vector<bool>(C, false));
    set<string> found;
    string path;

    for(int r = 0; r < R; r++){
        for(int c = 0; c < C; c++){
            dfs(board, r, c, root, path, used, found);
        }
    }
    return vector<string>(found.begin(), found.end());
}

int main(){
    vector<vector<char>> board = {
        {'a','d','e'},
        {'r','c','p'},
        {'l','a','y'}
    };
    vector<string> dictionary = {
        "ace","ape","cape","clap","clay","gape","grape","lace","lap","lay",
        "mace","map","may","pace","pay","race","rap","ray","tap","tape",
        "trace","trap","tray","yap"
    };

    vector<string> output = Boggle(board, dictionary);
    int expectedOutput = 14;

    cout << "Actual result: " << output.size() << " words" << endl;
    cout << "Expected result: " << expectedOutput << " words" << endl;
    for(auto& w : output) cout << "  " << w << endl;
}

/* psudocode/thoughts/logic
goal: find every dict word (>= 3 chars) traceable on the board through adjacent (incl diagonal)
cells, no cell reused per word
restraints: each board position used at most once in a single word

strategy: this is the "trie as a parameter" move. word-driven (search each word separately)
redoes shared prefixes over and over — trace/trap/tray would all re-walk "tra". instead build
ONE trie of the dictionary and walk the board + trie together. the second the board path stops
being a prefix of any word, the trie has no child and we prune instantly. dfs (not bfs) because
the no-reuse rule is natural with backtracking — flip used on going in, off coming out.

big O: building the trie is O(D*L). the dfs is bounded by the board branching (8 dirs) up to
the longest word, but in practice the trie prune kills almost all of that.
*/
