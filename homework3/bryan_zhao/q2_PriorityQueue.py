class PriorityQueue:
    def __init__(self):
        self.arr = []

    # Returns the highest priority (first) element in the PQ
    def top(self):
        if not self.arr:
            return None
        return self.arr[0][1]
    
    # Adds string x to the PQ with priority weight
    def insert(self, x, weight):
        self.arr.append([x, weight])
        i = len(self.arr) - 1

        while i > 0:
            p = self.parent(i)
            if self.arr[i][1] > self.arr[p][1]:
                self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
                i = p
            else:
                break
    
    def remove(self):
        if not self.arr:
            return
        
        if len(self.arr) == 1:
            self.arr.pop()
            return

        self.arr[0] = self.arr.pop()
        self._bubble_down(0)

    def left(self, i):
        return 2 * i + 1
    
    def right(self, i):
        return 2 * i + 2
    
    def parent(self, i):
        return (i - 1) // 2
    
    # Helper function to fix the heap property downwards
    def _bubble_down(self, i):
        largest = i
        l, r, n = self.left(i), self.right(i), len(self.arr)

        if l < n and self.arr[l] > self.arr[largest][1]:
            largest = l
        if r < n and self.arr[r] > self.arr[largest][1]:
            largest = r
        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest]. self.arr[i]
            self._bubble_down(largest)