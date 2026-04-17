class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

def isPalindrome(head):
    if not head or not head.next:
        return True

    left = head
    right = head
    while right.next != None:
        right = right.next

    while left != right and left.prev != right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.prev
    return True
# time: O(n)
