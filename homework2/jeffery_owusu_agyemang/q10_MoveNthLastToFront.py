"""
Technique: Linked list fixed-distance two-pointer
Time Complexity: O(n) - Single pass through the list.
Space Complexity: O(1) - Constant space used.
Time spent: 29 minutes
"""

def move_nth_last_to_front(head, n):
    if not head or not head.next or n <= 0:
        return head
    fast = head
    for _ in range(n):
        if not fast: return head # n is larger than list length
        fast = fast.next
    if not fast:
        return head
    slow = head

    while fast.next:
        slow = slow.next
        fast = fast.next
    target = slow.next
    slow.next = target.next
    target.next = head  
    head = target           

    return head

# --- Test Cases ---
if __name__ == "__main__":
    # Test: 1 -> 2 -> 3 -> 4 -> 5, k=2
    # 2nd from last is '4'
    test_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("Original List:")
    print_list(test_list)
    
    new_head = move_nth_last_to_front(test_list, 2)
    print("After Moving 2nd Last to Front:")
    print_list(new_head) # Expected: 4 -> 1 -> 2 -> 3 -> 5