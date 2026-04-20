# Technique: Hash linked list nodes
# Time Complexity: O(n)
# Space Complexity: O(n)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def disconnectCycle(head):
    if not head:
        return head

    visited = set()
    curr = head
    prev = None

    while curr:
        if curr in visited:
            # cycle detected → break it
            prev.next = None
            return head
        
        visited.add(curr)
        prev = curr
        curr = curr.next

    return head

# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)

# # create cycle: 30 → 10
# head.next.next.next = head
# disconnectCycle(head)

