"""
QUEUE METHODS

peek()
    Time: O(1)
    Space: O(1)

enqueue(x)
    Time: O(1)
    Space: O(1)

dequeue()
    Time: O(1)
    Space: O(1)

isEmpty()
    Time: O(1)
    Space: O(1)
"""

class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.frontNode = None
        self.backNode = None

    def peek(self):
        return self.frontNode.data

    def enqueue(self, x):
        newNode = QueueNode(x)

        if self.backNode:
            self.backNode.next = newNode
        else:
            self.frontNode = newNode

        self.backNode = newNode

    def dequeue(self):
        val = self.frontNode.data
        self.frontNode = self.frontNode.next

        if self.frontNode is None:
            self.backNode = None

        return val

    def isEmpty(self):
        return self.frontNode is None

def run_tests():
    q = Queue()

    # Test isEmpty on new queue
    assert q.isEmpty() == True

    # Test Enqueue
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    assert q.isEmpty() == False
    assert q.peek() == 10
    print("enqueue/peek passed")

    # Test Dequeue
    assert q.dequeue() == 10
    assert q.peek() == 20
    assert q.dequeue() == 20
    assert q.dequeue() == 30
    assert q.isEmpty() == True
    print("dequeue passed")

    # Test Re-entry after emptying
    q.enqueue(40)
    assert q.peek() == 40
    assert q.isEmpty() == False
    assert q.dequeue() == 40
    assert q.isEmpty() == True
    print("re-entry passed")


run_tests()

# Time spent: 20:00
