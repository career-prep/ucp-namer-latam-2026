"""
17 minutes
"""

class Queue:
    def __init__(self):
        self.queue = []
        self.count = 0

    def peek(self):
        if self.count > 0:
            return self.queue[0]
        
    def enqueue(self, val):
        self.queue.append(val)
        self.count += 1

    def dequeue(self):
        if self.count < 1:
            return None
        item = self.queue.pop(0)
        self.count -= 1
        return item

    def isEmpty(self):
        if self.count > 0:
            return False
        return True
