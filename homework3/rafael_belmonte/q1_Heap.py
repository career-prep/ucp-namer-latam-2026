# Data Structure: Min-Heap (array-backed binary heap)
#
# Time complexity:
#   top():    O(1)
#   insert(): O(log n)
#   remove(): O(log n)
# Space complexity: O(n)


class Heap:
    def __init__(self):
        self.arr = []

    def top(self):
        if not self.arr:
            raise IndexError("top from empty heap")
        return self.arr[0]

    def insert(self, x):
        self.arr.append(x)
        self._sift_up(len(self.arr) - 1)

    def remove(self):
        if not self.arr:
            raise IndexError("remove from empty heap")
        top = self.arr[0]
        last = self.arr.pop()
        if self.arr:
            self.arr[0] = last
            self._sift_down(0)
        return top

    def __len__(self):
        return len(self.arr)

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.arr[i] < self.arr[parent]:
                self.arr[i], self.arr[parent] = self.arr[parent], self.arr[i]
                i = parent
            else:
                return

    def _sift_down(self, i):
        n = len(self.arr)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < n and self.arr[left] < self.arr[smallest]:
                smallest = left
            if right < n and self.arr[right] < self.arr[smallest]:
                smallest = right
            if smallest == i:
                return
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            i = smallest


# test cases
if __name__ == "__main__":
    h = Heap()
    for x in [5, 3, 8, 1, 9, 2, 7]:
        h.insert(x)
    assert h.top() == 1

    out = []
    while len(h):
        out.append(h.remove())
    assert out == sorted([5, 3, 8, 1, 9, 2, 7]), out

    # duplicates + single element
    h2 = Heap()
    for x in [4, 4, 4, 1, 4]:
        h2.insert(x)
    assert h2.remove() == 1
    assert h2.remove() == 4

    print("yay!!")

# Time spent: ~25 minutes
