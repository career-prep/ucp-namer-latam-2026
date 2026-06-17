# Technique: Simultaneous iteration two-pointer
# Time: O(n)
# Space: O(1)
# Time Spent: 20 minutes


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


# Test cases
def printList(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")


head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(2)
head1.next.next.next = Node(4)
head1.next.next.next.next = Node(5)
head1.next.next.next.next.next = Node(5)
head1.next.next.next.next.next.next = Node(5)
head1.next.next.next.next.next.next.next = Node(10)
head1.next.next.next.next.next.next.next.next = Node(10)

head1 = dedupSortedList(head1)
printList(head1)


head2 = Node(8)
head2.next = Node(8)
head2.next.next = Node(8)
head2.next.next.next = Node(8)

head2 = dedupSortedList(head2)
printList(head2)