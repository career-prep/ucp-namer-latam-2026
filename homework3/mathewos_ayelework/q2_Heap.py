# Min heap backed by an array (binary heap, parent at (i-1)//2, children at 2i+1 and 2i+2)


class Heap:
    def __init__(self):
        self.arr = []

    def top(self):  # O(1)
        if not self.arr:
            return None
        return self.arr[0]

    def insert(self, x):  # O(log n)
        self.arr.append(x)
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
            if self.arr[i] < self.arr[parent]:
                self.arr[i], self.arr[parent] = self.arr[parent], self.arr[i]
                i = parent
            else:
                return

    def _bubbleDown(self, i):  # O(log n)
        n = len(self.arr)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < n and self.arr[left] < self.arr[smallest]:
                smallest = left
            if right < n and self.arr[right] < self.arr[smallest]:
                smallest = right
            if smallest == i:
                return
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            i = smallest


print("Heap Results:")

h = Heap()
for v in [5, 3, 8, 1, 9, 2, 7]:
    h.insert(v)

print(h.top())
print(h.arr)

h.remove()
print(h.top())

h.remove()
print(h.top())

h.insert(0)
print(h.top())

h.insert(-4)
print(h.top())

empty = Heap()
print(empty.top())
empty.remove()
print(empty.top())
