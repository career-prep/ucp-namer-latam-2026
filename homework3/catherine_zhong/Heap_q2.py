
class Heap:
    def __init__(self, arr= []):
        self.arr = arr

    #move element up tree to correct position
    #time complexity: O(logn)
    def up(self, x):
        while x > 0:
            parent = (x-1)//2
            if self.arr[parent] <= self.arr[x]:
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

            if left < n and self.arr[left] < self.arr[smallest]:
                smallest = left
            if right < n and self.arr[right] < self.arr[smallest]:
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
    def insert(self, x):
        self.arr.append(x)
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
h = Heap()
h.insert(1)
h.insert(2)
h.insert(3)
h.insert(4)
h.insert(5)

print(f'initial heap: {h.arr}')

print(f'top element: {h.top()}')
h.remove()
print(f'remove top: {h.arr}')
h.insert(2)
print(f'insert 2: {h.arr}')

#time spent: 35 min