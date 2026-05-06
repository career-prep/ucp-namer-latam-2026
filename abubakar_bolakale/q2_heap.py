class Heap:
    def __init__(self):
        self.arr = []

    def top(self):
        return None if not self.arr else self.arr[0]

    def insert(self, x):
        self.arr.append(x)
        i = len(self.arr) - 1
        while i > 0:
            p = (i - 1) // 2
            if self.arr[i] < self.arr[p]:
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
            if l < len(self.arr) and self.arr[l] < self.arr[m]:
                m = l
            if r < len(self.arr) and self.arr[r] < self.arr[m]:
                m = r
            if m == i:
                break
            self.arr[i], self.arr[m] = self.arr[m], self.arr[i]
            i = m


if __name__ == "__main__":
    print("=== Empty ===")
    h0 = Heap()
    print("  top:", h0.top())

    print("=== Single element ===")
    h1 = Heap()
    h1.insert(42)
    print("  top:", h1.top())
    h1.remove()
    print("  after remove top:", h1.top())

    print("=== Build [5,3,7,1] min at root ===")
    h = Heap()
    for x in (5, 3, 7, 1):
        h.insert(x)
    print("  top:", h.top())
    h.remove()
    print("  after one pop:", h.top())
    h.remove()
    print("  after two pops:", h.top())

    print("=== Duplicates ===")
    hd = Heap()
    for x in (2, 2, 2):
        hd.insert(x)
    print("  top:", hd.top(), "len:", len(hd.arr))

    print("=== Negative values ===")
    hn = Heap()
    for x in (5, -10, 3):
        hn.insert(x)
    print("  top:", hn.top())


# Time complexity: O(log n) per insert and remove
# Space complexity: O(n)
# Time spent: 37 minutes
