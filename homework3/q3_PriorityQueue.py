class PriorityQueue:
    def __init__(self, arr=None):
        self._arr = arr if arr is not None else []

    def left(self, i): return 2 * i + 1
    def right(self, i): return 2 * i + 2
    def parent(self, i): return (i - 1) // 2

    def top(self):
        return self._arr[0] if self._arr else None

    def insert(self, x, weight):
        self._arr.append((x, weight))
        i = len(self._arr) - 1

        while i > 0 and self._arr[self.parent(i)][1] > self._arr[i][1]:
            p = self.parent(i)
            self._arr[i], self._arr[p] = self._arr[p], self._arr[i]
            i = p

    def remove(self):
        if not self._arr:
            return None

        if len(self._arr) == 1:
            return self._arr.pop()

        root = self._arr[0]
        self._arr[0] = self._arr.pop()
        self.min_heapify(0)
        return root

    def min_heapify(self, i):
        l, r, n = self.left(i), self.right(i), len(self._arr)
        smallest = i

        if l < n and self._arr[l][1] < self._arr[smallest][1]:
            smallest = l
        if r < n and self._arr[r][1] < self._arr[smallest][1]:
            smallest = r

        if smallest != i:
            self._arr[i], self._arr[smallest] = self._arr[smallest], self._arr[i]
            self.min_heapify(smallest)

    def print(self):
        for pair in self._arr:
            print(pair[0], " ", end="")
        print()

if __name__ == "__main__":
    p = PriorityQueue()
    nums = [1, 2, 3, 6, 5]
    weights = [5, 4, 2, 1, 3]
    for i in range(len(nums)):
        p.insert(nums[i], weights[i])

    for i in range(5):
        print("Priority queue: ")
        p.print()
        print(f"Top (val, weight): {p.top()}")
        print("Removing top...")
        p.remove()
