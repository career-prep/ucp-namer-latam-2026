"""
5 minutes
"""


class Stack:
    def __init__(self):
        self.stack = []
        self.count = 0

    def top(self):
        if self.count > 0:
            return self.stack[-1]
        
    def push(self, val):
        self.stack.append(val)
        self.count += 1

    def pop(self):
        if self.count < 1:
            return None
        item = self.stack.pop(-1)
        self.count -= 1
        return item

    def isEmpty(self):
        if self.count > 0:
            return False
        return True
