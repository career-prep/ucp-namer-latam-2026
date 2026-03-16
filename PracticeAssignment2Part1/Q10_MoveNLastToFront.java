package PracticeAssignment2Part1;

public class Q10_MoveNLastToFront {
    class Node{
        int data;
        Node next;
        Node(int data){
            this.data = data;
            next = null;
        }
    }
    /**
     * my approach is first getting the size of the list -> caculating the nth node -> stoping one node before nth node -> then swaping nodes;
     * 
     * 
     * 
     * 
     */
    public Node moveNLastToFront(Node root, int n){
        if(root==null){
            return root;
        }
        int size = 0;
        Node current = root;
        while(current!=null){//gets size of the entire Node
            size++;
            current = current.next;
        }
        if(size==n){ // added this becase wihtout this case it would do unnecessary swaps
            return root;
        }
        size = size-n;
        current = root;
        for(int i=0;i<size-1;i++){//stops one node before nth node
            current = current.next;
        }
        Node firstNode = current.next; //stores the nth node
        current.next = firstNode.next;// removes the nth node from the root
        firstNode.next = root;// stored nth node is now pointing at the start of root
        root= firstNode; // makeing root equal firstNode;
        return root;
    }
    //time o(n) space o(1);
}
