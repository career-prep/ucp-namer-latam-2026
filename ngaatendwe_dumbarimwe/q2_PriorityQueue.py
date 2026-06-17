class PriorityQueue:
    def __init__(self):
        self.data = []

    def insert(self, value, priority):
        # store as (priority, value)
        self.data.append((priority, value))
        i = len(self.data) - 1

        # bubble up
        while i > 0:
            parent = (i - 1) // 2
            if self.data[i][0] < self.data[parent][0]:
                self.data[i], self.data[parent] = self.data[parent], self.data[i]
                i = parent
            else:
                break

    def top(self):
        if len(self.data) == 0:
            return None
        # return just the value, not the tuple
        return self.data[0][1]

    def remove(self):
        if len(self.data) == 0:
            return None

        if len(self.data) == 1:
            return self.data.pop()[1]

        root = self.data[0]
        self.data[0] = self.data.pop()

        i = 0
        n = len(self.data)

        # bubble down
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < n and self.data[left][0] < self.data[smallest][0]:
                smallest = left

            if right < n and self.data[right][0] < self.data[smallest][0]:
                smallest = right

            if smallest != i:
                self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
                i = smallest
            else:
                break

        return root[1]


#Time-taken: 20 minutes