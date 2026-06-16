# Data Structure: Priority Queue (max-heap of (element, weight) pairs, keyed on weight)
#
# Time complexity:
#   top():    O(1)
#   insert(): O(log n)
#   remove(): O(log n)
# Space complexity: O(n)
#
# Built on top of the heap idea from q2 but using a max-heap and a tuple payload.


class PriorityQueue:
    def __init__(self):
        self.arr = []  # list of (element, weight)

    def top(self):
        if not self.arr:
            raise IndexError("top from empty priority queue")
        return self.arr[0][0]

    def insert(self, x, weight):
        self.arr.append((x, weight))
        self._sift_up(len(self.arr) - 1)

    def remove(self):
        if not self.arr:
            raise IndexError("remove from empty priority queue")
        top = self.arr[0]
        last = self.arr.pop()
        if self.arr:
            self.arr[0] = last
            self._sift_down(0)
        return top[0]

    def __len__(self):
        return len(self.arr)

    def _weight(self, i):
        return self.arr[i][1]

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self._weight(i) > self._weight(parent):
                self.arr[i], self.arr[parent] = self.arr[parent], self.arr[i]
                i = parent
            else:
                return

    def _sift_down(self, i):
        n = len(self.arr)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i
            if left < n and self._weight(left) > self._weight(largest):
                largest = left
            if right < n and self._weight(right) > self._weight(largest):
                largest = right
            if largest == i:
                return
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            i = largest


# test cases
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert("low", 1)
    pq.insert("high", 10)
    pq.insert("mid", 5)
    pq.insert("higher", 11)

    assert pq.top() == "higher"
    assert pq.remove() == "higher"
    assert pq.remove() == "high"
    assert pq.remove() == "mid"
    assert pq.remove() == "low"

    print("yay!!")

# Time spent: ~15 minutes
