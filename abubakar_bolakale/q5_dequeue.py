class Node:
    # Time: O(1), Space: O(1)
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    # Time: O(1), Space: O(1)
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    # Time: O(1), Space: O(1)
    def isEmpty(self):
        return self.head is None

    # Time: O(1), Space: O(1)
    def front(self):
        if self.isEmpty():
            raise IndexError("front from empty deque")
        return self.head.value

    # Time: O(1), Space: O(1)
    def back(self):
        if self.isEmpty():
            raise IndexError("back from empty deque")
        return self.tail.value

    # Time: O(1), Space: O(1)
    def pushFront(self, x):
        new_node = Node(x)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1

    # Time: O(1), Space: O(1)
    def pushBack(self, x):
        new_node = Node(x)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    # Time: O(1), Space: O(1)
    def popFront(self):
        if self.isEmpty():
            raise IndexError("popFront from empty deque")
        
        removed_value = self.head.value
        self.head = self.head.next
        
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
            
        self._size -= 1
        return removed_value

    # Time: O(1), Space: O(1)
    def popBack(self):
        if self.isEmpty():
            raise IndexError("popBack from empty deque")
        
        removed_value = self.tail.value
        self.tail = self.tail.prev
        
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
            
        self._size -= 1
        return removed_value

dq = Deque()

print(f"Test 1 - Is empty? {dq.isEmpty()}")
print(f"Test 1 - Size: {dq._size}")

dq.pushFront(10)
dq.pushBack(20)
dq.pushFront(5)
print(f"Test 2 - Front (should be 5): {dq.front()}")
print(f"Test 2 - Back (should be 20): {dq.back()}")
print(f"Test 2 - Size (should be 3): {dq._size}")

val1 = dq.popFront()
print(f"Test 3 - popFront (should be 5): {val1}")
print(f"Test 3 - New Front (should be 10): {dq.front()}")
print(f"Test 3 - New Back (should be 20): {dq.back()}")
print(f"Test 3 - Size (should be 2): {dq._size}")

val2 = dq.popBack()
print(f"Test 4 - popBack (should be 20): {val2}")
print(f"Test 4 - Front/Back (should be 10): {dq.front()}, {dq.back()}")
print(f"Test 4 - Size (should be 1): {dq._size}")

dq.popFront()
print(f"Test 5 - Is empty after pops? {dq.isEmpty()}")
print(f"Test 5 - Head is None? {dq.head is None}")
print(f"Test 5 - Tail is None? {dq.tail is None}")
print(f"Test 5 - Size (should be 0): {dq._size}")

print("Test 6 - Attempting front/back on empty deque:")
try:
    dq.front()
except IndexError as e:
    print(f"Success: Caught expected error -> {e}")
try:
    dq.back()
except IndexError as e:
    print(f"Success: Caught expected error -> {e}")

print("Test 7 - Attempting popFront/popBack on empty deque:")
try:
    dq.popFront()
except IndexError as e:
    print(f"Success: Caught expected error -> {e}")
try:
    dq.popBack()
except IndexError as e:
    print(f"Success: Caught expected error -> {e}")

dq.pushBack(100)
print(f"Test 8 - Refill back/front (should be 100): {dq.back()}, {dq.front()}")
print(f"Test 8 - Size (should be 1): {dq._size}")