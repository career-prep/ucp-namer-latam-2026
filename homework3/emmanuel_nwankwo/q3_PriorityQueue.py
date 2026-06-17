class PriorityQueue:
    def __init__(self):
        self.arr = []

    def top(self):
        # return value with highest priority
        return self.arr[0][0]

    def insert(self, x, weight):
        # add new element
        self.arr.append((x, weight))
        self._heapify_up(len(self.arr) - 1)

    def remove(self):
        # remove root
        if not self.arr:
            return

        self.arr[0] = self.arr[-1]
        self.arr.pop()
        self._heapify_down(0)

    def _heapify_up(self, i):
        # move element up while its weight is greater than parent
        while i > 0:
            parent = (i - 1) // 2
            if self.arr[parent][1] >= self.arr[i][1]:
                break  # heap property fixed

            # swap if child has higher weight
            self.arr[parent], self.arr[i] = self.arr[i], self.arr[parent]
            i = parent

    def _heapify_down(self, i):
        n = len(self.arr)

        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i

            # find child with largest weight
            if left < n and self.arr[left][1] > self.arr[largest][1]:
                largest = left
            if right < n and self.arr[right][1] > self.arr[largest][1]:
                largest = right

            if largest == i:
                break  # heap property fixed

            # swap with larger child
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            i = largest