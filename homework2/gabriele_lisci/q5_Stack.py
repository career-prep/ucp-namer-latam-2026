"""
STACK METHODS

peek()
    Time: O(1)

push(x)
    Time: O(1)

pop()
    Time: O(1)

isEmpty()
    Time: O(1)
"""


class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.head = None

    def peek(self):
        return self.head.data

    def push(self, x):
        newNode = StackNode(x)
        newNode.next = self.head
        self.head = newNode

    def pop(self):
        val = self.head.data
        self.head = self.head.next
        return val

    def isEmpty(self):
        return self.head is None

def run_tests():
    s = Stack()

    # Test isEmpty on new stack
    assert s.isEmpty() == True

    # Test Push
    s.push(10)
    s.push(20)
    s.push(30)
    assert s.isEmpty() == False
    assert s.peek() == 30
    print("push/peek passed")

    # Test Pop
    assert s.pop() == 30
    assert s.peek() == 20
    assert s.pop() == 20
    assert s.pop() == 10
    assert s.isEmpty() == True
    print("pop passed")

    # Test Re-entry after emptying
    s.push(100)
    assert s.peek() == 100
    assert s.isEmpty() == False
    assert s.pop() == 100
    assert s.isEmpty() == True
    print("re-entry passed")


run_tests()

# Time spent: 20:00
