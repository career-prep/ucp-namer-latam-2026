class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtFront(head, val):
    new_node = Node(val)
    new_node.next = head
    return new_node

def insertAtBack(head, val):
    new_node = Node(val)

    if not head:
        return new_node

    curr = head
    while curr.next:
        curr = curr.next

    curr.next = new_node
    return head

def insertAfter(head, val, loc):
    if not loc:
        return head

    new_node = Node(val)
    new_node.next = loc.next
    loc.next = new_node

    return head

def insertBefore(head, val, loc):
    if not head or not loc:
        return head

    if head == loc:
        return insertAtFront(head, val)

    prev = None
    curr = head

    while curr and curr != loc:
        prev = curr
        curr = curr.next

    if curr == loc:
        new_node = Node(val)
        prev.next = new_node
        new_node.next = curr

    return head


def deleteFront(head):
    if not head:
        return None
    return head.next


def deleteBack(head):
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
    if not head or not loc:
        return head

    if head == loc:
        return head.next

    prev = None
    curr = head

    while curr and curr != loc:
        prev = curr
        curr = curr.next

    if curr == loc:
        prev.next = curr.next

    return head



def length(head):
    count = 0
    curr = head

    while curr:
        count += 1
        curr = curr.next

    return count


def reverseIterative(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


def reverseRecursive(head):
    if not head or not head.next:
        return head

    new_head = reverseRecursive(head.next)

    head.next.next = head
    head.next = None

    return new_head