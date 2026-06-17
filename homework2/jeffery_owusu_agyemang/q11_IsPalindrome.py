"""
Technique: Doubly linked list forward-backward two-pointer
Time Complexity: O(n)
Space Complexity: O(1)
time spent: 41 minutes
"""

class DLLNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

def is_palindrome(head):
    if not head:
        return True
    
    left = head
    right = head
    while right.next:
        right = right.next

    while left != right and left.prev != right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.prev
    return True

# --- Test Cases ---
if __name__ == "__main__":
    # Test 1: Palindrome 1 <-> 2 <-> 1
    n1 = DLLNode(1)
    n2 = DLLNode(2)
    n3 = DLLNode(1)
    n1.next = n2; n2.prev = n1; n2.next = n3; n3.prev = n2
    print(f"Test 1 (1-2-1): {is_palindrome(n1)}") # Expected: True

    # Test 2: Not Palindrome 1 <-> 2 <-> 3
    m1 = DLLNode(1); m2 = DLLNode(2); m3 = DLLNode(3)
    m1.next = m2; m2.prev = m1; m2.next = m3; m3.prev = m2
    print(f"Test 2 (1-2-3): {is_palindrome(m1)}") # Expected: False