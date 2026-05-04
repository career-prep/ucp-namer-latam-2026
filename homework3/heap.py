# Technique: Array-based Min Heap with bubble up / bubble down
# Time Complexity: insert O(log n), remove O(log n), top O(1)
# Space Complexity: O(n)

class MinHeap:
    def __init__(self):
        self.arr = []

    def top(self):
        if not self.arr:
            return None
        return self.arr[0]

    def insert(self, x):
        self.arr.append(x)
        self._bubbleUp(len(self.arr) - 1)

    def remove(self):
        # removes the min (root) element
        if not self.arr:
            return
        # swap root with last, pop last, fix heap downward
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        if self.arr:
            self._bubbleDown(0)

    def _bubbleUp(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self.arr[idx] < self.arr[parent]:
            self.arr[idx], self.arr[parent] = self.arr[parent], self.arr[idx]
            idx = parent
            parent = (idx - 1) // 2

    def _bubbleDown(self, idx):
        n = len(self.arr)
        while True:
            smallest = idx
            left  = 2 * idx + 1
            right = 2 * idx + 2

            if left < n and self.arr[left] < self.arr[smallest]:
                smallest = left
            if right < n and self.arr[right] < self.arr[smallest]:
                smallest = right

            if smallest == idx:
                break

            self.arr[idx], self.arr[smallest] = self.arr[smallest], self.arr[idx]
            idx = smallest


# Test 1: basic inserts + top
h = MinHeap()
h.insert(5)
h.insert(3)
h.insert(8)
h.insert(1)
h.insert(4)
print(h.top())    
print(h.arr)      

# Test 2: remove min repeatedly
h.remove()
print(h.top())    
h.remove()
print(h.top())    
h.remove()
print(h.top())    
h.remove()
print(h.top())    
h.remove()
print(h.top())    

# Test 3: single element
h2 = MinHeap()
h2.insert(10)
print(h2.top())   
h2.remove()
print(h2.top())   

# Test 4: duplicate values
h3 = MinHeap()
h3.insert(2)
h3.insert(2)
h3.insert(1)
print(h3.top())  
h3.remove()
print(h3.top())   

# Time spent: ~35 minutes