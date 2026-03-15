package PracticeAssignment2Part1;

import java.util.ArrayList;
import java.util.List;

public class Q4_Queue {
     class Node{
        int data;
        Node next;

        public Node(int data){
            this.data = data;
            next = null;
        }
     }
     Node front;
     Node tail;

     public int peek(){
        if(front==null){
            return -1; // here i have put in -1 as throwing exception!
        }
        return front.data;
     }

     public void enqueue(int x){
        Node newNode = new Node(x);
        if(front==null){
            front = newNode;
        }else{
            tail.next = newNode;
            
        }
        tail = newNode;
        return;
     }
     public int dequeue(){
        if(front==null){
            return -1; //thorwing exception
        }
        Node deletedNode = front;
        Node newFront = front.next;
        if(newFront==null){
            tail = newFront;
        }
        front = newFront;
        return deletedNode.data;
     }
     public boolean isEmpty(){
        return front == null;
     }
}

