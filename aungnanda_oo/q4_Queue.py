# Question 4: Queue

# Implement a Queue class using a linked list as the underlying data structure.
# Supports O(1) insertion and deletion. Stores integers.

# Examples:

# enqueue(1), enqueue(2), enqueue(3)
# peek() -> 1
# dequeue() -> 1
# dequeue() -> 2
# isEmpty() -> False
# dequeue() -> 3
# isEmpty() -> True


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None  # front of queue
        self.tail = None  # back of queue

    def peek(self):
        # Returns the first item in the queue
        if not self.head:
            return None
        return self.head.data
    # Time Complexity = O(1), Space Complexity = O(1)

    def enqueue(self, x):
        # Adds x to the back of the queue
        new_node = Node(x)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    # Time Complexity = O(1), Space Complexity = O(1)

    def dequeue(self):
        # Removes and returns the first item in the queue
        if not self.head:
            return None
        val = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return val
    # Time Complexity = O(1), Space Complexity = O(1)

    def isEmpty(self):
        # Returns True if queue is empty
        return self.head is None
    # Time Complexity = O(1), Space Complexity = O(1)


# --- Tests ---

q = Queue()
print("isEmpty (initial):", q.isEmpty())   # True

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("peek:", q.peek())                   # 1
print("isEmpty:", q.isEmpty())             # False

print("dequeue:", q.dequeue())             # 1
print("dequeue:", q.dequeue())             # 2
print("peek:", q.peek())                   # 3
print("isEmpty:", q.isEmpty())             # False

print("dequeue:", q.dequeue())             # 3
print("isEmpty:", q.isEmpty())             # True
print("dequeue (empty):", q.dequeue())     # None
print("peek (empty):", q.peek())           # None

# Spent a total of 20 mins on this question
