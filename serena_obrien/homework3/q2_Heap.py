class Heap:
    def __init__(self, arr = None):
        self._arr = arr if arr is not None else []

    def left(self, i): return 2 * i + 1
    def right(self, i): return 2 * i + 2
    def parent(self, i): return (i - 1) // 2

    def top(self):
        return self._arr[0] if self._arr else None
    
    def insert(self, x):
        self._arr.append(x)
        i = len(self._arr) - 1

        while i > 0 and self._arr[self.parent(i)] > self._arr[i]:
            p = self.parent(i)
            self._arr[i], self._arr[p] = self._arr[p], self._arr[i]
            i = p
    
    def remove(self):
        if len(self._arr) <= 0: return
        if len(self._arr) == 1:
            self._arr.pop()
            return
        
        self._arr[0] = self._arr.pop() 
        self.min_heapify(0)

    def min_heapify(self, i):
        l, r, n = self.left(i), self.right(i), len(self._arr)
        smallest = i
        
        if l < n and self._arr[l] < self._arr[smallest]: smallest = l
        if r < n and self._arr[r] < self._arr[smallest]: smallest = r
          
        if smallest != i:
            self._arr[i], self._arr[smallest] = self._arr[smallest], self._arr[i]
            self.min_heapify(smallest)
    
    def print(self):
        print(self._arr)
    
if __name__ == "__main__":
    h = Heap()
    nums = [1, 2, 3, 6, 5]
    for n in nums:
        h.insert(n)

    for i in range(5):
        h.print()
        print(h.top())
        h.remove()
