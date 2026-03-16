package PracticeAssignment2Part1;

public class Q6_Deque {
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
    Node end;
    Node start;

    public int front(){
        if(start==null){
            return -1; //thorwing exception
        }
        return start.data;
    }
    public int back(){
        if(end==null){
            return -1;
        }
        return end.data;
    }
    public void pushBack(int x){
        Node newNode = new Node(x);
        if(end==null){
            end =newNode;
            start = newNode;
        }else{
            end.next = newNode;
            newNode.prev = end;
            end = newNode;
        }
    }
    public void pushFront(int x){
        Node newNode = new Node(x);
        if(start==null){
            start = newNode;
            end = newNode;
            return;
        }
        newNode.next = start;
        start.prev = newNode;
        start = newNode;
    }
    public int popFront(){
        if(start==null){
            return -1;
        }
        int popedVal = start.data;
        start = start.next;
        if(start ==null){
            end = null;
        }else{
            start.prev = null;
        }
        return popedVal;
        
    }
    public int popBack(){
        if(end==null){
            return -1;
        }
        Node deleteNode = end;
        
        end = end.prev;
        if(end == null){
            start = null;
        }else{
            end.next = null;
        }
        return deleteNode.data;
    }
    public boolean isEmpty(){
        return start==null;
    }
}
