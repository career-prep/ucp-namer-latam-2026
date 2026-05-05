class Heap:
    # The underlying array
    def __init__(self):
        self.arr = []

    # Returns the min(top) element in the heap
    def top(self):
        if not self.arr:
            return None
        return self.arr[0]
    
    # Adds int x to the heap in the appropriate position
    def insert(self, x):
        self.arr.append(x)
        i = len(self.arr) - 1

        while i > 0 and self.arr[self.parent(i)] > self.arr[i]:
            p = self.parent(i)
            self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
            i = p

    # Removes the min (top) element in the heap
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
        smallest = i
        l, r, n = self.left(i), self.right(i), len(self.arr)

        if l < n and self.arr[l] < self.arr[smallest]:
            smallest = l
        if r < n and self.arr[r] < self.arr[smallest]:
            smallest = r
        if smallest != i:
            self.arr[i], self.arr[smallest] = self.arr[smallest]. self.arr[i]
            self._bubble_down(smallest)