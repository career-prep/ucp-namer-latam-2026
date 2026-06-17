# Technique: Doubly linked list forward-backward two-pointer
# time complexity: O(n)
# space complexity: O(1)
# 15 minutes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def isPalindrome(head):
    if not head:
        return True

    # find tail
    tail = head
    while tail.next:
        tail = tail.next

    left = head
    right = tail

    # advance inward until pointers meet or cross
    # odd length: left == right at center
    # even length: right.next == left after they've crossed
    while left != right and right.next != left:
        if left.data != right.data:
            return False
        left = left.next
        right = right.prev

    # check the final center element(s)
    return left.data == right.data

# helper
def from_list(lst):
    if not lst:
        return None
    head = Node(lst[0])
    curr = head
    for val in lst[1:]:
        new_node = Node(val)
        new_node.prev = curr
        curr.next = new_node
        curr = new_node
    return head

# test cases

# palindrome (odd length): 9 -> 2 -> 4 -> 2 -> 9
head1 = from_list([9, 2, 4, 2, 9])
assert isPalindrome(head1) == True

# not palindrome: 9 -> 12 -> 4 -> 2 -> 9
head2 = from_list([9, 12, 4, 2, 9])
assert isPalindrome(head2) == False

# palindrome (even length): 1 -> 2 -> 2 -> 1
head3 = from_list([1, 2, 2, 1])
assert isPalindrome(head3) == True

# not palindrome (even length): 1 -> 2 -> 3 -> 1
head4 = from_list([1, 2, 3, 1])
assert isPalindrome(head4) == False

# single element
head5 = from_list([5])
assert isPalindrome(head5) == True

# two identical elements
head6 = from_list([3, 3])
assert isPalindrome(head6) == True

# two different elements
head7 = from_list([3, 4])
assert isPalindrome(head7) == False

print("yay!!")
