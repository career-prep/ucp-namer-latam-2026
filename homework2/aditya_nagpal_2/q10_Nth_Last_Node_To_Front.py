# Approach:
# Use two pointers (fast and slow)
# Move fast n steps ahead
# Then move both until fast reaches end
# Remove nth from last and move it to front

# Time Complexity: O(n)
# Space Complexity: O(1)

def moveNthLastToFront(head, n):
    if not head or n == 0:
        return head

    fast = head
    slow = head

    # Move fast n steps ahead
    for _ in range(n):
        if not fast:
            return head  # n > length
        fast = fast.next

    # If fast is None → nth from last is head
    if not fast:
        return head

    # Move both pointers
    while fast.next:
        fast = fast.next
        slow = slow.next

    # slow is before the target node
    target = slow.next
    slow.next = target.next

    # move target to front
    target.next = head
    head = target

    return head