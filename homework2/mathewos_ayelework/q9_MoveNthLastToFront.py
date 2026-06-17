# Technique used: Linked list fixed-distance two-pointer
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def moveNthLastToFront(head, k):
    fast = head
    slow = head
    prev = None

    for _ in range(k):
        fast = fast.next

    while fast:
        prev = slow
        slow = slow.next
        fast = fast.next

    if prev:
        prev.next = slow.next
    else:
        return head

    slow.next = head
    return slow


def buildList(vals):
    head = None
    prev_node = None
    for v in vals:
        node = Node(v)
        if not head:
            head = node
        else:
            prev_node.next = node
        prev_node = node
    return head


def printList(head):
    result = []
    curr = head
    while curr:
        result.append(str(curr.data))
        curr = curr.next
    print(" -> ".join(result))


print("moveNthLastToFront Results:")

vals = [15, 2, 8, 7, 20, 9, 11, 6, 19]

printList(moveNthLastToFront(buildList(vals), 2))
printList(moveNthLastToFront(buildList(vals), 7))
printList(moveNthLastToFront(buildList([1, 2, 3, 4, 5]), 1))
printList(moveNthLastToFront(buildList([1, 2, 3]), 3))

# Time Taken: 30 mins
