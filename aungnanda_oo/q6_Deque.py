# Question 6: Deque (Double-Ended Queue)

# Implement a Deque class with O(1) insertion and deletion at both ends.
# Uses a doubly linked list as the underlying data structure. Stores integers.

# Examples:

# pushBack(1), pushBack(2), pushBack(3)
# front() -> 1
# back() -> 3
# pushFront(0)
# front() -> 0
# popFront() -> 0
# popBack() -> 3
# front() -> 1, back() -> 2
# isEmpty() -> False
# popFront(), popFront()
# isEmpty() -> True


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.head = None  # front of deque
        self.tail = None  # back of deque

    def front(self):
        # Returns the first item in the deque
        if not self.head:
            return None
        return self.head.data
    # Time Complexity = O(1), Space Complexity = O(1)

    def back(self):
        # Returns the last item in the deque
        if not self.tail:
            return None
        return self.tail.data
    # Time Complexity = O(1), Space Complexity = O(1)

    def pushBack(self, x):
        # Adds x to the back of the deque
        new_node = Node(x)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    # Time Complexity = O(1), Space Complexity = O(1)

    def pushFront(self, x):
        # Adds x to the front of the deque
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    # Time Complexity = O(1), Space Complexity = O(1)

    def popFront(self):
        # Removes and returns the first item in the deque
        if not self.head:
            return None
        val = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return val
    # Time Complexity = O(1), Space Complexity = O(1)

    def popBack(self):
        # Removes and returns the last item in the deque
        if not self.tail:
            return None
        val = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return val
    # Time Complexity = O(1), Space Complexity = O(1)

    def isEmpty(self):
        # Returns True if deque is empty
        return self.head is None
    # Time Complexity = O(1), Space Complexity = O(1)


# --- Tests ---

d = Deque()
print("isEmpty (initial):", d.isEmpty())   # True

d.pushBack(1)
d.pushBack(2)
d.pushBack(3)
print("front:", d.front())                 # 1
print("back:", d.back())                   # 3

d.pushFront(0)
print("front after pushFront(0):", d.front())  # 0
print("back:", d.back())                        # 3

print("popFront:", d.popFront())           # 0
print("front:", d.front())                 # 1

print("popBack:", d.popBack())             # 3
print("back:", d.back())                   # 2

print("isEmpty:", d.isEmpty())             # False

print("popFront:", d.popFront())           # 1
print("popFront:", d.popFront())           # 2
print("isEmpty:", d.isEmpty())             # True
print("popFront (empty):", d.popFront())   # None
print("popBack (empty):", d.popBack())     # None

# Spent a total of 20 mins on this question
