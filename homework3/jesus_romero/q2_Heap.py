# Technique: Array-based Min-Heap using sift-up and sift-down

class Heap: # Time, Space Complexities: Insert/Remove O(log n), Top O(1), Space O(n)
    def __init__(self):
        # 1. Initialize the underlying array to store heap elements as per API
        self.arr = []

    def top(self): 
        # 2. Return the root element (the minimum) without removing it
        if not self.arr:
            return None
        return self.arr[0]

    def insert(self, x):
        # 3. Add the new element to the end of the array
        self.arr.append(x)
        # 4. Bubble up the element to its correct position to maintain min-heap property
        self._bubble_up(len(self.arr) - 1)

    def remove(self):
        # 5. Handle empty or single-element cases
        if not self.arr:
            return
        if len(self.arr) == 1:
            self.arr.pop()
            return
        
        # 6. Replace the root with the last element and remove the last element
        self.arr[0] = self.arr.pop()
        # 7. Bubble down the new root to its correct position
        self._bubble_down(0)

    def _bubble_up(self, idx):
        # 8. Compare the current node with its parent
        parent = (idx - 1) // 2
        if idx > 0 and self.arr[idx] < self.arr[parent]:
            # 9. Swap if the current node is smaller than the parent
            self.arr[idx], self.arr[parent] = self.arr[parent], self.arr[idx]
            self._bubble_up(parent)

    def _bubble_down(self, idx):
        # 10. Identify the indices of the children
        left = 2 * idx + 1
        right = 2 * idx + 2
        smallest = idx
        
        # 11. Find the smallest value among the parent and its two children
        if left < len(self.arr) and self.arr[left] < self.arr[smallest]:
            smallest = left
        if right < len(self.arr) and self.arr[right] < self.arr[smallest]:
            smallest = right
            
        # 12. If the smallest value is not the parent, swap and continue bubbling down
        if smallest != idx:
            self.arr[idx], self.arr[smallest] = self.arr[smallest], self.arr[idx]
            self._bubble_down(smallest)

class Test:
    def run_tests(self):
        h = Heap()
        
        # 1. Test insertion and min-property
        h.insert(10)
        h.insert(5)
        h.insert(20)
        h.insert(2)
        
        # In a min-heap, 2 should be at the top
        assert h.top() == 2
        
        # 2. Test removal order (should always remove the smallest)
        h.remove() # Removes 2
        assert h.top() == 5
        
        h.remove() # Removes 5
        assert h.top() == 10
        
        # 3. Test single element state
        h.remove() # Removes 10
        assert h.top() == 20
        
        # 4. Test empty state
        h.remove() # Removes 20
        assert h.top() is None
        
        # 5. Test negative numbers and duplicates
        h.insert(-5)
        h.insert(0)
        h.insert(-5)
        assert h.top() == -5
        h.remove()
        assert h.top() == -5
        
        print("Heap tests passed")

if __name__ == "__main__":
    tester = Test()
    tester.run_tests()