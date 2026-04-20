# Question 9: DedupSortedList
# Technique: Linked list fixed-distance two-pointer
# Time: O(n)
# Space: O(1)

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


def DedupSortedList(head):
    if not head:
        return head

    cur = head

    while cur and cur.next:
        if cur.data == cur.next.data:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head


# Example 1
head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(2)
head1.next.next.next = Node(4)
head1.next.next.next.next = Node(5)
head1.next.next.next.next.next = Node(5)
head1.next.next.next.next.next.next = Node(5)
head1.next.next.next.next.next.next.next = Node(10)
head1.next.next.next.next.next.next.next.next = Node(10)


# Example 2
head2 = Node(8)
head2.next = Node(8)
head2.next.next = Node(8)
head2.next.next.next = Node(8)


def print_list(head):
    linked_list = []
    while head:
        linked_list.append(head.data)
        head = head.next
    print(linked_list)


print_list(DedupSortedList(head1))  # Expected Output:  1 -> 2 -> 4 -> 5 -> 10
print_list(DedupSortedList(head2))  # Expected Output: 8

# time: 13 minutes
