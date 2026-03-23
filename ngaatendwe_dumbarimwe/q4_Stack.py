class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class Stack:
    def _init_(self):
        self.head = None  

    def isEmpty(self):
        return self.head is None

    def push(self, x: int):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop from empty stack")
        
        removed_data = self.head.data
        self.head = self.head.next  
        return removed_data

    def top(self):
        if self.isEmpty():
            raise IndexError("Top from empty stack")
        return self.head.data