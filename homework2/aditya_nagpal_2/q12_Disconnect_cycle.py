# Approach:
# 1. Use slow and fast pointers to detect a cycle (Floyd’s cycle detection)
# 2. If no cycle → return head
# 3. If cycle exists:
#    - Move slow to head
#    - Move both slow and fast one step at a time
#    - They meet at the start of the cycle
# 4. To remove the cycle:
#    - Find the node just before the cycle start
#    - Set its next to None

# Time Complexity: O(n)
# Space Complexity: O(1)

def removeCycle(head):
    if not head or not head.next:
        return head

    slow = head
    fast = head

    # Step 1: detect cycle
    cycle_exists = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            cycle_exists = True
            break

    if not cycle_exists:
        return head

    # Step 2: find start of cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # slow (or fast) is now at start of cycle

    # Step 3: find last node in cycle
    prev = fast
    while prev.next != slow:
        prev = prev.next

    # Step 4: break the cycle
    prev.next = None

    return head