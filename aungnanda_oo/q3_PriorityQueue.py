# Question 3: Build a Priority Queue

# Max-priority queue using a max-heap over (string, int) pairs.
# The element with the highest integer priority is served first.

# Time Complexity:
#   top:    O(1)
#   insert: O(log n)
#   remove: O(log n)
# Space Complexity: O(n)


class PriorityQueue:
    def __init__(self):
        self.arr = []  # list of (string, int)

    def top(self):
        return self.arr[0][0] if self.arr else None
    # Time Complexity = O(1), Space Complexity = O(1)

    def insert(self, x, weight):
        self.arr.append((x, weight))
        self._sift_up(len(self.arr) - 1)
    # Time Complexity = O(log n), Space Complexity = O(1)

    def remove(self):
        if not self.arr:
            return None
        if len(self.arr) == 1:
            return self.arr.pop()[0]
        top = self.arr[0][0]
        self.arr[0] = self.arr.pop()
        self._sift_down(0)
        return top
    # Time Complexity = O(log n), Space Complexity = O(1)

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.arr[parent][1] < self.arr[i][1]:
                self.arr[parent], self.arr[i] = self.arr[i], self.arr[parent]
                i = parent
            else:
                break

    def _sift_down(self, i):
        n = len(self.arr)
        while True:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and self.arr[left][1] > self.arr[largest][1]:
                largest = left
            if right < n and self.arr[right][1] > self.arr[largest][1]:
                largest = right
            if largest != i:
                self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
                i = largest
            else:
                break


# --- Tests ---

pq = PriorityQueue()
print("top (empty):", pq.top())       # None
print("remove (empty):", pq.remove()) # None

pq.insert("low", 1)
pq.insert("high", 10)
pq.insert("medium", 5)
pq.insert("urgent", 15)
pq.insert("normal", 3)

print("top:", pq.top())               # urgent
print("remove:", pq.remove())         # urgent (15)
print("top:", pq.top())               # high (10)
print("remove:", pq.remove())         # high (10)
print("remove:", pq.remove())         # medium (5)
print("remove:", pq.remove())         # normal (3)
print("remove:", pq.remove())         # low (1)
print("remove (empty):", pq.remove()) # None

# Test equal priorities
pq2 = PriorityQueue()
pq2.insert("a", 5)
pq2.insert("b", 5)
print("equal priority top:", pq2.top())   # a or b (either valid)
print("equal priority remove:", pq2.remove())

# Spent a total of 20 mins on this question
