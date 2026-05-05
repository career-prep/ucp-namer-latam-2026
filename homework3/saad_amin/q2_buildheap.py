class MinHeap:
    def __init__(self):
        self.arr = []

    def top(self):
        
        if not self.arr:
            return None
        
        return self.arr[0]

    def insert(self, x):
        
        self.arr.append(x)
        self.heapify_up(len(self.arr) - 1)

    def remove(self):
        
        if not self.arr:
            return None
        
        top = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()

        if self.arr:
            self.heapify_down(0)

        return top

    def heapify_up(self, index):
        
        parent = (index - 1) // 2
        
        while index > 0 and self.arr[index] < self.arr[parent]:
            self.arr[index], self.arr[parent] = self.arr[parent], self.arr[index]
            index = parent
            parent = (index - 1) // 2

    def heapify_down(self, index):
        
        n = len(self.arr)
        
        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < n and self.arr[left] < self.arr[smallest]:
                smallest = left

            if right < n and self.arr[right] < self.arr[smallest]:
                smallest = right

            if smallest == index:
                break

            self.arr[index], self.arr[smallest] = self.arr[smallest], self.arr[index]
            index = smallest