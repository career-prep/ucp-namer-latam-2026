class Queue:
    def __init__(self):
        self.q = []

    def peek(self):
        if len(self.q) == 0:
            return -1
        return self.q[0]

    def enqueue(self, x):
        self.q.append(x)

    def dequeue(self):
        if len(self.q) == 0:
            return -1
        x = self.q[0]
        self.q.pop(0)
        return x

    
    def isEmpty(self):
        return len(self.q) == 0
    
q = Queue()

# Test 1: isEmpty on new queue
print(q.isEmpty())       # True

# Test 2: enqueue and peek
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.peek())          # 10 (first in)

# Test 3: dequeue returns front
print(q.dequeue())       # 10
print(q.dequeue())       # 20

# Test 4: peek after dequeue
print(q.peek())          # 30

# Test 5: isEmpty when not empty
print(q.isEmpty())       # False

# Test 6: dequeue last item
print(q.dequeue())       # 30

# Test 7: isEmpty after all removed
print(q.isEmpty())       # True

# Test 8: dequeue on empty queue
print(q.dequeue())       # -1

# Test 9: peek on empty queue
print(q.peek())          # -1