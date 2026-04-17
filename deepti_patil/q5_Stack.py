class Stack:
    # push and pop both happen at the front so this is O(1) with any linked list
    def __init__(self):
        self.head = None  # top of stack
 
    # Time: O(1)
    def top(self):
        if self.head is None:
            return None
        return self.head.data
 
    # push to front
    # Time: O(1)
    def push(self, x):
        new_node = SinglyNode(x)
        new_node.next = self.head
        self.head = new_node
 
    # pop from front
    # Time: O(1)
    def pop(self):
        if self.head is None:
            return None
        val = self.head.data
        self.head = self.head.next
        return val
 
    # Time: O(1)
    def isEmpty(self):
        return self.head is None
