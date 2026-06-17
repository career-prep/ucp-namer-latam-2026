# Time Spent: 16 minutes

from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional[Node]

class Queue:
    def __init__(self):
        self.head: Optional[Node]
        self.tail: Optional[Node]
    
    # Returns the first item in the queue. O(1) time.

    def peek(self) -> int:
        return self.head.data
    
    # Adds x to the tail of the queue. O(1) time.

    def enqueue(self, x: int) -> None:
        new_node = Node(x)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    # Removes and returns the first item in the queue. O(1) time.

    def dequeue(self) -> int:
        val = self.head.data
        self.head = self.head.next

        if not self.head:
            self.tail = None
        
        return val
    
    # Returns a boolean indicating whether the queue is empty. O(1) time.

    def isEmpty(self) -> bool:
        return not self.head