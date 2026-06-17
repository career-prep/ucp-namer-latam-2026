class PriorityQueue:
    def __init__(self) -> None:
        self.heap = []

    def top(self):
        """Return the highest-priority string without removing it, or None if empty."""
        if not self.heap: return None
        return self.heap[0][1]

    def insert(self, x, weight):
        """Add x with priority weight and sift it up."""
        self.heap.append((-weight, x))
        i = len(self.heap)-1
        while i > 0:
            # even case
            if i % 2 == 0:
                par_i = (i-2)//2
            # odd case
            else:
                par_i = (i-1)//2
            if self.heap[i][0] < self.heap[par_i][0]:
                self.heap[i], self.heap[par_i] = self.heap[par_i], self.heap[i]
            else:
                break 
            i = par_i

    def remove(self):
        """Remove and return the highest-priority string."""
        N = len(self.heap)
        if not self.heap:
            return None
        if N == 1:
            data = self.heap.pop()
            return data[1]
        
        last_idx = N - 1

        self.heap[0], self.heap[last_idx] = self.heap[last_idx], self.heap[0]
        data = self.heap.pop()
        last_idx -= 1  

        cur = 0
        while 2*cur+1 <= last_idx:
            child_l = 2*cur+1
            child_r = 2*cur+2
            if child_r > last_idx:
                if self.heap[child_l] < self.heap[cur]:
                    self.heap[cur], self.heap[child_l] = self.heap[child_l], self.heap[cur]
                break
            else:
                min_idx = find_min_idx(self.heap, cur, child_l, child_r)
                if cur == min_idx:
                    break
                self.heap[min_idx], self.heap[cur] = self.heap[cur], self.heap[min_idx]
                cur = min_idx
        return data[1]

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
    pq = PriorityQueue()
    pq.insert("regular", 5)
    pq.insert("urgent", 10)
    pq.insert("low", 1)
    pq.insert("important", 7)

    print("Initial queue:")
    pq.display()

    print("Top:", pq.top())
    assert pq.top() == "urgent"

    print("Removed:", pq.remove())
    print("New top:", pq.top())
    assert pq.top() == "important"

    print("Removed:", pq.remove())
    print("Removed:", pq.remove())
    print("Removed:", pq.remove())
    assert pq.remove() is None

    print("All tests passed.")