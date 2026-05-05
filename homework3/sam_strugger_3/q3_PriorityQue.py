# O(log n) time for push and remove, O(n) space

class PriorityQueue:
    def __init__(self):
        self.heap = [None] 

    def top(self):
        if len(self.heap) > 1:
            return self.heap[1][1] 
        return None

    def push(self, priority, item):
        entry = (priority, item)
        self.heap.append(entry)
        val_index = len(self.heap) - 1

        while val_index > 1 and self.heap[val_index][0] < self.heap[val_index//2][0]:
            parent_index = val_index // 2
            self.heap[val_index], self.heap[parent_index] = self.heap[parent_index], self.heap[val_index]
            val_index = parent_index

    def remove(self):
        if len(self.heap) <= 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()[1] 

        root_entry = self.heap[1]
        self.heap[1] = self.heap.pop()

        curr = 1
        while curr * 2 < len(self.heap):
            left = curr * 2
            right = curr * 2 + 1
            smallest_child = left

            if right < len(self.heap) and self.heap[right][0] < self.heap[left][0]:
                smallest_child = right

            if self.heap[curr][0] > self.heap[smallest_child][0]:
                self.heap[curr], self.heap[smallest_child] = self.heap[smallest_child], self.heap[curr]
                curr = smallest_child
            else:
                break

        return root_entry[1] # Return the item

test1 = PriorityQueue()
test1.push(3, "Low Priority")
test1.push(1, "High Priority")
test1.push(2, "Medium Priority")

print(test1.remove())
print(test1.remove())
print(test1.remove())

# I spent 10 minutes
