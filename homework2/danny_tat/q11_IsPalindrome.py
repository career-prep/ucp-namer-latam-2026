# Question 11: IsPalindrome
# Technique: Doubly linked list forward-backward two-pointer
# Time: O(n)
# Space: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def isPalindrome(head):
    if not head:
        return True

    tail = head

    while tail.next:
        tail = tail.next

    left = head
    right = tail

    while left != right and left.prev != right:
        if left.data != right.data:
            return False
        left = left.next
        right = right.prev

    return True


# Example 1: [9,2,4,2,9] → True
n1 = Node(9)
n2 = Node(2)
n3 = Node(4)
n4 = Node(2)
n5 = Node(9)
n1.next = n2
n2.prev = n1
n2.next = n3
n3.prev = n2
n3.next = n4
n4.prev = n3
n4.next = n5
n5.prev = n4

print(isPalindrome(n1))

# Example 2: [9,12,4,2,9] → False
m1 = Node(9)
m2 = Node(12)
m3 = Node(4)
m4 = Node(2)
m5 = Node(9)
m1.next = m2
m2.prev = m1
m2.next = m3
m3.prev = m2
m3.next = m4
m4.prev = m3
m4.next = m5
m5.prev = m4

print(isPalindrome(m1))

# time: 22 minutes
