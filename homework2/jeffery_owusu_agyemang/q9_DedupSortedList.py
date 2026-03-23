"""
Technique: Simultaneous iteration two-pointer (Current and Next)
Time Complexity: O(n) - traverse the list exactly once.
Space Complexity: O(1)
Time spent: 17 minutes
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def dedup_sorted_list(head):
    if not head:
        return None
    current = head
    
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head

# --- Test Cases ---
def print_list(head):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" -> ".join(vals) if vals else "Empty")

if __name__ == "__main__":
    # Test: 1 -> 1 -> 2 -> 3 -> 3
    test_list = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    print("Before Dedup:")
    print_list(test_list)
    
    deduped = dedup_sorted_list(test_list)
    print("After Dedup:")
    print_list(deduped) # Expected: 1 -> 2 -> 3