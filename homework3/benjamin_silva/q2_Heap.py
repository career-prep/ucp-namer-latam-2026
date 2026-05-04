class Heap:
    def __init__(self):
        self.arr = []

    def top(self):
        if not self.arr:
            return None
        return self.arr[0]

    def insert(self, x):
        self.arr.append(x)
        self.heapify_up(len(self.arr) - 1)
        pass

    def remove(self):
        if not self.arr:
            return None
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        removed = self.arr.pop()
        self.heapify_down(0)
        return removed

    def heapify_up(self, index):
        while index > 0:
            p = self.parent(index)
            if self.arr[index] < self.arr[p]:
                self.arr[index], self.arr[p] = self.arr[p], self.arr[index]
                index = p
            else:
                break

    def heapify_down(self, index):
        n = len(self.arr)
        while True:
            smallest = index
            l = self.left(index)
            r = self.right(index)

            if l < n and self.arr[l] < self.arr[smallest]:
                smallest = l
            if r < n and self.arr[r] < self.arr[smallest]:
                smallest = r
            
            if smallest != index:
                self.arr[index], self.arr[smallest] = self.arr[smallest], self.arr[index]
            else:
                break

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2


if __name__ == "__main__":
    h = Heap()

    print("insert & top")
    h.insert(5)
    print("Insert 5 | top (expect 5):", h.top())
    h.insert(3)
    print("Insert 3 | top (expect 3):", h.top())
    h.insert(8)
    print("Insert 8 | top (expect 3):", h.top())
    h.insert(1)
    print("Insert 1 | top (expect 1):", h.top())
    h.insert(4)
    print("Insert 4 | top (expect 1):", h.top())

    print("\nremove")
    h.remove()
    print("Remove   | top (expect 3):", h.top())
    h.remove()
    print("Remove   | top (expect 4):", h.top())
    h.remove()
    print("Remove   | top (expect 5):", h.top())

    print("\nfull sort via heap")
    h2 = Heap()
    for val in [9, 2, 7, 1, 5, 3]:
        h2.insert(val)
    result = []
    while h2.arr:
        result.append(h2.top())
        h2.remove()
    print("Got:     ", result)
    print("Expected: [1, 2, 3, 5, 7, 9]")