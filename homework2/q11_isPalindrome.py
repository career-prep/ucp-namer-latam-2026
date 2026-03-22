# Doubly Linked List Forward Backward Two Pointer
# O(n) Time Complexity
# O(1) Space Complexity
# Given a doubly linked list, determine if it is a palindrome

class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# I don't know if we are also given the tail, so I am assuming we don't get the tail
def isPalindrome(head):

    # Empty List
    if head == None:
        return True
    
    # List with one node
    if head.next == None:
        return True
    

    # Find the tail
    tail = head

    while tail.next:
        tail = tail.next

    headPtr = head

    # Now tail is on the real tail... we can start checking if we have a palindrome
    # Stop when the pointers meet (odd length) or when they cross (even length)
    while headPtr != tail and headPtr.prev != tail:

        if tail.data != headPtr.data:
            return False
        else:
            # Keep moving
            tail = tail.prev
            headPtr = headPtr.next

    return True


# 20 minutes

# Test Cases
arr1 = [9, 2, 4, 2, 9]
arr2 = [9, 12, 4, 2, 9]

def arrToDoublyLinkedList(arr):

    if len(arr) == 0:
        return None
    
    head = Node(arr[0])

    curr = head

    for i in range(1, len(arr)):
        newNode = Node(arr[i])

        curr.next = newNode
        newNode.prev = curr

        curr = newNode


    return head

list1 = arrToDoublyLinkedList(arr1)
list2 = arrToDoublyLinkedList(arr2)

print(isPalindrome(list1))
print(isPalindrome(list2))