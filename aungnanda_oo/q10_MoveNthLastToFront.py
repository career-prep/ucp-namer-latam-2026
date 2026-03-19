# Question 10: MoveNthLastToFront

# Given a singly linked list, move the nth from the last element to the front of the list.

# Time Complexity = O(n) — two-pointer technique, single pass after finding length
# Space Complexity = O(1) — in-place pointer manipulation

# Examples:

# Input: 1->2->3->4->5, k=2
# Output: 4->1->2->3->5  (4 is 2nd from last, moved to front)

# Input: 1->2->3->4->5->6->7, k=7
# Output: 1->2->3->4->5->6->7  (7th from last is 1 — the head — already at front)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def build_list(vals):
    if not vals:
        return None
    head = Node(vals[0])
    cur = head
    for v in vals[1:]:
        cur.next = Node(v)
        cur = cur.next
    return head


def list_to_str(head):
    result = []
    cur = head
    while cur:
        result.append(str(cur.data))
        cur = cur.next
    return "->".join(result) if result else "[]"


def MoveNthLastToFront(head, k):
    if not head or not head.next:
        return head

    # Use two pointers separated by k steps
    # We also need a pointer to the node BEFORE the target to unlink it
    dummy = Node(0)
    dummy.next = head

    fast = dummy
    slow = dummy

    # Advance fast by k+1 steps so that when fast reaches the end,
    # slow is at the node BEFORE the nth-from-last
    for _ in range(k + 1):
        if not fast:
            return head  # k is out of range
        fast = fast.next

    # If fast is None after advancing k+1 steps, nth from last is the head
    if not fast:
        # head is already at front, nothing to do (or k == length)
        return head

    while fast:
        fast = fast.next
        slow = slow.next

    # slow is now the node BEFORE the target
    target = slow.next
    slow.next = target.next  # unlink target

    # Move target to front
    target.next = dummy.next
    dummy.next = target

    return dummy.next


# --- Tests ---

# Test 1: k=2, move 2nd from last (4) to front
head = build_list([1, 2, 3, 4, 5])
print("Test 1 input: ", list_to_str(head))
print("Test 1 output:", list_to_str(MoveNthLastToFront(head, 2)))  # 4->1->2->3->5

# Test 2: k=1, move last element to front
head = build_list([1, 2, 3, 4, 5])
print("Test 2 input: ", list_to_str(head))
print("Test 2 output:", list_to_str(MoveNthLastToFront(head, 1)))  # 5->1->2->3->4

# Test 3: k=5 (length), move head — stays in place
head = build_list([1, 2, 3, 4, 5])
print("Test 3 input: ", list_to_str(head))
print("Test 3 output:", list_to_str(MoveNthLastToFront(head, 5)))  # 1->2->3->4->5

# Test 4: k=3, move middle element to front
head = build_list([10, 20, 30, 40, 50])
print("Test 4 input: ", list_to_str(head))
print("Test 4 output:", list_to_str(MoveNthLastToFront(head, 3)))  # 30->10->20->40->50

# Test 5: single element
head = build_list([7])
print("Test 5 output:", list_to_str(MoveNthLastToFront(head, 1)))  # 7

# Spent a total of 25 mins on this question
