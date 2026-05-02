#Time Complexity: O(n)
#Space Complexity: 0(1)
#Technique: Doublly Linked list forwrad backward pointer

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def isPalindrome(head):
    temp2 = head
    temp1 = head
    
    if not head or not head.next:
            return True

    while temp2.next:
        temp2 = temp2.next

    while temp1 != temp2 and temp1.prev != temp2:
        if temp2.val != temp1.val:
            return False
            
        temp1 = temp1.next
        temp2 = temp2.prev

    return True

head = ListNode(1)
head.next = ListNode(2)
head.next.prev = head
head.next.next = ListNode(1)
head.next.next.prev = head.next

print(isPalindrome(head))

head = ListNode(1)
head.next = ListNode(2)
head.next.prev = head
head.next.next = ListNode(3)
head.next.next.prev = head.next

print(isPalindrome(head))

#Time taken 27 min
