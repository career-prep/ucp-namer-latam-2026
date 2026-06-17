#include "bits/stdc++.h"
using namespace std;

const int K = 26;

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
        if(current == nullptr) return;

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



