class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class Queue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    # Time Complexity: O(1)
    def peek(self):
        if self.head is not None:
            return self.head.data
        return None

    # Time Complexity: O(1)
    def enqueue(self, x):
        temp = Node(x)
        if self.head is None:
            self.head = self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp

    # Time Complexity: O(1)
    def dequeue(self):
        if self.head is None:
            return None
        if self.head is self.tail:
            head_data = self.head.data
            self.head = self.tail = None
            return head_data
        head_data = self.head.data
        self.head = self.head.next
        return head_data

    # Time Complexity: O(1)
    def isEmpty(self):
        return self.head is None