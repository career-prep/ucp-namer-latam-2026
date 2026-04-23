class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None  
        self.tail = None  
        self.size = 0

    def peek(self):
        # returns the first item in the queue. O(1) time.
        if self.head is None:
            return None
        return self.head.data

    def enqueue(self, x):
        # adds x to the back of the queue. O(1) time.
        new_node = Node(x)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:   # first element
            self.head = new_node
        self.size += 1

    def dequeue(self):
        # removes and returns the first item in the queue. O(1) time.
        if self.head is None:
            return None
        val = self.head.data
        self.head = self.head.next
        if self.head is None:   
            self.tail = None
        self.size -= 1
        return val

    def isEmpty(self):
        # returns a boolean indicating whether the queue is empty. O(1) time.
        return self.head is None

if __name__ == "__main__":
    q = Queue()

    # isEmpty on empty queue
    print(q.isEmpty())   # True

    # enqueue some values
    q.enqueue(3)
    q.enqueue(7)
    q.enqueue(12)

    # peek should show front without removing it
    print(q.peek())      # 3

    # dequeue should return items in FIFO order
    print(q.dequeue())   # 3
    print(q.dequeue())   # 7
    print(q.isEmpty())   # False

    # dequeue last item, then check empty
    print(q.dequeue())   # 12
    print(q.isEmpty())   # True

    # dequeue from empty queue
    print(q.dequeue())   # None
    print(q.peek())      # None