class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


def isPalindrome(head): # O(n) time complexity and O(1) space complexity
    right = head

    while right.next:
        right = right.next

    left = head

    while left != right and right.next != left:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next  

    return True
    #This solution took me 14 minutes