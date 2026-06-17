class PriorityQueue:
    def __init__(self):
        self.arr = []

    def top(self):
        if self.arr:
            return self.arr[0][1]
        return None
    
    def left(self, i): 
        return 2 * i + 1
    def right(self, i): 
        return 2 * i + 2
    def parent(self, i): 
        return (i - 1) // 2
    
    def insert(self, x, weight):
        self.arr.append((weight, x))
        cur = len(self.arr) - 1

        while cur > 0 and self.arr[self.parent(cur)][0] < self.arr[cur][0]:
            p = self.parent(cur)
            self.arr[cur], self.arr[p] = self.arr[p], self.arr[cur]
            cur = p
    
    def remove(self):
        if not self.arr:
            return
        
        last_val = self.arr.pop()
        if self.arr:
            self.arr[0] = last_val
            self.max_heapify(0)

    def max_heapify(self, i):
        l, r, n = self.left(i), self.right(i), len(self.arr)
        largest = i
        
        if l < n and self.arr[l][0] > self.arr[largest][0]: largest = l
        if r < n and self.arr[r][0] > self.arr[largest][0]: largest = r
          
        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.max_heapify(largest)


pq = PriorityQueue()

pq.insert("low_priority_task", 1)
pq.insert("emergency_task", 10)
pq.insert("medium_task", 5)

print(pq.top())
print(pq.remove())
print(pq.top())
print(pq.remove())
print(pq.top())