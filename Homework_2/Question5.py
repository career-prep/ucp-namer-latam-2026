# Implement a Stack using a linked list with the following methods:
# top, push, pop, isEmpty.
# All operations should be O(1).

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def top(self):
        return self.head.data

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        val = self.head.data
        self.head = self.head.next
        return val

    def is_empty(self):
        return self.head is None


s = Stack()
print(s.is_empty())
s.push(1)
s.push(2)
s.push(3)
print(s.top())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.is_empty())

# top: O(1)
# push: O(1)
# pop: O(1)
# isEmpty: O(1)
# Spent 25 mins
