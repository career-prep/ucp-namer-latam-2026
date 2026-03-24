#Time: O(n)
#Space: O(1)

import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def move_node(head, k):
    if not head or not head.next:
        return head

    curr = head 
    length = 0

    while curr:
        length += 1
        curr = curr.next
    
    if k == length:
        return head 
    
    prev_pos = length - k
    curr = head

    for _ in range(prev_pos - 1):
        curr = curr.next
    
    temp = curr.next
    curr.next = temp.next
    temp.next = head 

    return temp 

#Time-taken: 25 minutes

class TestMoveNode(unittest.TestCase):

    def list_to_array(self, head):
        result = []
        curr = head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result

    def test_single_node(self):
        head = ListNode(1)
        result = move_node(head, 1)
        self.assertEqual(self.list_to_array(result), [1])

    def test_move_last_to_front(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        result = move_node(head, 1)
        self.assertEqual(self.list_to_array(result), [4, 1, 2, 3])

    def test_move_middle_node(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        result = move_node(head, 2)
        self.assertEqual(self.list_to_array(result), [4, 1, 2, 3, 5])

    def test_k_equals_length(self):
        head = ListNode(1, ListNode(2, ListNode(3)))
        result = move_node(head, 3)
        self.assertEqual(self.list_to_array(result), [1, 2, 3])

    def test_two_nodes(self):
        head = ListNode(1, ListNode(2))
        result = move_node(head, 1)
        self.assertEqual(self.list_to_array(result), [2, 1])


if __name__ == "__main__":
    unittest.main()
