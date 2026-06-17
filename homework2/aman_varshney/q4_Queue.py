# spent 15 minutes

class Node: 
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.head = None # front
        self.tail = None # back
        
    def peek(self): 
        """Returns first element on top. O(1)"""
        return self.head.data if self.head else None
    
    def enqueue(self, x): 
        """Adds x to the back of the queue. O(1)"""
        # create new node
        new_node = Node(x)
        
        # link
        if not self.tail: # empty case
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
    def dequeue(self):
        """Pops the first item from the queue. O(1)"""
        if not self.head:
            return None # empty case
        
        x = self.head.data
        self.head = self.head.next # update head
        
        if not self.head: # one element case
            self.tail = None
            
        return x
        
    def isEmpty(self):
        return (self.head is None)


if __name__ == "__main__":
    # 1
    # empty queue
    q = Queue()
    assert q.isEmpty() is True, "empty isEmpty error"
    assert q.peek() is None, "empty peek error"
    assert q.dequeue() is None, "empty dequeue error"


    # 2
    # enqueue / FIFO order
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    
    assert q.isEmpty() is False, "nonempty isEmpty error"
    assert q.peek() == 1, "peek error"
    assert q.head.data == 1, "head error1"
    assert q.tail.data == 3, "tail error1"
    assert q.dequeue() == 1, "dequeue 1 error"
    
    assert q.peek() == 2, "peek after dequeue error1"
    assert q.head.data == 2, "head error2"
    assert q.tail.data == 3, "tail error2"
    assert q.dequeue() == 2, "dequeue 2 error"
    
    assert q.peek() == 3, "peek after dequeue error2"
    assert q.head.data == 3, "head error3"
    assert q.tail.data == 3, "tail error3"
    assert q.dequeue() == 3, "dequeue 3 error"
    
    assert q.peek() is None, "empty peek after dequeue error"
    assert q.isEmpty() is True, "drained isEmpty error"
    assert q.dequeue() is None, "dequeue empty again error"


    print("All tests passed")
