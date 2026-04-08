class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def insertAtFront(head, val):  # O(1)
    new_node = Node(val)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node


def insertAtBack(head, tail, val):  # O(1)
    new_node = Node(val)
    if not head:
        return new_node, new_node
    new_node.prev = tail
    tail.next = new_node
    return head, new_node


def insertAfter(head, val, loc):  # O(1)
    new_node = Node(val)
    new_node.next = loc.next
    new_node.prev = loc
    if loc.next:
        loc.next.prev = new_node
    loc.next = new_node
    return head


def insertBefore(head, val, loc):  # O(1)
    new_node = Node(val)
    new_node.next = loc
    new_node.prev = loc.prev
    if loc.prev:
        loc.prev.next = new_node
    else:
        head = new_node
    loc.prev = new_node
    return head


def deleteFront(head):  # O(1)
    if not head:
        return None
    head = head.next
    if head:
        head.prev = None
    return head


def deleteBack(head, tail):  # O(1)
    if not head:
        return None, None
    if not tail.prev:
        return None, None
    tail.prev.next = None
    new_tail = tail.prev
    return head, new_tail


def deleteNode(head, loc):  # O(1)
    if not head or not loc:
        return head
    if loc.prev:
        loc.prev.next = loc.next
    else:
        head = loc.next
    if loc.next:
        loc.next.prev = loc.prev
    return head


def length(head):  # O(n)
    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next
    return count


def reverseIterative(head):  # O(n)
    curr = head
    new_head = None
    while curr:
        next_node = curr.next
        curr.next = curr.prev
        curr.prev = next_node
        new_head = curr
        curr = next_node
    return new_head


def reverseRecursive(head):  # O(n)
    def helper(node):
        if not node:
            return None
        next_node = node.next
        node.next = node.prev
        node.prev = next_node
        if not next_node:
            return node
        return helper(next_node)
    return helper(head)


def printList(head):
    result = []
    curr = head
    while curr:
        result.append(str(curr.data))
        curr = curr.next
    print(" <-> ".join(result))


print("DoublyLinkedList Results:")

head, tail = None, None
for v in [1, 2, 3, 4, 5]:
    head, tail = insertAtBack(head, tail, v)
printList(head)

head = insertAtFront(head, 0)
printList(head)

node3 = head.next.next.next
head = insertAfter(head, 99, node3)
printList(head)

head = insertBefore(head, 88, node3)
printList(head)

head = deleteFront(head)
printList(head)

head, tail = deleteBack(head, tail)
printList(head)

head = deleteNode(head, node3)
printList(head)

print(length(head))

head = reverseIterative(head)
printList(head)

head = reverseRecursive(head)
printList(head)
