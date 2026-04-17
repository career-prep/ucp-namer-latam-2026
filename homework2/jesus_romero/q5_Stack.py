class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):

        #Initialize top as None to represent an empty stack
        self.top_node = None

    def top(self): # Time, Space Complexities: O(1), O(1)

        #Return data from the top node if it exists
        if self.isEmpty():
            return None
        
        return self.top_node.data

    def push(self, x): # Time, Space Complexities: O(1), O(1)
        new_node = Node(x)
        #Link the new node to the current top and update the top
        new_node.next = self.top_node
        self.top_node = new_node

    def pop(self): # Time, Space Complexities: O(1), O(1)
        if self.isEmpty():
            return None
        #Retrieve top data and shift the top pointer to the next node
        data = self.top_node.data
        self.top_node = self.top_node.next

        return data

    def isEmpty(self): # Time, Space Complexities: O(1), O(1)
        #Stack is empty if top is None
        return self.top_node is None