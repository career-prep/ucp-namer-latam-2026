class Stack:

    def __init__(self):
        self.items = []

    # Returns the top item in the stack. O(1) time.
    def top(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None
        

    # adds x to the top of the stack. O(1) time.
    def push(self, x):
        self.items.append(x)

    
    # removes and returns the top item in the stack. O(1) time.
    def pop(self):
        if not self.isEmpty():
            x = self.items.pop()
            return x
        else:
            return None
        
    
    # Returns a boolean indicating whether the stack is empty. O(1) time.
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False