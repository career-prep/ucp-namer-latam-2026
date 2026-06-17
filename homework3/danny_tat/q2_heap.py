class Heap:
    def __init__(self):
        self.arr = []

    def top(self):
        # Returns the min (top) element
        return self.arr[0] if self.arr else None

    def insert(self, x):
        # Adds x to the heap in the correct position
        self.arr.append(x)
        self._sift_up(len(self.arr) - 1)

    def remove(self):
        # Removes the min (top) element
        if not self.arr:
            return
        # Swap root with last element, then sift down
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        self.arr.pop()
        if self.arr:
            self._sift_down(0)

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.arr[i] < self.arr[parent]:
                self.arr[i], self.arr[parent] = self.arr[parent], self.arr[i]
                i = parent
            else:
                break

    def _sift_down(self, i):
        n = len(self.arr)
        while True:
            smallest = i
            left, right = 2 * i + 1, 2 * i + 2
            if left < n and self.arr[left] < self.arr[smallest]:
                smallest = left
            if right < n and self.arr[right] < self.arr[smallest]:
                smallest = right
            if smallest == i:
                break
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            i = smallest

# Time: 40 min
