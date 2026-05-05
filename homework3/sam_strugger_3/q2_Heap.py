# O(log n) time for insert and remove, O(n) space

class Heap:
    def __init__(self):
        self.heap = [None] # Index start at 1 not 0

    def top(self):
        if len(self.heap) > 1:
            return self.heap[1]
        return None

    def insert(self, val): # Took me ~20 minutes
        length = len(self.heap)
        self.heap.append(val)
        val_index = length

        while val_index > 1 and self.heap[val_index] < self.heap[val_index//2]:
            parent_index =  val_index//2

            self.heap[val_index], self.heap[parent_index] = self.heap[parent_index], self.heap[val_index]
            val_index = parent_index

    def remove(self):
        if len(self.heap) <= 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        top_val = self.heap[1]
        self.heap[1] = self.heap.pop() # Move last element to root

        curr = 1
        while curr * 2 < len(self.heap):
            left = curr * 2
            right = curr * 2 + 1
            smallest_child = left

            if right < len(self.heap) and self.heap[right] < self.heap[left]:
                smallest_child = right

            if self.heap[curr] > self.heap[smallest_child]:
                self.heap[curr], self.heap[smallest_child] = self.heap[smallest_child], self.heap[curr]
                curr = smallest_child
            else:
                break

        return top_val

test1 = Heap()
for val in [5, 3, 8, 1, 2]:
    test1.insert(val)

print(test1.heap) # Internal array
print(test1.remove())
print(test1.remove())
print(test1.heap)

# I spent awhile on this I forgot to start my stop watch
