"""
Heap Methods

top()
    Time: O(1)
    Space: O(1)

insert(x)
    Time: O(logn)
    Space: O(1)

remove()
    Time: O(logn)
    Space: O(1)
"""
class Heap:
    def __init__(self):
        self.arr = [-float('inf')]
        self.n = len(self.arr)

    def top(self):
        if self.n > 1:
            return self.arr[1]
        else:
            return None

    def rise(self, i):
        if i <=1:
            return
        if self.arr[i] < self.arr[i//2]:
            self.arr[i], self.arr[i//2] = self.arr[i//2], self.arr[i]
            self.rise(i // 2)

    def insert(self, x):
        self.arr.append(x)
        self.n+=1
        self.rise(self.n-1)

    def sink(self, i):
        while 2*i < self.n:
            left = 2*i
            right = 2*i+1
            smallest = left
            if right < self.n and self.arr[right] < self.arr[left]:
                smallest = right
            if self.arr[i] <= self.arr[smallest]:
                break
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            i = smallest

    def remove(self):
        if self.n <= 1:
            return
        self.arr[1], self.arr[self.n-1] = self.arr[self.n-1], self.arr[1]
        self.arr.pop()
        self.n -= 1
        self.sink(1)

    def printHeap(self):
        print(self.arr)

heap = Heap()
heap2 = Heap()
heap3 = Heap()

# Generic Insert Test Case
heap.insert(2)
heap.insert(6)
heap.insert(7)
heap.insert(4)
heap.insert(5)
heap.insert(1)
heap.printHeap()

# Decreasing Order Insert Test Case
for i in range(5,-1,-1):
    heap2.insert(i)
heap2.printHeap()

# Generic Top Test Case
print(heap.top())
print(heap2.top())

# Empty Heap Top Test Case
print(heap3.top())

# Generic Remove Test Case
heap.remove()
heap.printHeap()
heap2.remove()
heap2.printHeap()

# Empty Remove Test Case
heap3.remove()

# Time Spent: 40:00
