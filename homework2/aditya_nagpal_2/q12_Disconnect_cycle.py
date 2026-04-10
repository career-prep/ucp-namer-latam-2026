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

#check if the given linkedlist has cycle and disconnect the cycle
# there will exist a cycle if there is no tail
#two pointer 
# approach:
# slow_pointer = fast_pointer = head
#iterate until slow and fast and fast.next exist
#find the point where both slow and fast meet set slow to fast and iterate again until slow.next == fast and point slow .next to none
#edge cases:
  ## if not head: return none
  ## if head.next is none: return no cycle

def disconnect(head):
    slow = fast = head

    if not head: return "no cycle"
    if not head.next: return "no cycle"

    while slow and fast and fast.next:
        slow = slow.next
        fast  = fast.next.next

        if slow == fast:
            slow = head

            while slow != fast:
                slow = slow.next
                fast = fast.next

            fast = fast.next
            while fast.next != slow:
                fast = fast.next

            fast.next = None
           

    return head
