class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  

class Stack:
    def __init__(self):
        self.top_node = None

    # Time complexity: O(1)
    def push(self, x: int):
        node = Node(x)
        node.next = self.top_node
        self.top_node = node

    # Time complexity: O(1)
    def pop(self) -> int:
        if self.top_node is None:
            print("pop from empty stack")
            return None
        val = self.top_node.data
        self.top_node = self.top_node.next
        return val

    # Time complexity: O(1)
    def top(self) -> int:
        if self.top_node is None:
            print("top from empty stack")
            return None
        return self.top_node.data

    # Time complexity: O(1)
    def isEmpty(self) -> bool:
        return self.top_node is None
