class PriorityQueue:
    def __init__(self):
        self.arr = []

    def top(self):
        if not self.arr:
            return None
        return self.arr[0][1]

    def insert(self, x, weight):
        self.arr.append((weight, x))
        self._bubble_up(len(self.arr) - 1)

    def remove(self):
        if not self.arr:
            return
        
        if len(self.arr) > 1:
            self.arr[0] = self.arr.pop()
            self._bubble_down(0)
        else:
            self.arr.pop()

    def _bubble_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.arr[index][0] > self.arr[parent][0]:
            self.arr[index], self.arr[parent] = self.arr[parent], self.arr[index]
            self._bubble_up(parent)

    def _bubble_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.arr) and self.arr[left][0] > self.arr[largest][0]:
            largest = left
        
        if right < len(self.arr) and self.arr[right][0] > self.arr[largest][0]:
            largest = right

        if largest != index:
            self.arr[index], self.arr[largest] = self.arr[largest], self.arr[index]
            self._bubble_down(largest)