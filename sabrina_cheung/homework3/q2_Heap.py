class Heap:
    def __init__(self):
        self.arr = []

    def top(self):
        if self.arr:
            return self.arr[0]
        return None
    
    def left(self, i): 
        return 2 * i + 1
    def right(self, i): 
        return 2 * i + 2
    def parent(self, i): 
        return (i - 1) // 2
    
    def insert(self, x):
        self.arr.append(x)
        cur = len(self.arr) - 1

        while cur > 0 and self.arr[self.parent(cur)] > self.arr[cur]:
            p = self.parent(cur)
            self.arr[cur], self.arr[p] = self.arr[p], self.arr[cur]
            cur = p
    
    def remove(self):
        if not self.arr:
            return
        
        last_val = self.arr.pop()
        if self.arr:
            self.arr[0] = last_val
            self.min_heapify(0)

    def min_heapify(self, i):
        l, r, n = self.left(i), self.right(i), len(self.arr)
        smallest = i
        
        if l < n and self.arr[l] < self.arr[smallest]: smallest = l
        if r < n and self.arr[r] < self.arr[smallest]: smallest = r
          
        if smallest != i:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            self.min_heapify(smallest)

h = Heap()

h.insert(20)
h.insert(5)
h.insert(15)
h.insert(1)

print(h.top())
h.remove()
print(h.top())