class PriorityQueue:
    def __init__(self):
        self.arr = [] 

    def top(self):
        if not self.arr:
            return None
        return self.arr[0][0]

    def insert(self, x, weight):
        self.arr.append((x, weight))
        self._heapify_up(len(self.arr) - 1)

    def remove(self):
        if not self.arr:
            return None
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        removed  = self.arr.pop()
        self._heapify_down(0)
        return removed

    def _heapify_up(self, index):
        while index > 0:
            p = self._parent(index)
            if self.arr[index][1] > self.arr[p][1]:
                self.arr[index], self.arr[p] = self.arr[p], self.arr[index]
                index = p
            else:
                break

    def _heapify_down(self, index):
        n = len(self.arr)
        while True:
            largest = index
            l = self._left(index)
            r = self._right(index)

            if l < n and self.arr[l][1] > self.arr[largest][1]:
                largest = l
            if r < n and self.arr[r][1] > self.arr[largest][1]:
                largest = r
            
            if largest != index:
                self.arr[index], self.arr[largest] = self.arr[largest], self.arr[index]
                index = largest
            else:
                break

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2


if __name__ == "__main__":
    pq = PriorityQueue()

    print("insert & top")
    pq.insert("low", 1)
    print("Insert low(1)    | top (expect low):", pq.top())
    pq.insert("high", 10)
    print("Insert high(10)  | top (expect high):", pq.top())
    pq.insert("medium", 5)
    print("Insert medium(5) | top (expect high):", pq.top())
    pq.insert("urgent", 20)
    print("Insert urgent(20)| top (expect urgent):", pq.top())

    print("\nremove")
    pq.remove()
    print("Remove | top (expect high):", pq.top())
    pq.remove()
    print("Remove | top (expect medium):", pq.top())
    pq.remove()
    print("Remove | top (expect low):", pq.top())

    print("\nfull priority order")
    pq2 = PriorityQueue()
    pq2.insert("dishes", 3)
    pq2.insert("laundry", 7)
    pq2.insert("taxes", 15)
    pq2.insert("nap", 1)
    pq2.insert("groceries", 9)
    result = []
    while pq2.arr:
        result.append(pq2.top())
        pq2.remove()
    print("Got:     ", result)
    print("Expected: ['taxes', 'groceries', 'laundry', 'dishes', 'nap']")