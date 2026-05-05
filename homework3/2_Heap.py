class Heap:
    def __init__(self):
        self.arr = []

    def top(self):
        if not self.arr:
            return None
        return self.arr[0]

    def insert(self, x):
        self.arr.append(x)
        self._bubble_up(len(self.arr) - 1)

    def remove(self):
        if not self.arr:
            return
        
        if len(self.arr) > 1:
            self.arr[0] = self.arr.pop()
            self._bubble_down(0)
        else:
            self.arr.pop()

    def _bubble_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.arr[index] < self.arr[parent]:
            self.arr[index], self.arr[parent] = self.arr[parent], self.arr[index]
            self._bubble_up(parent)

    def _bubble_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index


        if left < len(self.arr) and self.arr[left] < self.arr[smallest]:
            smallest = left
        
        if right < len(self.arr) and self.arr[right] < self.arr[smallest]:
            smallest = right

        if smallest != index:
            self.arr[index], self.arr[smallest] = self.arr[smallest], self.arr[index]
            self._bubble_down(smallest)


if __name__ == "__main__":
    h = Heap()
    for val in [10, 4, 15, 1, 8]:
        h.insert(val)
        
    print(f"Top element (min): {h.top()}") 
    h.remove()
    print(f"New top after removal: {h.top()}")