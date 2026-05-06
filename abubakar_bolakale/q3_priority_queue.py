class PriorityQueue:
    def __init__(self):
        self.arr = []

    def top(self):
        return None if not self.arr else self.arr[0][0]

    def insert(self, x, weight):
        self.arr.append((x, weight))
        i = len(self.arr) - 1
        while i > 0:
            p = (i - 1) // 2
            if self.arr[i][1] > self.arr[p][1]:
                self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
                i = p
            else:
                break

    def remove(self):
        if not self.arr:
            return
        if len(self.arr) == 1:
            self.arr.pop()
            return
        self.arr[0] = self.arr.pop()
        i = 0
        while True:
            l, r = 2 * i + 1, 2 * i + 2
            m = i
            if l < len(self.arr) and self.arr[l][1] > self.arr[m][1]:
                m = l
            if r < len(self.arr) and self.arr[r][1] > self.arr[m][1]:
                m = r
            if m == i:
                break
            self.arr[i], self.arr[m] = self.arr[m], self.arr[i]
            i = m


if __name__ == "__main__":
    print("=== Empty ===")
    pq0 = PriorityQueue()
    print("  top:", pq0.top())

    print("=== Spec-style priorities ===")
    pq = PriorityQueue()
    pq.insert("a", 1)
    pq.insert("b", 9)
    pq.insert("c", 4)
    print("  top:", pq.top())
    pq.remove()
    print("  after remove:", pq.top())

    print("=== Tie-breaking (same weight) ===")
    pq2 = PriorityQueue()
    pq2.insert("first", 5)
    pq2.insert("second", 5)
    print("  top one of tie:", pq2.top())

    print("=== Negative priority weight ===")
    pq3 = PriorityQueue()
    pq3.insert("low", -5)
    pq3.insert("high", 100)
    print("  top:", pq3.top())


# Time complexity: O(log n) per insert and remove
# Space complexity: O(n)
# Time spent: 40 minutes
