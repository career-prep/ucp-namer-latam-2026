# Technique: Doubly linked list forward-backward two-pointer
# Time Complexity: O(n)
# Space Complexity: O(1)

class DoublyListNode:
    def __init__(self, val=0):
        self.val  = val
        self.next = None
        self.prev = None

def isPalindrome(head):
    if not head:
        return True

    tail = head
    while tail.next:
        tail = tail.next

    left, right = head, tail
    while left and right and left != right and right.next != left:
        if left.val != right.val:
            return False
        left  = left.next
        right = right.prev

    return True

def build(vals):
    dummy = DoublyListNode(0)
    curr  = dummy
    for v in vals:
        node      = DoublyListNode(v)
        node.prev = curr
        curr.next = node
        curr      = curr.next
    return dummy.next

# Test 1: [9,2,4,2,9] → True
print(isPalindrome(build([9,2,4,2,9])))   # True

# Test 2: [9,12,4,2,9] → False
print(isPalindrome(build([9,12,4,2,9])))  # False

# Test 3: single node → True
print(isPalindrome(build([5])))            # True

# Test 4: even length [1,2,2,1] → True
print(isPalindrome(build([1,2,2,1])))     # True

# Time spent: ~33 minutes
