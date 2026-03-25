"""
SINGLY LINKED LIST METHODS

insertAtFront(head, val)
    Time: O(1)
    Space: O(1)

insertAtBack(head, val)
    Time: O(n)
    Space: O(1)

insertAfter(head, val, loc)
    Time: O(1)
    Space: O(1)

insertBefore(head, val, loc)
    Time: O(n)
    Space: O(1)

deleteFront(head)
    Time: O(1)
    Space: O(1)

deleteBack(head)
    Time: O(n)
    Space: O(1)

deleteNode(head, loc)
    Time: O(n)
    Space: O(1)

length(head)
    Time: O(n)
    Space: O(1)

reverseIterative(head)
    Time: O(n)
    Space: O(1)

reverseRecursive(head)
    Time: O(n)
    Space: O(n) recursion stack
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertAtFront(head, val):
    newNode = Node(val)
    newNode.next = head
    return newNode


def insertAtBack(head, val):
    newNode = Node(val)

    if head is None:
        return newNode

    curr = head
    while curr.next:
        curr = curr.next

    curr.next = newNode
    return head


def insertAfter(head, val, loc):
    if loc is None:
        return head

    newNode = Node(val)
    newNode.next = loc.next
    loc.next = newNode
    return head


def insertBefore(head, val, loc):
    newNode = Node(val)

    if head == loc:
        newNode.next = head
        return newNode

    curr = head
    while curr and curr.next != loc:
        curr = curr.next

    if curr:
        newNode.next = loc
        curr.next = newNode

    return head


def deleteFront(head):
    if head is None:
        return None
    return head.next


def deleteBack(head):
    if head is None or head.next is None:
        return None

    curr = head
    while curr.next.next:
        curr = curr.next

    curr.next = None
    return head


def deleteNode(head, loc):
    if head is None:
        return None

    if head == loc:
        return head.next

    curr = head
    while curr.next and curr.next != loc:
        curr = curr.next

    if curr.next:
        curr.next = curr.next.next

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
    def helper(node, prev):
        if node is None:
            return prev

        nxt = node.next
        node.next = prev
        return helper(nxt, node)

    return helper(head, None)

def toList(head):
    curr = head
    result = []
    while curr:
        result.append(curr.data)
        curr = curr.next
    return result

def run_tests():
    # 1. Test Insert at Front
    h1 = None
    h1 = insertAtFront(h1, 10)
    h1 = insertAtFront(h1, 20)
    assert toList(h1) == [20, 10]
    print("insertAtFront passed")

    # 2. Test Insert at Back
    h2 = None
    h2 = insertAtBack(h2, 5)
    h2 = insertAtBack(h2, 15)
    assert toList(h2) == [5, 15]
    print("insertAtBack passed")

    # 3. Test Insert Before/After
    h3 = Node(1)
    h3.next = Node(3)
    insertAfter(h3, 4, h3.next)
    h3 = insertBefore(h3, 2, h3.next)
    assert toList(h3) == [1, 2, 3, 4]
    print("insertBefore/After passed")

    # 4. Test Deletions
    h4 = Node(10)
    h4.next = Node(20)
    h4.next.next = Node(30)
    h4 = deleteFront(h4)
    h4 = deleteBack(h4)
    assert toList(h4) == [20]
    print("deleteFront/Back passed")

    # 5. Test Reverse
    h5 = Node(1)
    h5.next = Node(2)
    h5.next.next = Node(3)
    h5 = reverseIterative(h5)
    assert toList(h5) == [3, 2, 1]
    h5 = reverseRecursive(h5)
    assert toList(h5) == [1, 2, 3]
    print("Reversal methods passed")

    #6. Test Length
    h6 = Node(1)
    h6.next = Node(2)
    assert length(h6) == 2
    h6 = deleteFront(h6)
    assert length(h6) == 1
    print("Length method passed")


run_tests()

# Time Spent: 40:00
