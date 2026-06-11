package Part1DataStructureImplementation;

import java.util.*;
//time spend about 30min
public class Trie {
    TrieNode root;
    public Trie(){
        root = new TrieNode();
    }
    private void insert(String word){
        TrieNode curr = root;
        for(char c: word.toCharArray()){
            int index = c- 'a';
            if(curr.children[index] == null){
                curr.children[index] = new TrieNode();
            }
            curr = curr.children[index];
        }
        curr.validWord = true;
    }
    private boolean isValidWord(String word){
        TrieNode curr = root;
        for(char c : word.toCharArray()){
            int index = c- 'a';
            if(curr.children[index]==null){
                return false;
            }
            curr = curr.children[index];
        }
        return curr.validWord;
    }
    private void remove(String word){
        if(!isValidWord(word)){
    return;
}
        TrieNode curr = root;
        List<TrieNode> path = new ArrayList<>();
        path.add(curr);
        for(char c: word.toCharArray()){
            int index = c-'a';
          
                 path.add(curr.children[index]);
                curr = curr.children[index];
            
           
         
            
        }

        curr.validWord = false;
        
        for(int i=path.size()-1;i>0;i--){
            TrieNode current = path.get(i);
            TrieNode parent = path.get(i-1);
            if(!current.validWord && noChildren(current)){
                int index = word.charAt(i-1) - 'a';
               parent.children[index] = null;
            }else{
                break;
            }
        }
    }
    private boolean noChildren(TrieNode current){
            for(TrieNode curr : current.children){
                if(curr!=null){
                    return false;
                }
            }
            return true;
        }
        public static void main(String[] args){
           
    Trie trie = new Trie();

    trie.insert("cat");
    trie.insert("car");
    trie.insert("care");
    trie.insert("dog");

    System.out.println(trie.isValidWord("cat"));   // true
    System.out.println(trie.isValidWord("car"));   // true
    System.out.println(trie.isValidWord("care"));  // true
    System.out.println(trie.isValidWord("ca"));    // false
    System.out.println(trie.isValidWord("dog"));   // true
    System.out.println(trie.isValidWord("do"));    // false
    System.out.println(trie.isValidWord("cow"));   // false

    trie.remove("care");

    System.out.println("After removing care:");
    System.out.println(trie.isValidWord("care"));  // false
    System.out.println(trie.isValidWord("car"));   // true
    System.out.println(trie.isValidWord("cat"));   // true

    trie.remove("car");

    System.out.println("After removing car:");
    System.out.println(trie.isValidWord("car"));   // false
    System.out.println(trie.isValidWord("cat"));   // true

    trie.remove("cat");

    System.out.println("After removing cat:");
    System.out.println(trie.isValidWord("cat"));   // false
    System.out.println(trie.isValidWord("dog"));   // true

    trie.remove("notthere");

    System.out.println("After removing word not in trie:");
    System.out.println(trie.isValidWord("dog"));   // true
}
        }


 class TrieNode{
    TrieNode[] children;
    boolean validWord;
    public TrieNode(){
        children = new TrieNode[26];
        validWord = false;
    }
}