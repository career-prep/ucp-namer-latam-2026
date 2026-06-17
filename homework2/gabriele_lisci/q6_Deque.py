"""
DEQUE METHODS

front()
    Time: O(1)

back()
    Time: O(1)

pushFront(x)
    Time: O(1)

pushBack(x)
    Time: O(1)

popFront()
    Time: O(1)

popBack()
    Time: O(1)

isEmpty()
    Time: O(1)
"""

class DequeNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Deque:

    def __init__(self):
        self.head = None
        self.tail = None

    def front(self):
        if self.isEmpty():
            return None
        return self.head.data

    def back(self):
        if self.isEmpty():
            return None
        return self.tail.data

    def pushFront(self, x):
        node = DequeNode(x)

        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def pushBack(self, x):
        node = DequeNode(x)

        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def popFront(self):
        if self.isEmpty():
            return None

        val = self.head.data
        self.head = self.head.next

        if self.head:
            self.head.prev = None
        else:
            self.tail = None

        return val

    def popBack(self):
        if self.isEmpty():
            return None

        val = self.tail.data
        self.tail = self.tail.prev

        if self.tail:
            self.tail.next = None
        else:
            self.head = None

        return val

    def isEmpty(self):
        return self.head is None

def run_tests():
    dq = Deque()

    # Test initial state
    assert dq.isEmpty() == True
    assert dq.front() is None
    assert dq.back() is None

    # Test pushFront/front
    dq.pushFront(10)
    assert dq.front() == 10
    assert dq.back() == 10
    assert dq.isEmpty() == False

    # Test pushBack/back
    dq.pushBack(20)
    assert dq.front() == 10
    assert dq.back() == 20

    # Test multiple pushes
    dq.pushFront(5)
    dq.pushBack(30)
    # Deque should be [5, 10, 20, 30]
    assert dq.front() == 5
    assert dq.back() == 30
    print("push and front/back tests passed")

    # Test popFront
    assert dq.popFront() == 5
    assert dq.front() == 10

    # Test popBack
    assert dq.popBack() == 30
    assert dq.back() == 20
    print("popFront and popBack tests passed")

    # Test clearing the deque
    assert dq.popFront() == 10
    assert dq.popBack() == 20
    assert dq.isEmpty() == True
    assert dq.front() is None
    assert dq.back() is None
    print("emptying tests passed")

    # Test re-entry
    dq.pushBack(100)
    assert dq.front() == 100
    assert dq.popFront() == 100
    assert dq.isEmpty() == True
    print("re-entry tests passed")


run_tests()

# Time spent: 20:00
