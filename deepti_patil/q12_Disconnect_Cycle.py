# Technique: Linked list fast-slow two-pointer (Floyd's cycle detection)
# Time: O(n)
# Space: O(1)
#i understand the algorithm conceptually but the math of finding the exact cycle start gets tricky

 
# APPROACH:
# Step 1: use fast/slow pointers to detect IF there's a cycle
#   - fast moves 2 steps, slow moves 1 step
#   - if they ever meet, theres a cycle
 
# Step 2: find WHERE the cycle starts
#   - there's a math trick here: after fast and slow meet,
#     reset one pointer to head and keep the other at the meeting point
#   - advance both one step at a time - they'll meet again exactly at the cycle start
#   - i'd want to verify this on paper before writing it for sure
 
# Step 3: once we have the cycle start, walk around the cycle until we get
#   back to the node JUST BEFORE the start (the node whose .next = cycle start)
#   then set that node's .next = None to break the cycle
 
def disconnectCycle(head):
    if head is None or head.next is None:
        return head
 
    slow = head
    fast = head
 
    # step 1: detect cycle
    has_cycle = False
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break
 
    if not has_cycle:
        return head  # no cycle, nothing to disconnect
 
    # step 2: find the start of the cycle
    # reset slow to head, keep fast at meeting point
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    # now both are at the cycle start node
 
    cycle_start = slow
 
    # step 3: walk around the cycle to find the node that points back to cycle_start
    # that node is the "tail" of the cycle - we need to set its .next to None
    curr = cycle_start
    while curr.next != cycle_start:
        curr = curr.next
    curr.next = None  # break the cycle!
 
    return head
