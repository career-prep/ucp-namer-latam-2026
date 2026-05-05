class PriorityQueue:
    def __init__(self):
        self.arr = []  # list of (string, int) pairs

    def top(self):
        # Returns the highest-priority (first) element
        return self.arr[0][0] if self.arr else None

    def insert(self, x, weight):
        # Adds string x with priority weight
        self.arr.append((x, weight))
        self._sift_up(len(self.arr) - 1)

    def remove(self):
        # Removes the highest-priority element
        if not self.arr:
            return
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        self.arr.pop()
        if self.arr:
            self._sift_down(0)

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.arr[i][1] > self.arr[parent][1]:  # max heap on weight
                self.arr[i], self.arr[parent] = self.arr[parent], self.arr[i]
                i = parent
            else:
                break

    def _sift_down(self, i):
        n = len(self.arr)
        while True:
            largest = i
            left, right = 2 * i + 1, 2 * i + 2
            if left < n and self.arr[left][1] > self.arr[largest][1]:
                largest = left
            if right < n and self.arr[right][1] > self.arr[largest][1]:
                largest = right
            if largest == i:
                break
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            i = largest


# Time: 20 min
