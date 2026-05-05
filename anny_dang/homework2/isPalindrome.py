class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def isPalindrome(head, tail):
    """
    Given a doubly linked list, determine whether it is a palindrome.
    Return True or False.

    Idea: use two pointers from both ends (head and tail).
    Compare values while moving inward; if any mismatch appears,
    return False, otherwise True.

    Time: O(n)
    Space: O(1)
    """
    l, r = head, tail

    while l != r and l.prev != r:
        if l.data != r.data:
            return False
        
        l = l.next
        r = r.prev
    
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

print(isPalindrome(head1, tail1))
print(isPalindrome(head2, tail2))
