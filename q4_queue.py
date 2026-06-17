# Time: 20 minutes
class Queue:
    def __innit (self):
        self._q = []
        self._head = 0

    def peek(self):
        return self._q[self._head]
    ## returns the first item in the queue. O(1) time.

    def enqueue(self, x):
        self._q.append(x)
    ## adds x to the back of the queue. O(1) time.

    def dequeue(self):
        top = self._q[self._head]
        self._head += 1

        return top
    ## removes and returns the first item in the queue. O(1) time.

    def isEmpty(self):
        if len(self._q) == 0:
            return True
        retrun False
    ## returns a boolean indicating whether the queue is empty. O(1) time.


