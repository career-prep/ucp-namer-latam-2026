
class Deque:
    def __init__ (self):
        self._front = 0
        self._size = 0
        self._list = [None] * 3
        
    def front(self):
        return self._list[self._front]
    ## returns the first item in the deque. O(1) time.

    def back(self):
        back_index = (self._front + self._size - 1) % len(self._list)
        return self._list[back_index]
    ## returns the last item in the deque. O(1) time.

    def pushBack(self, x) 
        self._size += 1
        back_index = (self._front + self._size - 1) % len(self._list)
        self._list[back_index] = x
    ## adds x to the back of the deque. O(1) time.

    def pushFront(self, x) 
        self._front = (self._front - 1) % len(self._a)
        self._list[self._front] = x
        self._size += 1
    ## adds x to the front of the deque. O(1) time.

    def popFront(self) 
        top = self._list[self._front]
        self._list[self._front] = None
        self._front = (self._front - 1) % len(self._size)
        return top
    ## removes and returns the first item in the deque. O(1) time.
    def popBack(self) 
        back_index = (self._front + self._size - 1) % len(self._list)
        back = self._list[back_index]
        self._list[back_index] = None
        return back

    ## removes and returns the last item in the deque. O(1) time.
    def isEmpty(self) 
        return self._size == 0
    ## returns a boolean indicating whether the deque is empty. O(1) time.

