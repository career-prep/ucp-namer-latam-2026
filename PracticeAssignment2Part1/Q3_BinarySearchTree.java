package PracticeAssignment2Part1;

public class Q3_BinarySearchTree {
    
    private Node root;

    public int min(){
        
        Node current = root;
        if(current==null){
            return -1;
        }
        while(current.left !=null){
            current = current.left;
        }
        return current.data;
    }
    public int max(){
        Node current = root;
        if(current==null){
            return -1;
        }
        while(current.right!=null){
            current = current.right;
        }
        return current.data;
    }
    public boolean contains(int val){
        Node current = root;
        
        if(current==null){
            return false;
        }
        while(current!=null){
             if(current.data == val){
            return true;
        }else if(current.data <val){
            current =current.right;
        }else{
            current = current.left;
        }
        }
        return false;
       
    }
    public void insert(int val){
        Node current = root;
        Node nodeToBeAdded = new Node(val);
        if(current==null){
            root = nodeToBeAdded;
        }else{
            insertHelper(current,nodeToBeAdded);
        }
        

    }
    private void insertHelper(Node current, Node nodeToBeAdded){
        
        if(current.data > nodeToBeAdded.data){
            if(current.left==null){
                current.left = nodeToBeAdded;
                return;
            }
             insertHelper(current.left, nodeToBeAdded);

        }else{
            if(current.right==null){
                current.right = nodeToBeAdded;
                return;
            }
            insertHelper(current.right, nodeToBeAdded);
        }
       

    }
   

}
class Node{
        int data;
        Node left;
        Node right;

        public Node(int data){
            this.data = data;
            left = null;
            right = null;
        }
    }