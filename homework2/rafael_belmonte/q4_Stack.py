# Data Structure Implementation: Stack (using singly linked list)
# time complexity per method noted inline
# 10 minutes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None  # top of stack

    def top(self):  # O(1)
        if not self.head:
            return None
        return self.head.data

    def push(self, x):  # O(1)
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def pop(self):  # O(1)
        if not self.head:
            return None
        val = self.head.data
        self.head = self.head.next
        return val

    def isEmpty(self):  # O(1)
        return self.head is None

# test cases
s = Stack()
assert s.isEmpty() == True
assert s.pop() is None

s.push(1)
s.push(2)
s.push(3)
assert s.top() == 3
assert s.isEmpty() == False

assert s.pop() == 3
assert s.pop() == 2
assert s.top() == 1
assert s.pop() == 1
assert s.isEmpty() == True

print("yay!!")
