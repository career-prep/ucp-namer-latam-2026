# Time Spent: 8 minutes

from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional[Node]

class Stack:
    def __init__(self):
        self.head: Optional[Node]

    # Returns the top item in the stack. O(1) time.

    def top(self) -> int:
        return self.head.data
    
    # Adds x to the top of the stack. O(1) time.
        
    def push(self, x: int) -> None:
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    # Removes and returns the top item in stack. O(1) time.

    def pop(self) -> int:
        val = self.head.data
        self.head = self.head.next
        return val
    
    # Returns a boolean indicating whether the stack is empty. O(1) time.

    def isEmpty(self) -> bool:
        return not self.head