class MinHeap:
    def __init__(self, values=None):
        self.data = values[:] if values else []

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def peek(self):
        return self.data[0] if self.data else None

    def add(self, value):
        self.data.append(value)
        self._bubble_up(len(self.data) - 1)

    def remove_min(self):
        if not self.data:
            return None

        if len(self.data) == 1:
            return self.data.pop()

        minimum = self.data[0]
        self.data[0] = self.data.pop()
        self._bubble_down(0)
        return minimum

    def _bubble_up(self, i):
        while i > 0:
            p = self._parent(i)
            if self.data[p] <= self.data[i]:
                break
            self.data[p], self.data[i] = self.data[i], self.data[p]
            i = p

    def _bubble_down(self, i):
        n = len(self.data)

        while True:
            smallest = i
            l = self._left(i)
            r = self._right(i)

            if l < n and self.data[l] < self.data[smallest]:
                smallest = l
            if r < n and self.data[r] < self.data[smallest]:
                smallest = r

            if smallest == i:
                break

            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            i = smallest

    def show(self):
        print(self.data)
