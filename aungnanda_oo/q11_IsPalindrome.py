# Question 11: IsPalindrome

# Given a doubly linked list, determine if it is a palindrome.

# Time Complexity = O(n) — walk both pointers toward center
# Space Complexity = O(1) — only two pointers, no extra storage

# Examples:

# Input:  1<->2<->3<->2<->1
# Output: True

# Input:  1<->2<->3<->4<->5
# Output: False

# Input:  1<->2<->2<->1
# Output: True (even length)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def build_list(vals):
    if not vals:
        return None
    head = Node(vals[0])
    cur = head
    for v in vals[1:]:
        new_node = Node(v)
        new_node.prev = cur
        cur.next = new_node
        cur = cur.next
    return head


def list_to_str(head):
    result = []
    cur = head
    while cur:
        result.append(str(cur.data))
        cur = cur.next
    return "<->".join(result) if result else "[]"


def IsPalindrome(head):
    if not head or not head.next:
        return True

    # Find tail
    tail = head
    while tail.next:
        tail = tail.next

    # Walk from both ends toward center, compare
    left = head
    right = tail
    while left != right and left.prev != right:
        if left.data != right.data:
            return False
        left = left.next
        right = right.prev

    return True


# --- Tests ---

# Test 1: odd-length palindrome
head = build_list([1, 2, 3, 2, 1])
print("Test 1 input:", list_to_str(head))
print("Test 1 output:", IsPalindrome(head))   # True

# Test 2: not a palindrome
head = build_list([1, 2, 3, 4, 5])
print("Test 2 input:", list_to_str(head))
print("Test 2 output:", IsPalindrome(head))   # False

# Test 3: even-length palindrome
head = build_list([1, 2, 2, 1])
print("Test 3 input:", list_to_str(head))
print("Test 3 output:", IsPalindrome(head))   # True

# Test 4: single element
head = build_list([5])
print("Test 4 input:", list_to_str(head))
print("Test 4 output:", IsPalindrome(head))   # True

# Test 5: two same elements
head = build_list([3, 3])
print("Test 5 input:", list_to_str(head))
print("Test 5 output:", IsPalindrome(head))   # True

# Test 6: two different elements
head = build_list([1, 2])
print("Test 6 input:", list_to_str(head))
print("Test 6 output:", IsPalindrome(head))   # False

# Spent a total of 20 mins on this question
