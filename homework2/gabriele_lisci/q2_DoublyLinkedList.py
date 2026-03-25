"""
DOUBLY LINKED LIST METHODS

insertAtFront(head, val)
    Time: O(1)
    Space: O(1)

insertAtBack(head, tail, val)
    Time: O(1)
    Space: O(1)

insertAfter(head, val, loc)
    Time: O(1)
    Space: O(1)

insertBefore(head, val, loc)
    Time: O(1)
    Space: O(1)

deleteFront(head)
    Time: O(1)
    Space: O(1)

deleteBack(head, tail)
    Time: O(1)
    Space: O(1)

deleteNode(head, loc)
    Time: O(1)
    Space: O(1)

length(head)
    Time: O(n)
    Space: O(1)

reverseIterative(head)
    Time: O(n)
    Space: O(1)

reverseRecursive(head)
    Time: O(n)
    Space: O(n)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def insertAtFront(head, val):
    newNode = Node(val)
    newNode.next = head
    if head:
        head.prev = newNode
    return newNode


def insertAtBack(head, val):
    newNode = Node(val)
    if head is None:
        return newNode

    curr = head
    while curr.next:
        curr = curr.next

    curr.next = newNode
    newNode.prev = curr
    return head


def insertAfter(head, val, loc):
    if loc is None:
        return head

    newNode = Node(val)
    newNode.next = loc.next
    newNode.prev = loc

    if loc.next:
        loc.next.prev = newNode
    loc.next = newNode
    return head


def insertBefore(head, val, loc):
    if loc is None:
        return head

    newNode = Node(val)
    newNode.next = loc
    newNode.prev = loc.prev

    if loc.prev:
        loc.prev.next = newNode
    else:
        head = newNode

    loc.prev = newNode
    return head


def deleteFront(head):
    if head is None:
        return None

    newHead = head.next
    if newHead:
        newHead.prev = None
    return newHead


def deleteBack(head):
    if head is None or head.next is None:
        return None

    curr = head
    while curr.next:
        curr = curr.next

    if curr.prev:
        curr.prev.next = None
    return head


def deleteNode(head, loc):
    if head is None or loc is None:
        return head

    if head == loc:
        head = loc.next

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
    new_head = None
    while curr:
        new_head = curr
        curr.next, curr.prev = curr.prev, curr.next
        curr = curr.prev
    return new_head


def reverseRecursive(head):
    if head is None:
        return None

    head.next, head.prev = head.prev, head.next

    if head.prev is None:
        return head

    return reverseRecursive(head.prev)


def toList(head):
    curr = head
    result = []
    while curr:
        result.append(curr.data)
        curr = curr.next
    return result


def toListReverse(head):
    if not head: return []
    curr = head
    while curr.next:
        curr = curr.next

    result = []
    while curr:
        result.append(curr.data)
        curr = curr.prev
    return result


def run_tests():
    # 1. Test Insert at Front
    h1 = None
    h1 = insertAtFront(h1, 10)
    h1 = insertAtFront(h1, 20)
    assert toList(h1) == [20, 10]
    assert toListReverse(h1) == [10, 20]
    print("insertAtFront passed")

    # 2. Test Insert at Back
    h2 = None
    h2 = insertAtBack(h2, 5)
    h2 = insertAtBack(h2, 15)
    assert toList(h2) == [5, 15]
    assert toListReverse(h2) == [15, 5]
    print("insertAtBack passed")

    # 3. Test Insert Before/After
    h3 = Node(1)
    h3.next = Node(3)
    h3.next.prev = h3
    insertAfter(h3, 4, h3.next)
    h3 = insertBefore(h3, 2, h3.next)
    assert toList(h3) == [1, 2, 3, 4]
    assert toListReverse(h3) == [4, 3, 2, 1]
    print("insertBefore/After passed")

    # 4. Test Deletions
    h4 = Node(10)
    n20 = Node(20)
    n30 = Node(30)
    h4.next = n20; n20.prev = h4
    n20.next = n30; n30.prev = n20

    h4 = deleteFront(h4)
    h4 = deleteBack(h4)
    assert toList(h4) == [20]
    assert h4.prev is None
    print("deleteFront/Back passed")

    # 5. Test Reverse
    h5 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    h5.next = n2; n2.prev = h5
    n2.next = n3; n3.prev = n2

    h5 = reverseIterative(h5)
    assert toList(h5) == [3, 2, 1]
    assert toListReverse(h5) == [1, 2, 3]

    h5 = reverseRecursive(h5)
    assert toList(h5) == [1, 2, 3]
    assert toListReverse(h5) == [3, 2, 1]
    print("Reversal methods passed")

    # 6. Test Length
    h6 = Node(1)
    h6.next = Node(2)
    h6.next.prev = h6
    assert length(h6) == 2
    h6 = deleteFront(h6)
    assert length(h6) == 1
    print("Length method passed")


run_tests()

# Time spent: 20:00
