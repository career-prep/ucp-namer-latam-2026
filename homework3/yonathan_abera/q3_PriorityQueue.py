# Data Structure: Priority Queue (max heap on int priority, stores string/int pairs)
# Time Complexity: top() O(1), insert() O(log n), remove() O(log n)
# Space Complexity: O(n)

class PriorityQueue:
    def __init__(self):
        self.arr = []

    def top(self):
        if not self.arr:
            return None
        return self.arr[0][0]

    def insert(self, x, weight):
        self.arr.append((x, weight))
        self._bubble_up(len(self.arr) - 1)

    def remove(self):
        if not self.arr:
            return
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        if self.arr:
            self._sift_down(0)

    def _bubble_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.arr[parent][1] < self.arr[idx][1]:
                self.arr[parent], self.arr[idx] = self.arr[idx], self.arr[parent]
                idx = parent
            else:
                break

    def _sift_down(self, idx):
        n = len(self.arr)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            largest = idx
            if left < n and self.arr[left][1] > self.arr[largest][1]:
                largest = left
            if right < n and self.arr[right][1] > self.arr[largest][1]:
                largest = right
            if largest != idx:
                self.arr[largest], self.arr[idx] = self.arr[idx], self.arr[largest]
                idx = largest
            else:
                break


pq = PriorityQueue()
pq.insert("low priority task", 1)
pq.insert("urgent task", 10)
pq.insert("medium task", 5)
pq.insert("critical task", 20)

print(pq.top()) 

while pq.arr:
    print(pq.top())
    pq.remove()

# Time spent: ~40 minutes
