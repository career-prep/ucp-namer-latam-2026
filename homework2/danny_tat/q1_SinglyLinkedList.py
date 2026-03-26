# Question 1: Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertAtFront(head, val):
    # Time and Space: O(1)
    new_node = Node(val)
    new_node.next = head
    return new_node


def insertAtBack(head, val):
    # Time: O(n) and Space: O(1)
    new_node = Node(val)
    if not head:
        return new_node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    return head


def insertAfter(head, val, loc):
    # Time: O(n) and Space: O(1)
    if not loc:
        return head
    new_node = Node(val)
    new_node.next = loc.next
    loc.next = new_node
    return head


def insertBefore(head, val, loc):
    # Time: O(n) — must traverse to find node before loc and Space: O(1)
    if not head or not loc:
        return head
    if head == loc:
        return insertAtFront(head, val)

    curr = head
    while curr and curr.next != loc:
        curr = curr.next

    if curr:
        new_node = Node(val)
        new_node.next = loc
        curr.next = new_node
    return head


def deleteFront(head):
    # Time and Space: O(1)
    if not head:
        return None
    return head.next


def deleteBack(head):
    # Time: O(n) — must traverse to second-to-last node and Space: O(1)
    if not head:
        return None
    if not head.next:
        return None
    curr = head
    while curr.next.next:
        curr = curr.next
    curr.next = None
    return head


def deleteNode(head, loc):
    # Time: O(n) — must traverse to find node before loc and Space: O(1)
    if not head or not loc:
        return head
    if head == loc:
        return head.next

    curr = head
    while curr and curr.next != loc:
        curr = curr.next

    if curr:
        curr.next = loc.next
    return head


def length(head):
    # Time: O(n) and Space: O(1)
    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next
    return count


def reverseIterative(head):
    # Time: O(n) and Space: O(1)
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def reverseRecursive(head):
    # Time: O(n) and Space: O(n) — recursion stack depth is n
    def _helper(curr, prev):
        if not curr:
            return prev
        next_node = curr.next
        curr.next = prev
        return _helper(next_node, curr)

    return _helper(head, None)

# time: 35 minutes
