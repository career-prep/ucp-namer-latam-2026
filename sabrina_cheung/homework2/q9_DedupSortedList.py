'''
Method: Linked List reset/catch up two pointer
Time: 20 min
Time Complexity: O(n)
Space Complexity: O(n)

Intuition: Use two pointers. If first pointer points to the same value as second pointer, 
move second pointer until pointing to a different value and set the first pointer's next value to the second pointer.
Move first pointer to second pointer and continue.

'''

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
# Input: 1 -> 2 -> 2 -> 4 -> 5 -> 5 -> 5 -> 10 -> 10
# Expected Output: 1 -> 2 -> 4 -> 5 -> 10
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
# Input: 8 -> 8 -> 8 -> 8
# Expected Output: 8
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

print_list(DedupSortedList(head1))
print_list(DedupSortedList(head2))

