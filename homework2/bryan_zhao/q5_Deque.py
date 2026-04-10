# Time Spent: 12 minutes

from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional[Node]
        self.prev: Optional[Node]

class Deque:
    def __init__(self):
        self.head: Optional[Node]
        self.tail: Optional[Node]

    # Returns the first item in the deque. O(1) time.

    def front(self) -> int:
        return self.head.data
    # Returns the last item in the deque. O(1) time.

    def back(self) -> int:
        return self.tail.data
    
    # Adds x to the back of the deque. O(1) time.
    
    def pushBack(self, x: int) -> None:
        new_node = Node(x)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
    # Adds x to the front of the deque. O(1) time.

    def pushFront(self, x: int) -> None:
        new_node = Node(x)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Removes and returns the first item in the deque. O(1) time.

    def popFront(self) -> int:
        val = self.head.data
        self.head = self.head.next

        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        
        return val
    
    # Removes and returns the last item in the deque. O(1) time.

    def popBack(self) -> int:
        val = self.tail.data
        self.tail = self.tail.prev

        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        
        return val

    # Returns a boolean indicating whether the deque is empty. O(1) time.

    def isEmpty(self) -> bool:
        return not self.head