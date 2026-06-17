# Time taken: ~45 minutes
# def top: -> Time O(1)
# def insert: -> Time O(log(N))
# def remove: -> Time O(log(N))

import random


class Heap:
    """Min-heap stored in level-order: children of i are 2i+1 and 2i+2."""

    def __init__(self) -> None:
        self.heap = []

    def top(self):
        """Return the minimum without removing it, or None if empty."""
        if not self.heap: return None
        return self.heap[0]

    def insert(self, x):
        """Append x at the end and sift it up to restore the min-heap property."""
        self.heap.append(x)
        i = len(self.heap)-1
        while i > 0:
            # even case
            if i % 2 == 0:
                par_i = (i-2)//2
            # odd case
            else:
                par_i = (i-1)//2
            if self.heap[i] < self.heap[par_i]:
                self.heap[i], self.heap[par_i] = self.heap[par_i], self.heap[i]
            else:
                break 
            i = par_i

    def remove(self):
        """Pop and return the minimum; replace root with last leaf and sift down."""
        N = len(self.heap)
        if not self.heap:
            return None
        if N == 1:
            data = self.heap.pop()
            return data
        
        last_idx = N - 1

        self.heap[0], self.heap[last_idx] = self.heap[last_idx], self.heap[0]
        data = self.heap.pop()
        last_idx -= 1  

        cur = 0
        while cur <= last_idx-2:
            child_l = 2*cur+1
            child_r = 2*cur+2
            if child_l > last_idx:
                break
            elif child_r > last_idx:
                if self.heap[child_l] < self.heap[cur]:
                    self.heap[cur], self.heap[child_l] = self.heap[child_l], self.heap[cur]
                break
            else:
                min_idx = find_min_idx(self.heap, cur, child_l, child_r)
                if cur == min_idx:
                    break
                self.heap[min_idx], self.heap[cur] = self.heap[cur], self.heap[min_idx]
                cur = min_idx
        return data
    def display(self):
        """Print the array."""
        print(self.heap)
                

def find_min_idx(arr, i, j, k):
    """Return whichever of i, j, k indexes the smallest value in arr."""
    if arr[i] <= arr[j] and arr[i] <= arr[k]:
        return i 
    elif arr[j] <= arr[k] and arr[j] <= arr[i]:
        return j 
    else:
        return k


if __name__ == "__main__":
    random.seed(1)

    heap = Heap()
    values = []

    print("Inserting random values:")
    for _ in range(10):
        x = random.randint(0, 50)
        values.append(x)
        heap.insert(x)
        print(f"insert {x} -> ", end="")
        heap.display()

    print("\nTop:", heap.top())

    removed = []
    print("\nRemoving values:")
    while heap.top() is not None:
        removed_value = heap.remove()
        removed.append(removed_value)
        print(f"remove {removed_value:2d} -> ", end="")
        heap.display()

    print("\nOriginal values:", values)
    print("Removed order:  ", removed)
    assert removed == sorted(values)


