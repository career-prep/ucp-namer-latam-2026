# Technique used: Linked list reset/catch-up two-pointer
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def dedupSortedList(head):
    curr = head
    while curr and curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head


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


print("dedupSortedList Results:")

printList(dedupSortedList(buildList([1, 2, 2, 4, 5, 5, 5, 10, 10])))
printList(dedupSortedList(buildList([8, 8, 8, 8])))
printList(dedupSortedList(buildList([1, 2, 3, 4])))
printList(dedupSortedList(buildList([5])))

# Time Taken: 15 mins
