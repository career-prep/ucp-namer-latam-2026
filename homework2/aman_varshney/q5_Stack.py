# spent 5 minutes

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        

class Stack:
    def __init__(self, head) -> None:
        self.head = head
        
    def top(self):
        """Returns top item. O(1)"""
        return self.head.data if self.head else None
    
    def push(self, x): 
        """Adds `x` to the stack. O(1)"""
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
        
    def pop(self):
        """Pops top item in stack. O(1)"""
        if not self.head: # empty case
            return None
        
        x = self.head.data
        self.head = self.head.next
        return x
        
    def isEmpty(self):
        """Returns true if the stack is empty. O(1) """
        return (self.head is None)


if __name__ == "__main__":
    # 1
    # empty stack
    s = Stack(None)
    assert s.isEmpty() is True, "empty isEmpty error"
    assert s.pop() is None, "empty pop error"


    # 2
    # push / LIFO order
    s.push(10)
    s.push(20)
    s.push(30)
    
    assert s.isEmpty() is False, "nonempty isEmpty error"
    assert s.top() == 30, "top error"
    assert s.pop() == 30, "pop 30 error"
    
    assert s.top() == 20, "top after pop error1"
    assert s.pop() == 20, "pop 20 error"
    
    assert s.top() == 10, "top after pop error2"
    assert s.pop() == 10, "pop 10 error"
    
    assert s.isEmpty() is True, "drained isEmpty error"
    assert s.pop() is None, "pop empty again error"
    assert s.top() is None, "top when empty error"


    print("All tests passed")
