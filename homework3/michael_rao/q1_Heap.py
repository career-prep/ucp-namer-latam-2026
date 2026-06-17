class Heap:
    def __init__(self):
        self._arr = []

    def top(self):
        if not self._arr:
            raise IndexError("top from empty heap")
        return self._arr[0]

    def insert(self, x):
        self._arr.append(x)
        i = len(self._arr) - 1
        while i > 0:
            p = (i - 1) // 2
            if self._arr[p] <= self._arr[i]:
                break
            self._arr[p], self._arr[i] = self._arr[i], self._arr[p]
            i = p

    def remove(self):
        if not self._arr:
            raise IndexError("remove from empty heap")
        if len(self._arr) == 1:
            self._arr.pop()
            return
        self._arr[0] = self._arr.pop()
        i = 0
        n = len(self._arr)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < n and self._arr[left] < self._arr[smallest]:
                smallest = left
            if right < n and self._arr[right] < self._arr[smallest]:
                smallest = right
            if smallest == i:
                break
            self._arr[i], self._arr[smallest] = self._arr[smallest], self._arr[i]
            i = smallest


h = Heap()
for x in [5, 3, 7, 1, 9, 2]:
    h.insert(x)
out = []
while True:
    try:
        out.append(h.top())
        h.remove()
    except IndexError:
        break
print("popped in order:", out)
