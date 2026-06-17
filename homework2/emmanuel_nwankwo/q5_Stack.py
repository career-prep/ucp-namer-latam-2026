class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class Stack:
    def __init__(self, head=None):
        self.head = head

    # Time Complexity: O(1)
    def top(self):
        if self.head is None:
            return None
        return self.head.data

    # Time Complexity: O(1)
    def push(self, x):
        self.head = Node(x, self.head)

    # Time Complexity: O(1)
    def pop(self):
        if self.head is None:
            return None
        else:
            head_data = self.head.data
            self.head = self.head.next
            return head_data

    # Time Complexity: O(1)
    def isEmpty(self):
        return self.head is None