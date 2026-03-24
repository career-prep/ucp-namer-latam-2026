class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def top(self):
        # returns the top item in the stack. O(1) time.
        if self.head is None:
            return None
        return self.head.data

    def push(self, x):
        # adds x to the top of the stack. O(1) time.
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        # removes and returns the top item in the stack. O(1) time.
        if self.head is None:
            return None
        val = self.head.data
        self.head = self.head.next
        self.size -= 1
        return val

    def isEmpty(self):
        # returns a boolean indicating whether the stack is empty. O(1) time.
        return self.head is None


if __name__ == "__main__":
    s = Stack()

    # isEmpty on empty stack
    print(s.isEmpty())   # True

    # push some values
    s.push(3)
    s.push(7)
    s.push(12)

    # top should show front without removing it
    print(s.top())       # 12

    # pop should return items in LIFO order
    print(s.pop())       # 12
    print(s.pop())       # 7
    print(s.isEmpty())   # False

    # pop last item, then check empty
    print(s.pop())       # 3
    print(s.isEmpty())   # True

    # pop from empty stack
    print(s.pop())       # None
    print(s.top())       # None
