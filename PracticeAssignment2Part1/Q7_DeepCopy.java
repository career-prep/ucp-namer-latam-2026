package PracticeAssignment2Part1;
public class Q7_DeepCopy {
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
     * my function goes through root node creates new Identicle node then
     * recursivly goes down the root node creating more identicle node and storing a copy;
     *       4
     *      / \     
           2   7

            copy - >  4  ->  4 ->   4
                            /      / \
                           2      2    7


    */    
    public Node deepCopy(Node root){
         if(root==null){
            return root;
        }
        Node newNode = new Node(root.data);
       
        newNode.left = deepCopy(root.left);
        
       newNode.right =deepCopy(root.right);
        return newNode;                                //2.right == null;
    }
    //time complexity o(n)
    //space complexity o(h) wehre h is height of tree;
    
}
