//Time Complexity: O(N * M * 7^(L)), where L is the lenght of the largest string in the trie.

/*
    The backtracking is the slowest part of the algorithm, at every cell we have 7 cells to consider because a cell 
    can not be visited twice.
    Since we have 7 options, the number of possibilities, is the multiplication of the number of options
    at every time during our tracking.
*/

//Space Complexity: O(W * L * K)

/*
    W is the number of words
    L is the length of the largest word
    K is the size of the alphabet.
*/

//Technique: Trie and Backtracking

#include "bits/stdc++.h"
using namespace std;

const int K = 26;

int row[] = {1, 0, -1, 0, 1, 1, -1, -1};
int col[] = {0, 1, 0, -1, 1, -1, 1, -1};

struct TrieNode{
    vector<TrieNode*> children;
    bool valid_word;

    TrieNode(){

        valid_word = false;

        children.resize(K);

        for(int i = 0; i < K; ++i){
            children[i] = nullptr;
        }
    }
};

struct Trie{

    TrieNode* root;

    Trie(){
        root = new TrieNode();
    }

    void insert(string word){

        TrieNode* curr_node = root;

        for(char c : word){

            //If the node does not exist we create the node
            if(curr_node -> children[c - 'a'] == nullptr){
                curr_node -> children[c - 'a'] = new TrieNode;
            }

            curr_node = curr_node -> children[c - 'a'];
        }

        //The current node is the end of the word we are inserting.
        curr_node -> valid_word = true;
    }

    bool isValidWord(string word){

        TrieNode* curr_node = root;

        for(char c: word){

            //This means the word does not exist in the trie.
            if(curr_node -> children[c - 'a'] == nullptr) return false;
            curr_node = curr_node -> children[c - 'a'];
        }

        //We check if the node contains a valid word.
        return curr_node -> valid_word;
    }

    bool has_children(TrieNode* current_node){
        
        for(int i = 0; i < K; ++i){
            if(current_node -> children[i] != nullptr) return true;
        }
        
        return false;
    }

    TrieNode* remove_helper(TrieNode* current, string &word, int depth){

        //The word does not exist in the trie
        if(current == nullptr) return nullptr;

        //This is the leaf of the word in the structure
        if(depth == (int)word.size()){

            //We are removing this word so the node does not contain a valid word anymore.
            current -> valid_word = false;

            //The word is not a prefix of other word in the trie.
            if(!has_children(current)){

                delete current;
                current = nullptr;
            }

            return current;
        }

        int letter_idx = word[depth] - 'a';
        current -> children[letter_idx] = remove_helper(current -> children[letter_idx], word, depth + 1);

        //If it does not have children and the node is not the end of another word, we can remove that node.
        if(!has_children(current) && !(current -> valid_word)){
            delete current;
            current = nullptr;
        }

        return current;
    }

    void remove(string &word){
        remove_helper(root, word, 0);
    }
};

bool inrange(int i, int j, int n, int m){
    if(i < 0 || i >= n || j < 0 || j >= m) return false;
    return true;
}


void tracking(Trie* trie, TrieNode* current_node, int i, int j, string &word, 
    vector<vector<char>> &board, vector<vector<bool>> &visited, vector<string> &answer, int n, int m){

    //The word we are forming does not exist in the dictionary
    if(current_node == nullptr) return;

    visited[i][j] = true;
    //If this is a valid word, we push the word in the vector and remove it from the trie, so we do not count twice.
    if(current_node -> valid_word){
        answer.push_back(word);
        trie -> remove(word);
    }

    //Check adjacent neighbors to see if we can find more words.
    
    for(int k = 0; k < 8; ++k){
        int new_i = i + row[k], new_j = j + col[k];

        if(inrange(new_i, new_j, n, m) && !visited[new_i][new_j]){

            //Insert the letter in our word.
            word.push_back(board[new_i][new_j]);
            
            int letter_idx = board[new_i][new_j] - 'a';

            tracking(trie, current_node -> children[letter_idx], new_i, new_j, word, board, visited, answer, n, m);

            //We erase the letter to consider other paths.
            word.pop_back();
        }
    }

    visited[i][j] = false;
}


void solve_Boggle(vector<string> &dictionary, vector<vector<char>> &board){
    Trie* trie = new Trie();

    //We manipulate lowercase letters in the trie.
    for(string word : dictionary){
        string lower_word = "";
        for(char c : word) lower_word.push_back(tolower(c));
        trie -> insert(lower_word);
    }

    int n = board.size();
    int m = board[0].size();
    
    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < m; ++j) {
            board[i][j] = tolower(board[i][j]);
        }
    }

    vector<string> answer;
    vector<vector<bool>> visited(n, vector<bool>(m, false));

    //Start the tracking at every cell.
    for(int i = 0; i < n; ++i){
        for(int j = 0; j < m; ++j){
            int letter_idx = board[i][j] - 'a';
            if(trie -> root -> children[letter_idx] != nullptr){
                string word = "";
                word.push_back(board[i][j]);
                tracking(trie, trie -> root -> children[letter_idx], i, j, word, board, visited, answer, n, m);
            }
        }
    }

    for(string found_word : answer){
        cout << found_word << "\n";
    }
}

int main(){
    vector<string> dictionary = {
        "Ace", "Ape", "Cape", "Clap", "Clay", "Gape", "Grape", "Lace", "Lap", 
        "Lay", "Mace", "Map", "May", "Pace", "Pay", "Race", "Rap", "Ray", 
        "Tap", "Tape", "Trace", "Trap", "Tray", "Yap"
    };

    vector<vector<char>> board = {
        {'A', 'D', 'E'},
        {'R', 'C', 'P'},
        {'L', 'A', 'Y'}
    };

    solve_Boggle(dictionary, board);

    return 0;
}

//Time Spent: 28 minutes

