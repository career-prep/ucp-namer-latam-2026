def _higher_priority(a, b):
    wa = a[1]
    wb = b[1]
    if wa != wb:
        return wa > wb
    return a[0] > b[0]


class PriorityQueue:
    def __init__(self):
        self._arr = []

    def top(self):
        if not self._arr:
            raise IndexError("top from empty priority queue")
        return self._arr[0][0]

    def insert(self, x, weight):
        self._arr.append((x, weight))
        i = len(self._arr) - 1
        while i > 0:
            p = (i - 1) // 2
            if not _higher_priority(self._arr[i], self._arr[p]):
                break
            self._arr[p], self._arr[i] = self._arr[i], self._arr[p]
            i = p

    def remove(self):
        if not self._arr:
            raise IndexError("remove from empty priority queue")
        if len(self._arr) == 1:
            self._arr.pop()
            return
        self._arr[0] = self._arr.pop()
        i = 0
        n = len(self._arr)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            best = i
            if left < n and _higher_priority(self._arr[left], self._arr[best]):
                best = left
            if right < n and _higher_priority(self._arr[right], self._arr[best]):
                best = right
            if best == i:
                break
            self._arr[i], self._arr[best] = self._arr[best], self._arr[i]
            i = best


pq = PriorityQueue()
pq.insert("low", 1)
pq.insert("high", 10)
pq.insert("mid", 5)
pq.insert("tie_b", 5)
pq.insert("tie_a", 5)
out = []
while True:
    try:
        out.append(pq.top())
        pq.remove()
    except IndexError:
        break
print("pop order (max priority first):", out)
