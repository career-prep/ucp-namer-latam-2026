# Question 2: Build a Heap

# Min heap using an array as the underlying data structure.
# Parent at index i has children at 2i+1 and 2i+2.

# Time Complexity:
#   top:    O(1)
#   insert: O(log n)  — sift up
#   remove: O(log n)  — sift down
# Space Complexity: O(n)


class Heap:
    def __init__(self):
        self.arr = []

    def top(self):
        return self.arr[0] if self.arr else None
    # Time Complexity = O(1), Space Complexity = O(1)

    def insert(self, x):
        self.arr.append(x)
        self._sift_up(len(self.arr) - 1)
    # Time Complexity = O(log n), Space Complexity = O(1)

    def remove(self):
        if not self.arr:
            return None
        if len(self.arr) == 1:
            return self.arr.pop()
        min_val = self.arr[0]
        self.arr[0] = self.arr.pop()
        self._sift_down(0)
        return min_val
    # Time Complexity = O(log n), Space Complexity = O(1)

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.arr[parent] > self.arr[i]:
                self.arr[parent], self.arr[i] = self.arr[i], self.arr[parent]
                i = parent
            else:
                break

    def _sift_down(self, i):
        n = len(self.arr)
        while True:
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and self.arr[left] < self.arr[smallest]:
                smallest = left
            if right < n and self.arr[right] < self.arr[smallest]:
                smallest = right
            if smallest != i:
                self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
                i = smallest
            else:
                break


# --- Tests ---

h = Heap()
print("top (empty):", h.top())     # None
print("remove (empty):", h.remove())  # None

h.insert(5)
h.insert(3)
h.insert(8)
h.insert(1)
h.insert(4)
print("arr after inserts:", h.arr)
print("top:", h.top())             # 1

print("remove:", h.remove())       # 1
print("top after remove:", h.top())  # 3
print("arr:", h.arr)

h.insert(2)
print("top after insert(2):", h.top())  # 2
print("remove:", h.remove())            # 2
print("remove:", h.remove())            # 3
print("remove:", h.remove())            # 4
print("remove:", h.remove())            # 5
print("remove:", h.remove())            # 8
print("remove (empty):", h.remove())    # None

# Spent a total of 30 mins on this question
