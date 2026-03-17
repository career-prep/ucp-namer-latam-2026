package PracticeAssignment2Part1;

public class Q14_FloorInBST {
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
     * my approach is to solve it recursivly. I plan to have a helper method that get passed in the root,target and a min(floor) vairabel
     * then i will use binary search and traverse thorugh my tree and keep sotring min in a variable.
     * time o(log n) can be o(n) worst case space o(h) height of tree;
     * 
     */
    public int floorInBst(Node root,int target){
        
        if(root==null){
            return -1; // thorwing exception
        }
            
        return helper(root,target,-1);
               
     
    }
    private int helper(Node root,int target,int min){
        if(root==null){
            return min;
        }
        if(root.data <= target && root.data > min){ // keeps track of min
            min = root.data;
        }
        if(root.data > target){ //if node is grater then target we go left
            return helper(root.left,target,min);
        }else{ // else we go right
            return helper(root.right,target,min);
        }


    }
}
