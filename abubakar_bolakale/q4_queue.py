class Node:
    # Time: O(1), Space: O(1)
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    # Time: O(1), Space: O(1)
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    # Time: O(1), Space: O(1)
    def isEmpty(self):
        return self.head is None

    # Time: O(1), Space: O(1)
    def peek(self):
        if self.isEmpty():
            raise IndexError("peek from empty queue")
        return self.head.value

    # Time: O(1), Space: O(1)
    def enqueue(self, x):
        new_node = Node(x)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    # Time: O(1), Space: O(1)
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("dequeue from empty queue")

        removed_value = self.head.value
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self._size -= 1
        return removed_value


q = Queue()

print(f"Test 1 - Is empty? {q.isEmpty()}")

q.enqueue(5)
q.enqueue(10)
q.enqueue(15)
print(f"Test 2 - Peek (should be 5): {q.peek()}")
print(f"Test 2 - Size (should be 3): {q._size}")

val1 = q.dequeue()
val2 = q.dequeue()
print(f"Test 3 - Dequeued first: {val1}")
print(f"Test 3 - Dequeued second: {val2}")
print(f"Test 3 - Current Peek (should be 15): {q.peek()}")

q.dequeue()
print(f"Test 4 - Is empty after 3 dequeues? {q.isEmpty()}")
print(f"Test 4 - Head is None? {q.head is None}")
print(f"Test 4 - Tail is None? {q.tail is None}")

print("Test 5 - Attempting to dequeue from empty queue:")
try:
    q.dequeue()
except IndexError as e:
    print(f"Success: Caught expected error -> {e}")

q.enqueue(100)
print(f"Test 6 - Re-fill Peek (should be 100): {q.peek()}")
