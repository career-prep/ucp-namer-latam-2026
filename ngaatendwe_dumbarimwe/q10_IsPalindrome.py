#Time: O(n)
#Space: O(1)

def is_palindrome(head):
    curr = head 
    left = head

    while curr.next:
        curr = curr.next
    right = curr 

    while left is not right:
        if left.val != right.val:
            return False
        else:
            left = left.next
            right = right.prev
    return True

#Time-taken: 20 minutes