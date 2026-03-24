#Time: O(n)
#Space: O(1)

import unittest

class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev  

def is_palindrome(head):
    if not head:
        return True

    curr = head 
    left = head

    while curr.next:
        curr = curr.next
    right = curr 

    while left is not right and left.prev is not right:
        if left.val != right.val:
            return False
        else:
            left = left.next
            right = right.prev
    return True

#Time-taken: 20 minutes
class TestIsPalindrome(unittest.TestCase):

    def build_doubly_linked_list(self, values):
        if not values:
            return None
        
        head = ListNode(values[0])
        curr = head
        
        for val in values[1:]:
            new_node = ListNode(val)
            curr.next = new_node
            new_node.prev = curr
            curr = new_node
        
        return head

    def test_empty_list(self):
        head = None
        self.assertTrue(is_palindrome(head))

    def test_single_node(self):
        head = self.build_doubly_linked_list([1])
        self.assertTrue(is_palindrome(head))

    def test_even_palindrome(self):
        head = self.build_doubly_linked_list([1, 2, 2, 1])
        self.assertTrue(is_palindrome(head))

    def test_odd_palindrome(self):
        head = self.build_doubly_linked_list([1, 2, 3, 2, 1])
        self.assertTrue(is_palindrome(head))

    def test_not_palindrome(self):
        head = self.build_doubly_linked_list([1, 2, 3])
        self.assertFalse(is_palindrome(head))


if __name__ == "__main__":
    unittest.main()