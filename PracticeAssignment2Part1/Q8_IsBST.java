package PracticeAssignment2Part1;

import java.util.ArrayList;
import java.util.List;

public class Q8_IsBST {
     class Node{
        int data;
        Node left;
        Node right;

        Node(int data){
            this.data = data;
            left = null;
            right = null;
        }
    }
    /**
     * My approach:= i take the root check left sub tree and check right sub tree
     * if i find values violating the bst rule like root.left > root or root.right < root then i return false
     * other wise i recuirsivly go thought each node 
     * which is making the time complxity o(n) and space o(h) where h is the height of tree;
     * 
     * this approach failed for me because i failed to realize that checking only
     * immidiate childrren is not going to tell us if its valid binary search tree
     * 
     * My 2nd approach: Inorder traversal left root right which in bst means if i go through the treee
     * the values must be in asending order. 
     * i will store it in a list then comapre if we break the condition list(i) > list(i+1);
     * my time compelxity will still be o(n)  my space will be o(n+h) wehre h is the height of tree and n is the list i created which can be written as o(n);
     */
    
    public boolean isBST(Node root){
        if(root==null){
            return true;
        }
        List<Integer> NodeValList = new ArrayList<>();
        populateListFromBST(root,NodeValList);
        //checkes if the list is ascending or not;
        for(int i=0;i<NodeValList.size()-1;i++){
            if(NodeValList.get(i) >= NodeValList.get(i+1)){
                return false;
            }
        }
        return true;
    }
    private void populateListFromBST(Node root, List<Integer> NodeValList){
        if(root==null){
            return;
        }
        //inorder traversal goes to left store it in list then goes to right store it and recurse!
        populateListFromBST(root.left,NodeValList);
        NodeValList.add(root.data);
        populateListFromBST(root.right,NodeValList);
        
    }
    //time o(n) space o(n)
}
