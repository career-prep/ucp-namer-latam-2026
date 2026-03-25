# Technique: Doubly linked list forward-backward two-pointer
# Time: O(n)
# Space: O(1)

# doubly linked list makes this clean start one pointer at the front
# and one at the back, compare them, move inward, repeat
# if all values match it's a palindrome
 
def isPalindrome(head):
    if head is None:
        return True
 
    # get to the tail first
    tail = head
    while tail.next is not None:
        tail = tail.next
 
    # now walk inward from both ends
    left = head
    right = tail
 
    while left != right and left.prev != right:
        # left.prev != right handles the even-length case where they cross
        if left.data != right.data:
            return False
        left = left.next
        right = right.prev
 
    return True
 
