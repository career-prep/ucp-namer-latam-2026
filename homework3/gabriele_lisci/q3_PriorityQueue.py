"""
Priority Queue Methods

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
class PriorityQueue:
    def __init__(self):
        self.arr = [(None, -float('inf'))]
        self.n = len(self.arr)

    def top(self):
        if self.n > 1:
            return self.arr[1][0]
        else:
            return None

    def rise(self, i):
        if i <=1:
            return
        if self.arr[i][1] < self.arr[i//2][1]:
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
            if right < self.n and self.arr[right][1] < self.arr[left][1]:
                smallest = right
            if self.arr[i][1] <= self.arr[smallest][1]:
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

    def printpq(self):
        print(self.arr)

pq = PriorityQueue()
pq2 = PriorityQueue()
pq3 = PriorityQueue()

# Generic Insert Test Case
pq.insert(("B", 2))
pq.insert(("E",6))
pq.insert(("F",7))
pq.insert(("C",4))
pq.insert(("D", 5))
pq.insert(("A", 1))
pq.printpq()

# Decreasing Order Insert Test Case
for i in range(5,-1,-1):
    pq2.insert((chr(i+65), i))
pq2.printpq()

# Generic Top Test Case
print(pq.top())
print(pq2.top())

# Empty pq Top Test Case
print(pq3.top())

# Generic Remove Test Case
pq.remove()
pq.printpq()
pq2.remove()
pq2.printpq()

# Empty Remove Test Case
pq3.remove()

# Time Spent: 10:00
