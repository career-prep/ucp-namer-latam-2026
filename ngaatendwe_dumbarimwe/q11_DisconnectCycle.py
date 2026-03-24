#Time: O(n)
#Space: O(n)

import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def disconnect_cycle(head):
    if not head:
        return None

    sett = set()
    sett.add(head)
    curr = head

    while curr and curr.next:
        node = curr.next 
        if node in sett:
            curr.next = None 
            break
        else:
            sett.add(node)
            curr = curr.next 
    
    return head

#Time-taken: 20 minutes
class TestDisconnectCycle(unittest.TestCase):

    def list_to_array(self, head, limit=20):
        """Convert list to array (limit prevents infinite loop if cycle not removed)"""
        result = []
        curr = head
        count = 0
        while curr and count < limit:
            result.append(curr.val)
            curr = curr.next
            count += 1
        return result

    def test_empty_list(self):
        head = None
        result = disconnect_cycle(head)
        self.assertIsNone(result)

    def test_no_cycle(self):
        head = ListNode(1, ListNode(2, ListNode(3)))
        result = disconnect_cycle(head)
        self.assertEqual(self.list_to_array(result), [1, 2, 3])

    def test_cycle_at_end(self):
        head = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)

        head.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2  

        result = disconnect_cycle(head)
        self.assertEqual(self.list_to_array(result), [1, 2, 3, 4])

    def test_cycle_to_head(self):
        head = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)

        head.next = node2
        node2.next = node3
        node3.next = head  

        result = disconnect_cycle(head)
        self.assertEqual(self.list_to_array(result), [1, 2, 3])

    def test_single_node_cycle(self):
        head = ListNode(1)
        head.next = head

        result = disconnect_cycle(head)
        self.assertEqual(self.list_to_array(result), [1])


if __name__ == "__main__":
    unittest.main()
            