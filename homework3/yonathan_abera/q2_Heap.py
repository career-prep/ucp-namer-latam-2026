# Data Structure: Heap (min heap, array-based)
# Time Complexity: top() O(1), insert() O(log n), remove() O(log n)
# Space Complexity: O(n)

class Heap:
    def __init__(self):
        self.arr = []

    def top(self):
        if not self.arr:
            return None
        return self.arr[0]

    def insert(self, x):
        self.arr.append(x)
        self._bubble_up(len(self.arr) - 1)

    def remove(self):
        if not self.arr:
            return
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        if self.arr:
            self._sift_down(0)

    def _bubble_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.arr[parent] > self.arr[idx]:
                self.arr[parent], self.arr[idx] = self.arr[idx], self.arr[parent]
                idx = parent
            else:
                break

    def _sift_down(self, idx):
        n = len(self.arr)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx
            if left < n and self.arr[left] < self.arr[smallest]:
                smallest = left
            if right < n and self.arr[right] < self.arr[smallest]:
                smallest = right
            if smallest != idx:
                self.arr[smallest], self.arr[idx] = self.arr[idx], self.arr[smallest]
                idx = smallest
            else:
                break


h = Heap()
for val in [5, 3, 8, 1, 4, 2]:
    h.insert(val)
print(h.top()) 

sorted_vals = []
while h.arr:
    sorted_vals.append(h.top())
    h.remove()
print(sorted_vals)

# Time spent: ~35 minutes
