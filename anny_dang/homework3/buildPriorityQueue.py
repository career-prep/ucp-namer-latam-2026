class PriorityQueue:
    def __init__(self):
        self.arr = []

    def heapify_up(self, i):
        """
        idea:
        start from index i, compare that value with its parent,
        and swap while the child is smaller
        this continues until the value reaches the correct position

        Time complexity: O(h) (h: height of heap tree)
        Space complexity: O(1)
        """
        while i > 0:
            parent = (i - 1)//2
            if self.arr[i][1] > self.arr[parent][1]:
                self.arr[i], self.arr[parent] = self.arr[parent], self.arr[i]
                i = parent
            else:
                break

    def heapify_down(self, i):
        """
        idea:
        start from index i, compare it with its left and right children, 
        and swap with the smaller child if needed 
        keep moving doward until the current value is in correct place

        Time complexity: O(h) (h: height of heap tree)
        Space complexity: O(1)
        """
        n = len(self.arr)

        while i < n:
            left = 2*i + 1
            right = 2*i + 2
            highest = i

            if left < n and self.arr[left][1] > self.arr[highest][1]:
                highest = left
            if right < n and self.arr[right][1] > self.arr[highest][1]:
                highest = right 
            
            if highest != i:
                self.arr[highest], self.arr[i] = self.arr[i], self.arr[highest]
                i = highest
            else:
                break

    def top(self):
        if not self.arr:
            return None
        return self.arr[0]
    
    def insert(self, x, weight):
        self.arr.append((x, weight))
        self.heapify_up(len(self.arr) - 1)

    def remove(self):
        if not self.arr:
            return None
        if len(self.arr) == 1:
            return self.arr.pop()

        root = self.arr[0]
        self.arr[0] = self.arr.pop()
        self.heapify_down(0)
        return root


ex1 = PriorityQueue()
for item, weight in [("study", 10), ("eat", 3), ("sleep", 7), ("exercise", 12)]:
    ex1.insert(item, weight)
    print(f"insert ({item}, {weight}): {ex1.arr}")

print(f"top of ex1: {ex1.top()}")
print(f"remove from ex1: {ex1.remove()}")
print(f"after remove ex1: {ex1.arr}")

ex2 = PriorityQueue()
for item, weight in [("wash dishes", 2), ("do homework", 9), ("call mom", 5), ("buy groceries", 7)]:
    ex2.insert(item, weight)

print(f"starting ex2 priority queue: {ex2.arr}")
while ex2.top() is not None:
    print(f"removed {ex2.remove()}, priority queue is now {ex2.arr}")
