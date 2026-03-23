'''
Method: Linked List fixed distance two pointer
Time: 20 min
Time Complexity: O(n)
Space Complexity: O(n)

Intuition: Use two pointers. Move the first pointer such that they have a distance k. 
Move both pointers forward until first pointer hits the tail. 
Move the node pointed to by the second pointer to the head.

'''

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def MoveNthLastToFront(head, k):
    cur = head
    nth = head
    prev = None
    count = 1

    while count != k:
        cur = cur.next
        count += 1
    while cur.next:
        cur = cur.next
        prev = nth
        nth = nth.next

    prev.next = nth.next
    nth.next = head
    head = nth
    return head

def print_list(head):
    linked_list = []
    while head:
        linked_list.append(head.data)
        head = head.next
    print(linked_list)


# Example 1
# Input: k = 2
# 15 -> 2 -> 8 -> 7 -> 20 -> 9 -> 11 -> 6 -> 19
# Expected Output:
# 6 -> 15 -> 2 -> 8 -> 7 -> 20 -> 9 -> 11 -> 19
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


# Example 2
# Input: k = 7
# 15 -> 2 -> 8 -> 7 -> 20 -> 9 -> 11 -> 6 -> 19
# Expected Output:
# 8 -> 15 -> 2 -> 7 -> 20 -> 9 -> 11 -> 6 -> 19
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

print_list(MoveNthLastToFront(head1, k1))
print_list(MoveNthLastToFront(head2, k2))