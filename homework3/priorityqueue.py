# Technique: Array-based Max Heap storing 
# Time Complexity: insert O(log n), remove O(log n), top O(1)
# Space Complexity: O(n)


class PriorityQueue:
    def __init__(self):
        self.arr = []

    def top(self):
        if not self.arr:
            return None
        return self.arr[0][1]  

    def insert(self, x, weight):
        self.arr.append((-weight, x))
        self._bubbleUp(len(self.arr) - 1)

    def remove(self):
        # removes highest priority (root) element
        if not self.arr:
            return
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        if self.arr:
            self._bubbleDown(0)

    def _bubbleUp(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self.arr[idx][0] < self.arr[parent][0]:
            self.arr[idx], self.arr[parent] = self.arr[parent], self.arr[idx]
            idx = parent
            parent = (idx - 1) // 2

    def _bubbleDown(self, idx):
        n = len(self.arr)
        while True:
            smallest = idx
            left  = 2 * idx + 1
            right = 2 * idx + 2

            if left < n and self.arr[left][0] < self.arr[smallest][0]:
                smallest = left
            if right < n and self.arr[right][0] < self.arr[smallest][0]:
                smallest = right

            if smallest == idx:
                break

            self.arr[idx], self.arr[smallest] = self.arr[smallest], self.arr[idx]
            idx = smallest


# Test 1: basic inserts, top returns highest priority
pq = PriorityQueue()
pq.insert("Cricket", 10)
pq.insert("Tabletennis", 9)
pq.insert("Football", 7)
pq.insert("Movies", 5)
print(pq.top())    

# Test 2: remove in priority order
pq.remove()
print(pq.top())    
pq.remove()
print(pq.top())    
pq.remove()
print(pq.top())    
pq.remove()
print(pq.top())    

# Test 3: single element
pq2 = PriorityQueue()
pq2.insert("only task", 1)
print(pq2.top())   
pq2.remove()
print(pq2.top())   

# Test 4: same priority
pq3 = PriorityQueue()
pq3.insert("task a", 5)
pq3.insert("task b", 5)
print(pq3.top())   # task a or task b (either valid)

# Time spent: ~20 minutes