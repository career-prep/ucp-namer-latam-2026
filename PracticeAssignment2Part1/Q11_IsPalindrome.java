package PracticeAssignment2Part1;

public class Q11_IsPalindrome {
    /**
     * 
     * assuming tail node is not provided!
     */
    class Node{
        int data;
        Node next;
        Node prev;
        Node(int data){
            this.data = data;
            next =null;
            prev = null;
        }
    }
    /**
     * i will have two pointer one at the front and one at the end. Since its a doubly linked list i can go both ways.
     * i will check if front does not equal end if that conidtion is true i return false.
     * for odd length i can check if both pointers are equal and exit the loop
     * for even length i have added another check checking if the next pointer for front in the end node. this prevents skip when the lsit size is even;
     * time o(n) space o(1)
     * 
     */
    public boolean isPalindrome(Node root){
        if(root==null){
            return true;
        }
        Node tailNode = root;
        while(tailNode.next!=null){
            tailNode = tailNode.next;
        }
        Node frontNode = root;
        while(frontNode != tailNode &&frontNode.next != tailNode){ //second check is so for even size it doesnt skip both pointer;
            if(frontNode.data != tailNode.data){
                return false;
            }
            frontNode = frontNode.next;
            tailNode = tailNode.prev;
        }
        return true;
    }
}
