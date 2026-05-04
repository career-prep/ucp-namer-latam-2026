
class PriorityQueue:
    def __init__(self, arr= None):
        self.arr = arr if arr is not None else []

    #move element up tree to correct position
    #time complexity: O(logn)
    def up(self, x):
        while x > 0:
            parent = (x-1)//2
            if self.arr[parent][1] <= self.arr[x][1]:
                break
            self.arr[parent], self.arr[x] = self.arr[x], self.arr[parent]
            x = parent

        return

    # moves element down to bottom of tree
    #time complexity: O(logn)
    def down(self, x):
        n = len(self.arr)

        while True:
            left = 2*x + 1
            right = 2*x + 2
            smallest = x

            if left < n and self.arr[left][1] < self.arr[smallest][1]:
                smallest = left
            if right < n and self.arr[right][1] < self.arr[smallest][1]:
                smallest = right

            if smallest == x:
                break

            self.arr[x], self.arr[smallest] = self.arr[smallest], self.arr[x]
            x = smallest
        return 

    #int top(); // returns the min (top) element in the heap
    #time complexity: O(1)
    def top(self):
        if not self.arr:
            return

        return self.arr[0]

    #void insert(int x); // adds int x to the heap in the appropriate position
    #time complexity: O(logn)
    def insert(self, x, w):
        self.arr.append((x,w))
        self.up(len(self.arr)-1)
        return 

    #void remove(); // removes the min (top) element in the heap
    #time complexity: O(logn)
    def remove(self):
        if not self.arr:
            return
        self.arr[0] = self.arr[len(self.arr)-1]
        self.arr.pop()

        if self.arr:
            self.down(0)
        return

#test cases

q = PriorityQueue()
q.insert('bob', 3)
q.insert('teddy', 5)
q.insert('al', 2)
q.insert('todd', 4)

print(f'initial queue: {q.arr}')
print(f'get top element: {q.top()}')
q.insert('charlie', 7)
print(f'insert (charlie, 7): {q.arr}')
q.remove()
print(f'remove top element: {q.arr}')

#time spent: 20 min