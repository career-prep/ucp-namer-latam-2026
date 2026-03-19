# Question 5: Stack

# Implement a Stack class using a linked list as the underlying data structure.
# Supports O(1) insertion and deletion. Stores integers.

# Examples:

# push(1), push(2), push(3)
# top() -> 3
# pop() -> 3
# pop() -> 2
# isEmpty() -> False
# pop() -> 1
# isEmpty() -> True


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None  # top of stack

    def top(self):
        # Returns the top item in the stack
        if not self.head:
            return None
        return self.head.data
    # Time Complexity = O(1), Space Complexity = O(1)

    def push(self, x):
        # Adds x to the top of the stack
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
    # Time Complexity = O(1), Space Complexity = O(1)

    def pop(self):
        # Removes and returns the top item in the stack
        if not self.head:
            return None
        val = self.head.data
        self.head = self.head.next
        return val
    # Time Complexity = O(1), Space Complexity = O(1)

    def isEmpty(self):
        # Returns True if stack is empty
        return self.head is None
    # Time Complexity = O(1), Space Complexity = O(1)


# --- Tests ---

s = Stack()
print("isEmpty (initial):", s.isEmpty())   # True

s.push(1)
s.push(2)
s.push(3)
print("top:", s.top())                     # 3
print("isEmpty:", s.isEmpty())             # False

print("pop:", s.pop())                     # 3
print("pop:", s.pop())                     # 2
print("top:", s.top())                     # 1
print("isEmpty:", s.isEmpty())             # False

print("pop:", s.pop())                     # 1
print("isEmpty:", s.isEmpty())             # True
print("pop (empty):", s.pop())             # None
print("top (empty):", s.top())             # None

# Spent a total of 20 mins on this question
