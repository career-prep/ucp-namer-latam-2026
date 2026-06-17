class PriorityQueue:
    def __init__(self):
        self.arr = []

    def top(self):
        
        if not self.arr:
            return None
        
        return self.arr[0][0]

    def insert(self, x, weight):
        
        self.arr.append((x, weight))
        self.heapify_up(len(self.arr) - 1)

    def remove(self):
        
        if not self.arr:
            return None

        top = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()

        if self.arr:
            self.heapify_down(0)

        return top[0]

    def heapify_up(self, index):
        
        parent = (index - 1) // 2

        while index > 0 and self.arr[index][1] > self.arr[parent][1]:
            self.arr[index], self.arr[parent] = self.arr[parent], self.arr[index]
            index = parent
            parent = (index - 1) // 2

    def heapify_down(self, index):
        
        n = len(self.arr)

        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < n and self.arr[left][1] > self.arr[largest][1]:
                largest = left

            if right < n and self.arr[right][1] > self.arr[largest][1]:
                largest = right

            if largest == index:
                break

            self.arr[index], self.arr[largest] = self.arr[largest], self.arr[index]
            index = largest