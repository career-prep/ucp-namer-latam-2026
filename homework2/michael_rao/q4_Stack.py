class Stack:
    def __init__(self):
        self.arr = []

    def top(self):
        if not self.arr:
            return None
        return self.arr[-1]
    # time: O(1)

    def push(self, x):
        self.arr.append(x)
    # time: O(1)

    def pop(self):
        if not self.arr:
            return None
        return self.arr.pop()
    # time: O(1)

    def isEmpty(self):
        return not self.arr
    # time: O(1)