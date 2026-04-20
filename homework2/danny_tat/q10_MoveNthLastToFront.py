# Question 10: MoveNthLastToFront
# Technique: Linked list fixed-distance two-pointer
# Time: O(n)
# Space: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def moveNthLastToFront(head, k):
    if not head or not head.next:
        return head

    length = 0
    cur = head

    while cur:
        length += 1
        cur = cur.next

    target = length - k

    if target == 0:
        return head

    prev = head

    for _ in range(target - 1):
        prev = prev.next

    target_node = prev.next
    prev.next = target_node.next
    target_node.next = head
    return target_node


def print_list(head):
    result = []
    while head:
        result.append(head.data)
        head = head.next
    print(result)


# Example 1
k1 = 2
head1 = Node(15)
head1.next = Node(2)
head1.next.next = Node(8)
head1.next.next.next = Node(7)
head1.next.next.next.next = Node(20)
head1.next.next.next.next.next = Node(9)
head1.next.next.next.next.next.next = Node(11)
head1.next.next.next.next.next.next.next = Node(6)
head1.next.next.next.next.next.next.next.next = Node(19)

# Expected Output: [6, 15, 2, 8, 7, 20, 9, 11, 19]
head1 = moveNthLastToFront(head1, k1)
print_list(head1)

# Example 2
k2 = 7
head2 = Node(15)
head2.next = Node(2)
head2.next.next = Node(8)
head2.next.next.next = Node(7)
head2.next.next.next.next = Node(20)
head2.next.next.next.next.next = Node(9)
head2.next.next.next.next.next.next = Node(11)
head2.next.next.next.next.next.next.next = Node(6)
head2.next.next.next.next.next.next.next.next = Node(19)

# Expected Output: [8, 15, 2, 7, 20, 9, 11, 6, 19]
head2 = moveNthLastToFront(head2, k2)
print_list(head2)

# time: 28 minutes
