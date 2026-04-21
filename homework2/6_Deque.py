class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.front_node = None
        self.back_node = None

    def front(self):
        if not self.front_node:
            return None
        return self.front_node.data

    def back(self):
        if not self.back_node:
            return None
        return self.back_node.data

    def pushFront(self, x):
        new_node = Node(x)

        if not self.front_node:
            self.front_node = self.back_node = new_node
            return

        new_node.next = self.front_node
        self.front_node.prev = new_node
        self.front_node = new_node

    def pushBack(self, x):
        new_node = Node(x)

        if not self.back_node:
            self.front_node = self.back_node = new_node
            return

        self.back_node.next = new_node
        new_node.prev = self.back_node
        self.back_node = new_node

    def popFront(self):
        if not self.front_node:
            return None

        val = self.front_node.data
        self.front_node = self.front_node.next

        if self.front_node:
            self.front_node.prev = None
        else:
            self.back_node = None

        return val

    def popBack(self):
        if not self.back_node:
            return None

        val = self.back_node.data
        self.back_node = self.back_node.prev

        if self.back_node:
            self.back_node.next = None
        else:
            self.front_node = None

        return val

    def isEmpty(self):
        return self.front_node is None