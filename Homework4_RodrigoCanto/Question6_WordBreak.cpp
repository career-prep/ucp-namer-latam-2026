//Time Complexity: O(n^2)
//Space Complexity: O(m + n)
//Where m is the sum of lenghts of the words in the dictionary and n is the length of the string.

//Technique: Trie and Backtracking

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
};

bool can_divide(int idx, string &word, vector<string> &answer, TrieNode* root, string &current_word){

    //This base case tells us that all the letters have been covered and the division is possible.
    if(idx == (int)word.size()) return true;

    TrieNode* current_node = root;

    //Iterate through the letters starting at idx.
    //idx represents the position of the first letter that we need to cover.
    for(int i = idx; i < word.size(); ++i){

        int letter_idx = word[i] - 'a';

        if(current_node -> children[letter_idx] != nullptr){
            current_word.push_back(word[i]);
            current_node = current_node -> children[letter_idx];

            //If at some letter we have a dictionary word, we can take that word as part of our answer.
            if(current_node -> valid_word){

                answer.push_back(current_word);

                string nxt_word = "";

                //If the rest of the string has a possible division, we found an answer.
                if(can_divide(i + 1, word, answer, root, nxt_word)) return true;

                //Otherwise, we delete the word and look for another combination.
                answer.pop_back();
            }
        }
        else{
            return false;
        }
    }

    return false;
}

//Function to put a word in lowercase letters.
string lowercase_word(string &word){
    string new_word = "";

    for(auto c : word){
        c = tolower(c);
        new_word.push_back(c);
    }

    return new_word;
}


void solve_wordBreak(vector<string> &dictionary, string &word){

    Trie* trie = new Trie;

    //Insert the dictionary words in the trie.
    for(auto word : dictionary){
        trie -> insert(lowercase_word(word));
    }

    vector<string> answer;
    string empty_word = "";

    //Call the function with the first letter and see if a division exists.
    //If there is more than one possible division, it returns the first one that it finds.
    if(can_divide(0, word, answer, trie -> root, empty_word)){
        for(auto w : answer) cout << w << " ";
    }
    else{
        cout << "There is no possible division" << "\n";
    }
}

int main(){

    vector<string> dictionary = {
        "Elf", "Manatee", "Quip", "Go", "Not", "Tee", 
        "Golf", "Note", "Teen", "Man", "Pig"
    };

    //string s = "mangolf";
    //string s = "manateenotelf";
    string s = "quipig";

    solve_wordBreak(dictionary, s);
}

//Time Spent: 25 minutes.