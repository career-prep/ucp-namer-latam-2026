#Move Nth Last to front
#Time Complexity: O(n) where n is the length of the list
#Space Complexity: O(1)
#Technique: Linked List Fixed-Distance Two-Pointer
#Time Spent: 20 minutes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def MoveNthLastToFront(head, n):
    if not head or not head.next:
        return head
    
    prev = head
    curr = head

    for i in range(n):
        curr = curr.next

    if not curr:
        return head 

    while curr.next:
        curr = curr.next
        prev = prev.next
    
    newHead = prev.next
    prev.next = prev.next.next
    newHead.next = head
    head = newHead

    return head


def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> " if curr.next else "\n")
        curr = curr.next


# Test Case 1
# Input: 15 -> 2 -> 8 -> 7 -> 20 -> 9 -> 11 -> 6 -> 19, k = 2
# Output: 6 -> 15 -> 2 -> 8 -> 7 -> 20 -> 9 -> 11 -> 19
head1 = Node(15)
head1.next = Node(2)
head1.next.next = Node(8)
head1.next.next.next = Node(7)
head1.next.next.next.next = Node(20)
head1.next.next.next.next.next = Node(9)
head1.next.next.next.next.next.next = Node(11)
head1.next.next.next.next.next.next.next = Node(6)
head1.next.next.next.next.next.next.next.next = Node(19)

print_list(MoveNthLastToFront(head1, 2))

# Test Case 2
# Input: 15 -> 2 -> 8 -> 7 -> 20 -> 9 -> 11 -> 6 -> 19, k = 7
# Output: 8 -> 15 -> 2 -> 7 -> 20 -> 9 -> 11 -> 6 -> 19
head2 = Node(15)
head2.next = Node(2)
head2.next.next = Node(8)
head2.next.next.next = Node(7)
head2.next.next.next.next = Node(20)
head2.next.next.next.next.next = Node(9)
head2.next.next.next.next.next.next = Node(11)
head2.next.next.next.next.next.next.next = Node(6)
head2.next.next.next.next.next.next.next.next = Node(19)

print_list(MoveNthLastToFront(head2, 7))