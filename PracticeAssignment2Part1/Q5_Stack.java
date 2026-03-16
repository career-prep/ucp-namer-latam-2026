package PracticeAssignment2Part1;

public class Q5_Stack {
    class Node{
        int data;
        Node next;
        Node prev;
        public Node(int data){
            this.data = data;
            next = null;
            prev = null;
        }
    }
    Node topStack;
    public int top(){
        if(topStack==null){
            return -1;// throwing exception

        }
        return topStack.data;
    }
    public void push(int x){
        Node newNode = new Node(x);
        if(topStack==null){
            topStack = newNode;
        }else{
            newNode.prev = topStack;
            topStack.next = newNode;
            topStack = newNode;
        }
        return;
    }
    public int pop(){
        if(topStack==null){
            return -1; // thorwing exception
        }
        Node newNode = topStack;
        topStack = topStack.prev;
        return newNode.data;
        
    }
    public boolean isEmpty(){
        return topStack == null;
    }


}
