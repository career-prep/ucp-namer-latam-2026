class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def insertAtFront(head, val):
    new_node = Node(val)

    if head:
        head.prev = new_node
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
    new_node.prev = curr

    return head


def insertAfter(head, val, loc):
    if not loc:
        return head

    new_node = Node(val)

    new_node.next = loc.next
    new_node.prev = loc

    if loc.next:
        loc.next.prev = new_node

    loc.next = new_node

    return head


def insertBefore(head, val, loc):
    if not loc:
        return head

    new_node = Node(val)

    new_node.next = loc
    new_node.prev = loc.prev

    if loc.prev:
        loc.prev.next = new_node
    else:
        head = new_node 

    loc.prev = new_node

    return head


def deleteFront(head):
    if not head:
        return None

    head = head.next

    if head:
        head.prev = None

    return head



def deleteBack(head):
    if not head:
        return None

    if not head.next:
        return None

    curr = head
    while curr.next:
        curr = curr.next

    curr.prev.next = None

    return head


def deleteNode(head, loc):
    if not head or not loc:
        return head

    if loc == head:
        return deleteFront(head)

    if loc.next:
        loc.next.prev = loc.prev

    if loc.prev:
        loc.prev.next = loc.next

    return head


def length(head):
    count = 0
    curr = head

    while curr:
        count += 1
        curr = curr.next

    return count

def reverseIterative(head):
    curr = head
    prev = None

    while curr:
        curr.prev, curr.next = curr.next, curr.prev
        prev = curr
        curr = curr.prev

    return prev


def reverseRecursive(head):
    if not head:
        return None

    head.prev, head.next = head.next, head.prev

    if not head.prev:
        return head

    return reverseRecursive(head.prev)