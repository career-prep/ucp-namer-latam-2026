class MinHeap:
    def __init__(self):
        self.data = []

    def insert(self, x):
        self.data.append(x)
        i = len(self.data) - 1

        # bubble up
        while i > 0:
            parent = (i - 1) // 2
            if self.data[i] < self.data[parent]:
                self.data[i], self.data[parent] = self.data[parent], self.data[i]
                i = parent
            else:
                break

    def top(self):
        if len(self.data) == 0:
            return None
        return self.data[0]

    def remove(self):
        if len(self.data) == 0:
            return None

        if len(self.data) == 1:
            return self.data.pop()

        root = self.data[0]
        self.data[0] = self.data.pop()

        i = 0
        n = len(self.data)

        # bubble down
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < n and self.data[left] < self.data[smallest]:
                smallest = left

            if right < n and self.data[right] < self.data[smallest]:
                smallest = right

            if smallest != i:
                self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
                i = smallest
            else:
                break

        return root


#Time-taken: 25 minutes