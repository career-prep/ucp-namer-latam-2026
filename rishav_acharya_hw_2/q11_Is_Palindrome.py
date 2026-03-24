# Approach:
# Since this is a doubly linked list, we can use two pointers:
# 1. One pointer starts at the head
# 2. Another pointer goes to the tail
# 3. Compare values from both ends while moving inward
# If all corresponding values match, the list is a palindrome

# Time Complexity: O(n)
# → one pass to reach tail, then at most half the list for comparisons

# Space Complexity: O(1)
# → only pointers are used

def isPalindrome(head):
    if not head or not head.next:
        return True

    left = head
    right = head

    # move right to the tail
    while right.next:
        right = right.next

    # compare from both ends
    while left != right and left.prev != right:
        if left.data != right.data:
            return False
        left = left.next
        right = right.prev

    return True
