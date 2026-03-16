package PracticeAssignment2Part1;

public class Q9_DedupeSortedArray {
    class Node{
        int data;
        Node next;

        Node(int data){
            this.data = data;
            next = null;
        }
    }
    /**
     *  i will have two pointers one at the start and one at the next index and i will loop though the list if i find two pointers to be equal i will 
     * increment the right pointer until its not equal. then i will set current.next to be the new unique node and then cahnge the node pointers acordingly!.
     * 
     * i used two while loop howveer since i will only be going in one direction the time is still o(n)
     * time o(n) space o(n)
     */
    public Node dedupeSortedList(Node root){
        if(root==null || root.next == null){
            return root;
        }
        Node current = root;
        Node fastNode = root.next;
        while(fastNode !=null){
            while(fastNode!=null && current.data == fastNode.data){ // added fastNode !=null because fastNode can be null during this loop
                fastNode = fastNode.next;
            }
                current.next = fastNode;

                current = fastNode;
                if(fastNode!=null){ // added this check becase fasNode can be null and fastNode.next might break the funciton;
                    fastNode = fastNode.next;
                }

        }
        return root;
    }
}
