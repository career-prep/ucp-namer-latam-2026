# implement a min heap class with array as underlying DS
# assumption: head holds integers

#starting

class Heap():
    def __init__(self, heap):
        self.arr = heap

    def top(self):
        if self.arr:
            return self.arr[0]
        return -1

    def insert(self, x):
        
        i = len(self.arr)
        self.arr.append(x)

        while i >0 and self.arr[i] < self.arr[(i-1)//2]:
            self.arr[i], self.arr[(i-1)//2] = self.arr[(i-1)//2], self.arr[i]
            i = (i-1) // 2

        return self.arr[0]

    def remove(self):
        if len(self.arr) == 0:
            return "nothing to remove"

        if len(self.arr) == 1:
            return self.arr.pop()

        root = self.arr[0]
        self.arr[0] = self.arr.pop()

        i = 0
        n = len(self.arr)

        while True:
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and self.arr[left] < self.arr[smallest]:
                smallest = left

            if right < n and self.arr[right] < self.arr[smallest]:
                smallest = right

            if smallest == i:
                break

            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            i = smallest

        return root
    # private:
    #   array<int> arr; // the underlying array

    # public:
    #   int top(); // returns the min (top) element in the heap
    #   void insert(int x); // adds int x to the heap in the appropriate position
    #   void remove(); // removes the min (top) element in the heap




 