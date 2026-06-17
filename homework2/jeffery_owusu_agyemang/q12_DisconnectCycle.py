"""
Technique: Linked list fast-slow two-pointer
Time Complexity: O(n) - Linear scan to find and break the cycle.
Space Complexity: O(1) - Constant space pointers.
Time spent: 40 minutes
"""

from homework2.jeffery_owusu_agyemang.q9_DedupSortedList import ListNode

def disconnect_cycle(head):
    if not head or not head.next:
        return head
    slow = head
    fast = head
    
    # if cycle exists
    has_cycle = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break
    if not has_cycle:
        return head

    slow = head
    if slow == fast:
        while fast.next != slow:
            fast = fast.next
    else:
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next
    fast.next = None
    return head

# --- Test Cases ---
if __name__ == "__main__":
    # Create: 1 -> 2 -> 3 -> 4 -> (back to 2)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2; node2.next = node3; node3.next = node4; node4.next = node2
    
    disconnect_cycle(node1)
    
    # Check if node4.next is now None
    print(f"Node 4 next is None? {node4.next == None}") # Expected: True