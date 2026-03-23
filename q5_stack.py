def Stack:
    def __init__(self):
        self._s = []
        self._head = 0

    def top(self):
        return self._s[self._head]
    ## returns the top item in the stack. O(1) time.

    def push(self, x)
        self._s.insert(0,x)
    ## adds x to the top of the stack. O(1) time.

    def pop(self) 
        top = self._s[self._head]
        del self._s[0]
        return top
    ## removes and returns the top item in the stack. O(1) time.

    def isEmpty(self) 
        if len(self._s) == 0:
            return True
        return False
    ## returns a boolean indicating whether the stack is empty. O(1) time.


