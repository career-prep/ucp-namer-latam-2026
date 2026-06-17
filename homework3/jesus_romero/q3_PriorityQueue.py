class PriorityQueue: # Technique: Max-Heap with (Value, Weight) pairs
    def __init__(self):
        self.arr = [] # Stores [string_val, integer_priority]

    def top(self): # O(1)
        return self.arr[0][0] if self.arr else None

    def insert(self, x, weight): # O(log n)
        self.arr.append([x, weight])
        self._bubble_up(len(self.arr) - 1)

    def remove(self): # O(log n)
        if not self.arr: return
        if len(self.arr) == 1:
            self.arr.pop()
            return
        self.arr[0] = self.arr.pop()
        self._bubble_down(0)

    def _bubble_up(self, idx):
        parent = (idx - 1) // 2
        # Max-Heap logic, higher weight has higher priority
        if idx > 0 and self.arr[idx][1] > self.arr[parent][1]:
            self.arr[idx], self.arr[parent] = self.arr[parent], self.arr[idx]
            self._bubble_up(parent)

    def _bubble_down(self, idx):
        left, right, largest = 2 * idx + 1, 2 * idx + 2, idx
        if left < len(self.arr) and self.arr[left][1] > self.arr[largest][1]:
            largest = left
        if right < len(self.arr) and self.arr[right][1] > self.arr[largest][1]:
            largest = right
        if largest != idx:
            self.arr[idx], self.arr[largest] = self.arr[largest], self.arr[idx]
            self._bubble_down(largest)

class Test:
    def run_tests(self):
        pq = PriorityQueue()
        
        # 1. Test insertion and highest priority retrieval
        pq.insert("task low", 10)
        pq.insert("task high", 50)
        pq.insert("task mid", 25)
        
        # Highest weight should be at the top
        assert pq.top() == "task high"
        
        # 2. Test removal order
        pq.remove() # Removes "task high"
        assert pq.top() == "task mid"
        
        pq.remove() # Removes "task mid"
        assert pq.top() == "task low"
        
        # 3. Test empty state
        pq.remove()
        assert pq.top() is None
        
        print("PriorityQueue tests passed")

if __name__ == "__main__":
    Test().run_tests()