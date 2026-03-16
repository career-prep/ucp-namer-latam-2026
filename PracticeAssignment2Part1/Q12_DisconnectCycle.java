package PracticeAssignment2Part1;

import java.util.HashSet;
import java.util.Set;

public class Q12_DisconnectCycle {
    //if cycle found make end .next == null;
    //my approach is fast slow pointers to check for cycle
    //i didnt realize i wont know wahts the end if it is an cycle so i might need a List that stores seen node and then if current.next is seen thenn i make it null and return;
    class Node{
        int data;
        Node next;
        Node(int data){
            this.data = data;
            next = null;
        }
    }
    public Node disconnectCycle(Node root){
        if(root==null){
            return null;
        }
        Set<Node> seenList = new HashSet<>();
        Node current = root;
     
        while(current!=null && current.next!=null){
             seenList.add(current);
            if(seenList.contains(current.next)){
                current.next = null;
                return root;
            }
           
            current = current.next;
        }
        return root;
        
    }
    //space o(n) time o(n)
}
