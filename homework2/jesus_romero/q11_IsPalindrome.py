# Technique: Doubly linked list forward-backward two-pointer

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def isPalindrome(head): # Time, Space Complexities: O(n), O(1).
    #1. Handle edge cases: empty list or single node
    if head is None or head.next is None:
        return True
    
    #2. Initialize front pointer at the start
    front = head
    
    #3. Find the tail of the list
    back = head
    while back.next is not None:
        back = back.next
        
    #4. Move pointers toward the center
    while front != back and front.prev != back:
        #5. Return False if data mismatch occurs
        if front.data != back.data:
            return False
        
        #6. Advance front and retreat back
        front = front.next
        back = back.prev
        
    #7. If pointers met or crossed -> the list is a palindrome
    return True

def run_tests():
    #Test odd len palindrome: 9 <-> 2 <-> 4 <-> 2 <-> 9
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
    
    assert isPalindrome(n1) is True
    
    #2. Test mismatch: 9 <-> 12 <-> 4 <-> 2 <-> 9
    n2.data = 12
    assert isPalindrome(n1) is False
    
if __name__ == "__main__":
    run_tests()