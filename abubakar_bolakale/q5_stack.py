class Node:
    # Time: O(1), Space: O(1)
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    # Time: O(1), Space: O(1)
    def __init__(self):
        self.head = None
        self._size = 0

    # Time: O(1), Space: O(1)
    def isEmpty(self):
        return self.head is None

    # Time: O(1), Space: O(1)
    def top(self):
        if self.isEmpty():
            raise IndexError("top from empty stack")
        return self.head.value

    # Time: O(1), Space: O(1)
    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    # Time: O(1), Space: O(1)
    def pop(self):
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        
        removed_value = self.head.value
        self.head = self.head.next
        self._size -= 1
        return removed_value


s = Stack()

print(f"Test 1 - Is empty? {s.isEmpty()}")

s.push(10)
s.push(20)
s.push(30)
print(f"Test 2 - Top (should be 30): {s.top()}")
print(f"Test 2 - Size (should be 3): {s._size}")

val1 = s.pop()
print(f"Test 3 - Popped (should be 30): {val1}")
print(f"Test 3 - New Top (should be 20): {s.top()}")

s.pop()
s.pop()
print(f"Test 4 - Is empty? {s.isEmpty()}")

print("Test 5 - Attempting to pop from empty stack:")
try:
    s.pop()
except IndexError as e:
    print(f"Success: Caught expected error -> {e}")

s.push(500)
print(f"Test 6 - Re-fill Top (should be 500): {s.top()}")