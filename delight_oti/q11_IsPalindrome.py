# Technique: Doubly linked list forward-backward two-pointer
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    def isPalindrome(self):

        if not self:
            return True
        
        right = self
        while right.next:
            right = right.next
        
        left = self

        while left != right and left.prev != right:
            if left.data != right.data:
                return False
            
            left = left.next
            right = right.prev

        return True
    
# head = Node(1)
# n2 = Node(2)
# n3 = Node(3)

# head.next = n2
# n2.prev = head

# n2.next = n3
# n3.prev = n2

# print(head.isPalindrome())  # False