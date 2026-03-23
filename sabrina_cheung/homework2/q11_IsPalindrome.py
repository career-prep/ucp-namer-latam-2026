'''
Method: Doubly Linked List forward backward two pointer
Time: 20 min
Time Complexity: O(n)
Space Complexity: O(1)

Intuition: Use two pointers. One point at head one at tail. 
Check if both are pointing to the same value and if they are move towards the middle.
Keep moving until pointers cross each other in middle.

'''

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

def IsPalindrome(head, tail):
    while head != tail or head.prev == tail:
        if head.data != tail.data:
            return False
        head = head.next
        tail = tail.prev
    return True

# Example 1
# Input: 9 <-> 2 <-> 4 <-> 2 <-> 9
# Output: True
head1 = Node(9)
head1.next = Node(2)
head1.next.prev = head1
head1.next.next = Node(4)
head1.next.next.prev = head1.next
head1.next.next.next = Node(2)
head1.next.next.next.prev = head1.next.next
head1.next.next.next.next = Node(9)
head1.next.next.next.next.prev = head1.next.next.next
tail1 = head1.next.next.next.next


# Example 2
# Input: 9 <-> 12 <-> 4 <-> 2 <-> 9
# Output: False
head2 = Node(9)
head2.next = Node(12)
head2.next.prev = head2
head2.next.next = Node(4)
head2.next.next.prev = head2.next
head2.next.next.next = Node(2)
head2.next.next.next.prev = head2.next.next
head2.next.next.next.next = Node(9)
head2.next.next.next.next.prev = head2.next.next.next
tail2 = head2.next.next.next.next

print(IsPalindrome(head1, tail1))
print(IsPalindrome(head2, tail2))