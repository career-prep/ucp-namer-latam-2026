# Technique used: Doubly linked list forward-backward two-pointer
# Time Complexity: O(n)
# Space Complexity: O(1)

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

    front = head
    back = tail

    while front != back and back.prev != front:
        if front.data != back.data:
            return False
        front = front.next
        back = back.prev

    return front.data == back.data


def buildDLL(vals):
    if not vals:
        return None
    head = Node(vals[0])
    curr = head
    for v in vals[1:]:
        new_node = Node(v)
        new_node.prev = curr
        curr.next = new_node
        curr = new_node
    return head


print("isPalindrome Results:")

print(isPalindrome(buildDLL([9, 2, 4, 2, 9])))
print(isPalindrome(buildDLL([9, 12, 4, 2, 9])))
print(isPalindrome(buildDLL([5])))
print(isPalindrome(buildDLL([1, 2, 2, 1])))
print(isPalindrome(buildDLL([1, 2, 3])))
print(isPalindrome(buildDLL([7, 7, 7, 7])))

# Time Taken: 25 mins
