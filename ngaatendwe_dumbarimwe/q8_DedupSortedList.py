#Time: O(n)
#Space: O(1)

import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def dedup_sorted_list(head):
    if not head:   
        return None

    curr = head 

    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next 
    return head 

#Time-taken: 15 minutes
class TestDedupSortedList(unittest.TestCase):

    def list_to_array(self, head):
        result = []
        curr = head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result

    def test_empty_list(self):
        head = None
        result = dedup_sorted_list(head)
        self.assertIsNone(result)

    def test_single_node(self):
        head = ListNode(1)
        result = dedup_sorted_list(head)
        self.assertEqual(self.list_to_array(result), [1])

    def test_no_duplicates(self):
        head = ListNode(1, ListNode(2, ListNode(3)))
        result = dedup_sorted_list(head)
        self.assertEqual(self.list_to_array(result), [1, 2, 3])

    def test_with_duplicates(self):
        head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
        result = dedup_sorted_list(head)
        self.assertEqual(self.list_to_array(result), [1, 2, 3])

    def test_all_duplicates(self):
        head = ListNode(1, ListNode(1, ListNode(1, ListNode(1))))
        result = dedup_sorted_list(head)
        self.assertEqual(self.list_to_array(result), [1])


if __name__ == "__main__":
    unittest.main()