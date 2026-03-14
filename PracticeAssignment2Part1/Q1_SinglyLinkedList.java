package PracticeAssignment2Part1;

 
public class Q1_SinglyLinkedList {
   public class Node{
        int data;

        Node next;
        public Node(int data){
            this.data = data;
            this.next = null;
        }
    }

    public Node insertAtFront(Node head,int val){
        Node firstNode = new Node(val);
        firstNode.next = head;
        head = firstNode;
        return head;
    }

    public Node insertAtBack(Node head,int val){
         Node newNode = new Node(val);
        if(head==null){
            return newNode;
        }
        Node current = head;
        while(current.next!=null){
            current = current.next;
        }
        current.next = newNode;
        return head;
       
    }
    public Node insertAfter(Node head,int val,Node loc){
       
        Node nodeToBeAdded = new Node(val);
        Node current = head;
        while(current!=null){
            if(current==loc){
                Node temp = current.next;
                current.next = nodeToBeAdded;
                current.next.next = temp;
                return head;
            }
            current = current.next;
        }
        return head;
    }
    public Node insertBefore(Node head, int val , Node loc){
        Node nodeToBeAdded = new Node(val);
        Node current = head;
        Node prev = null;
        while(current!=null){
            if(current ==loc){
                if(prev!=null){
                    prev.next = nodeToBeAdded;
                    prev.next.next = current;
                }else{
                    nodeToBeAdded.next = current;
                    head = nodeToBeAdded;
                }
                
                return head;
            }
            prev = current;
            current = current.next;
        }
        return head;
    }
    public Node deleteFront(Node head){
        if(head==null){
            return null;
        }
        return head.next;
    }
    public Node deleteBack(Node head){
        if(head==null){
            return head;
        }
        if(head.next ==null){
            return head.next;
        }
        Node prev = null;
        Node current = head;
        while(current.next!=null){
            prev = current;
            current = current.next;
        }
        
            prev.next = null;
        


        
        return head;
    }
    public Node deleteNode(Node head, Node loc){
        Node current = head;
        Node prev = null;
        while(current!=null){
            if(current == loc){
                if(prev!=null){
                    prev.next = current.next;
                    return head;
                }else{
                    return head.next;
                }
            }
             prev = current;
            current = current.next;
        }
       
        
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
