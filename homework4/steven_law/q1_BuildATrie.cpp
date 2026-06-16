/*Data Structure: Trie
Algorithm: prefix tree — insert/search walk the path, remove unwinds + prunes dead nodes
Time Complexity: insert O(L), isValidWord O(L), remove O(L)   (L = word length)
Space Complexity: O(total chars inserted)
Time Taken: 35 mins 12 seconds
*/

#include<iostream>
#include<vector>
#include <string>

using namespace std;

/*
1. node = 26 children + validWord flag. root is an empty node.
2. insert: walk letter by letter, make the child if it doesnt exist, flag last node validWord.
3. isValidWord: walk the path, if any child missing return false, else return last->validWord.
4. remove: recurse to the end, unflag validWord, then on the way back delete any node that
   has no children AND isnt a word end. never delete root.
*/

struct TrieNode {
    vector<TrieNode*> children;
    bool validWord;
    TrieNode() : children(26, nullptr), validWord(false) {}
};

class Trie {
    TrieNode* root;

    //returns true if the caller should delete this node (no kids + not a word end)
    bool removeHelper(TrieNode* node, const string& word, int i){
        if(node == nullptr) return false;

        if(i == (int)word.size()){
            if(!node->validWord) return false; //word was never in the trie
            node->validWord = false;
        } else {
            int idx = word[i] - 'a';
            if(removeHelper(node->children[idx], word, i+1)){
                delete node->children[idx];
                node->children[idx] = nullptr;
            }
        }

        if(node->validWord) return false;
        for(auto& c : node->children) if(c != nullptr) return false;
        return node != root; //dont let root get deleted
    }

public:
    Trie() : root(new TrieNode()) {}

    void insert(string word){
        TrieNode* curr = root;
        for(char ch : word){
            int idx = ch - 'a';
            if(curr->children[idx] == nullptr) curr->children[idx] = new TrieNode();
            curr = curr->children[idx];
        }
        curr->validWord = true;
    }

    bool isValidWord(string word){
        TrieNode* curr = root;
        for(char ch : word){
            int idx = ch - 'a';
            if(curr->children[idx] == nullptr) return false;
            curr = curr->children[idx];
        }
        return curr->validWord;
    }

    void remove(string word){
        removeHelper(root, word, 0);
    }
};

int main(){
    Trie t;
    t.insert("cat");
    t.insert("car");
    t.insert("care");

    cout << boolalpha;
    cout << "isValidWord(cat)  expect true  -> " << t.isValidWord("cat")  << endl;
    cout << "isValidWord(ca)   expect false -> " << t.isValidWord("ca")   << endl;
    cout << "isValidWord(care) expect true  -> " << t.isValidWord("care") << endl;

    t.remove("car");
    cout << "after remove(car):" << endl;
    cout << "isValidWord(car)  expect false -> " << t.isValidWord("car")  << endl;
    cout << "isValidWord(care) expect true  -> " << t.isValidWord("care") << endl; //'car' path must survive
    cout << "isValidWord(cat)  expect true  -> " << t.isValidWord("cat")  << endl;
}

/* psudocode/thoughts/logic
goal: trie with insert, isValidWord (search), remove (and clean up unused nodes)
restraints: removing a word cant break other words that share its path (remove "car" must
keep "care" alive)

strategy: each node is 26 children + a validWord bool. insert/search are simple walks. remove
is the tricky one — recurse down, clear the validWord at the end, then on the unwind delete a
child only if its now empty (no children) and isnt itself a word end. the node != root guard
stops us from ever nuking the root.
*/
