# Runtime: O(n)
# Space complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def isPalindrome(head):
    if not head:
        return True

    left = head
    right = head
    while right.next:
        right = right.next

    while left != right and left.prev != right:
        if left.data != right.data:
            return False

        left = left.next
        right = right.prev

    return True

def run_tests():
    # Helper to build a DLL from a list
    def buildDLL(arr):
        if not arr: return None
        head = Node(arr[0])
        curr = head
        for i in range(1, len(arr)):
            newNode = Node(arr[i])
            curr.next = newNode
            newNode.prev = curr
            curr = newNode
        return head

    # 1. Test Odd Palindrome
    h1 = buildDLL([1, 2, 3, 2, 1])
    assert isPalindrome(h1) == True
    print("Odd palindrome test passed")

    # 2. Test Even Palindrome
    h2 = buildDLL([1, 2, 2, 1])
    assert isPalindrome(h2) == True
    print("Even palindrome test passed")

    # 3. Test Non-Palindrome
    h3 = buildDLL([1, 2, 3])
    assert isPalindrome(h3) == False
    print("Non-palindrome test passed")

    # 4. Test Single Node
    h4 = buildDLL([10])
    assert isPalindrome(h4) == True
    print("Single node test passed")

    # 5. Test Empty List
    assert isPalindrome(None) == True
    print("Empty list test passed")

run_tests()

# Time spent: 25:00
