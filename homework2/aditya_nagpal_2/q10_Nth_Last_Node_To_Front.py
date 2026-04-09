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




#Given a singly linked list, move the nth from the last element to the front of the list.

# eg len(arr) = m
# the element to be movoed(k) k = m-n +1

# we got the element, now we move it to the front
# pre2->pre1->k->after
# k->pre->pre->after
# k should point towards the head (k.next = head), head = k
# prev1->after

#edge cases:
# when we dont have any node:
# return none

#when k is the head itself:
#do nothing and return head

#code
def nth_node(head, n):
    if not head:
        return None
    
    curr = head
    m = 0
    while curr:
        m += 1
        curr = curr.next

    k_element = m - n + 1

    node_number = 1
    node = head
    while node_number < k_element:
        node = node.next
        node_number += 1