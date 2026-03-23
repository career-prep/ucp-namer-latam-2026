class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None  # top of stack

    def top(self):                      
        if self.head is None:
            return -1
        return self.head.val

    def push(self, x):                  
        node = Node(x)
        node.next = self.head
        self.head = node

    def pop(self):                      
        if self.head is None:
            return -1
        val = self.head.val
        self.head = self.head.next
        return val

    def isEmpty(self):                  
        return self.head is None


# --- Tests ---
s = Stack()

# Test 1: isEmpty on new stack
print(s.isEmpty())       # True

# Test 2: push and top
s.push(10)
s.push(20)
s.push(30)
print(s.top())           # 30 (last in, first out)

# Test 3: pop returns top
print(s.pop())           # 30
print(s.pop())           # 20

# Test 4: top after pops
print(s.top())           # 10

# Test 5: isEmpty when not empty
print(s.isEmpty())       # False

# Test 6: pop last item
print(s.pop())           # 10

# Test 7: isEmpty after all removed
print(s.isEmpty())       # True

# Test 8: pop on empty stack
print(s.pop())           # -1

# Test 9: top on empty stack
print(s.top())           # -1