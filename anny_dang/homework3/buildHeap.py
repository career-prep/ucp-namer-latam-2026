class Heap:
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
            if self.arr[i] < self.arr[parent]:
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
            smallest = i

            if left < n and self.arr[left] < self.arr[smallest]:
                smallest = left
            if right < n and self.arr[right] < self.arr[smallest]:
                smallest = right 
            
            if smallest != i:
                self.arr[smallest], self.arr[i] = self.arr[i], self.arr[smallest]
                i = smallest
            else:
                break

    def top(self):
        """
        Time complexity: O(1)
        """
        if not self.arr:
            return None
        return self.arr[0]
    
    def insert(self, x):
        """
        Time complexity: O(h)
        Space complexity: O(1)
        """
        self.arr.append(x)
        self.heapify_up(len(self.arr) - 1)

    def remove(self):
        """
        Time complexity: O(h)
        Space complexity: O(1)
        """
        if not self.arr:
            return None
        if len(self.arr) == 1:
            return self.arr.pop()

        root = self.arr[0]
        self.arr[0] = self.arr.pop()
        self.heapify_down(0)
        return root


ex1 = Heap()
for value in [7, 3, 10, 1, 5]:
    ex1.insert(value)
    print(f"insert {value}: {ex1.arr}")

print(f"top of ex1: {ex1.top()}")
print(f"remove from ex1: {ex1.remove()}")
print(f"after remove ex1: {ex1.arr}")

ex2 = Heap()
for value in [9, 4, 6, 2, 8]:
    ex2.insert(value)

print(f"starting ex2 heap: {ex2.arr}")
while ex2.top() is not None:
    print(f"removed {ex2.remove()}, heap is now {ex2.arr}")
