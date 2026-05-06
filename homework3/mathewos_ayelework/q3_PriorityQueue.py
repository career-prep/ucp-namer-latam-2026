# Priority queue backed by a max heap of (element, priority) pairs
# Comparisons use the priority weight; elements are returned in priority order


class PriorityQueue:
    def __init__(self):
        self.arr = []

    def top(self):  # O(1)
        if not self.arr:
            return None
        return self.arr[0][0]

    def insert(self, x, weight):  # O(log n)
        self.arr.append((x, weight))
        self._bubbleUp(len(self.arr) - 1)

    def remove(self):  # O(log n)
        if not self.arr:
            return
        last = self.arr.pop()
        if self.arr:
            self.arr[0] = last
            self._bubbleDown(0)

    def _bubbleUp(self, i):  # O(log n)
        while i > 0:
            parent = (i - 1) // 2
            if self.arr[i][1] > self.arr[parent][1]:
                self.arr[i], self.arr[parent] = self.arr[parent], self.arr[i]
                i = parent
            else:
                return

    def _bubbleDown(self, i):  # O(log n)
        n = len(self.arr)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i
            if left < n and self.arr[left][1] > self.arr[largest][1]:
                largest = left
            if right < n and self.arr[right][1] > self.arr[largest][1]:
                largest = right
            if largest == i:
                return
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            i = largest


print("PriorityQueue Results:")

pq = PriorityQueue()
pq.insert("low", 1)
pq.insert("urgent", 10)
pq.insert("medium", 5)
pq.insert("highest", 20)
pq.insert("normal", 3)

print(pq.top())
pq.remove()
print(pq.top())
pq.remove()
print(pq.top())

pq.insert("brand new top", 100)
print(pq.top())

pq.remove()
pq.remove()
pq.remove()
pq.remove()
print(pq.top())

empty = PriorityQueue()
print(empty.top())
empty.remove()
print(empty.top())
