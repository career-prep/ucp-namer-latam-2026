package PracticeAssignment2Part1;

public class Q2_DoubleLinkedList {
    public class Node{
        int data;

        Node next;
        Node prev;
        public Node(int data){
            this.data = data;
            this.next = null;
            this.prev = null;
        }
    }

    public Node insertAtFront(Node head,int val){
        Node firstNode = new Node(val);
        firstNode.next = head;
        head = firstNode;
        return head;
    }

    public Node insertAtBack(Node head,Node tail,int val){
        
        Node newNode = new Node(val);
        if(head==null){
            return newNode;
        }
        tail.next = newNode;
        return head;
       
    }
    public Node insertAfter(Node head,int val,Node loc){
        if(head==null || loc==null){
            return head;
        }
        Node nodeToBeAdded = new Node(val);
        Node temp = loc.next;
        loc.next = nodeToBeAdded;
        loc.next.next = temp;
        return head;
    }
    public Node insertBefore(Node head, int val , Node loc){
        Node nodeToBeAdded = new Node(val);
        Node temp = loc.prev;
        loc.prev = nodeToBeAdded;
        loc.prev.prev = temp;
        return head;

    }
    public Node deleteFront(Node head){
        if(head==null){
            return null;
        }
        return head.next;
    }
    public Node deleteBack(Node head,Node tail){
        if(head==null){
            return head;
        }
        tail  = tail.prev;
        tail.next = null;
        return head;
    }
    public Node deleteNode(Node head, Node loc){
        if(head==null){
            return head;
        }
        Node temp = loc.prev;
        temp.next = loc.next;
        return head;
       
        
       
    }
    public int length(Node head){
        int size = 0;
        Node current = head;
        while(current !=null){
            size++;
            current = current.next;
        }
        return size;
    }
    public Node reverseInterative(Node head){
        if(head==null){
            return head;
        }
        Node prev = null;
        Node current = head;
        while(current!=null){
            Node temp = current.next;
            current.next = prev;
            prev = current;
            current = temp;
        }
        return prev;
    }

    public Node reverseRecursive(Node head){
        if(head==null){
            return head;
        }
        Node prev = null;
        return helper(head,prev);
    }
    private Node helper(Node head, Node prev){
        if(head==null){
            return prev;
        }
        Node current = head;
        Node temp = current.next;
        current.next = prev;
        prev = current;
        current = temp;
        return helper(current,prev);
        

    }

}
