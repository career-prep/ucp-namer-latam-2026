class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.front_node = None
        self.back_node = None

    # Time complexity: O(1)
    def pushFront(self, x: int):
        node = Node(x)
        if not self.front_node:  # empty deque
            self.front_node = self.back_node = node
        else:
            node.next = self.front_node
            self.front_node.prev = node
            self.front_node = node

    # Time complexity: O(1)
    def pushBack(self, x: int):
        node = Node(x)
        if not self.back_node:  # empty deque
            self.front_node = self.back_node = node
        else:
            node.prev = self.back_node
            self.back_node.next = node
            self.back_node = node

    # Time complexity: O(1)
    def popFront(self) -> int:
        if not self.front_node:
            print("popFront from empty deque")
            return None
        val = self.front_node.data
        self.front_node = self.front_node.next
        if self.front_node:
            self.front_node.prev = None
        else:
            self.back_node = None  # deque became empty
        return val

    # Time complexity: O(1)
    def popBack(self) -> int:
        if not self.back_node:
            print("popBack from empty deque")
            return None
        val = self.back_node.data
        self.back_node = self.back_node.prev
        if self.back_node:
            self.back_node.next = None
        else:
            self.front_node = None  # deque became empty
        return val

    # Time complexity: O(1)
    def front(self) -> int:
        if not self.front_node:
            print("front from empty deque")
            return None
        return self.front_node.data

    # Time complexity: O(1)
    def back(self) -> int:
        if not self.back_node:
            print("back from empty deque")
            return None
        return self.back_node.data

    # Time complexity: O(1)
    def isEmpty(self) -> bool:
        return self.front_node is None