class Heap:
    def __init__(self):
        self.arr = []

    def top(self):
        # return smallest element
        return self.arr[0]

    def insert(self, x):
        # add element at end
        self.arr.append(x)
        self._heapify_up(len(self.arr) - 1)

    def remove(self):
        # remove root by replacing with last element
        if not self.arr:
            return

        self.arr[0] = self.arr[-1]
        self.arr.pop()
        self._heapify_down(0)

    def _heapify_up(self, i):
        # move element at index i up until heap property is fixed
        while i > 0:
            parent = (i - 1) // 2
            if self.arr[parent] <= self.arr[i]:
                break  # heap property fixed

            # swap with parent if smaller
            self.arr[parent], self.arr[i] = self.arr[i], self.arr[parent]
            i = parent

    def _heapify_down(self, i):
        # move element at index i to th correct position
        n = len(self.arr)

        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            # find the smallest among node and children
            if left < n and self.arr[left] < self.arr[smallest]:
                smallest = left
            if right < n and self.arr[right] < self.arr[smallest]:
                smallest = right

            if smallest == i:
                break  # heap property fixed

            # swap with smaller child
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            i = smallest