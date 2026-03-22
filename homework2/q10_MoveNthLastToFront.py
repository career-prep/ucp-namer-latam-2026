# Linked List fast-slow two-pointer
# O(n) Time Complexity
# O(1) Space Complexity
# Given a singly linked list node, mode the nth from the last element to the front of the list

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Knowing the constraints of k would be helpful... What should I do if k = 0? Can k be negative?
def moveNthLastToFront(head, k):

    if head == None:
        return head
    
    # when k = 2, the example test case moved the node at n - 2 to the front...
    # so if k = 1, we move the node at n - 1 (the last node) to the front
    # So I am assuming that if k = 0, we don't move any nodes
    if k == 0:
        return head
    # I am also assuming k cannot be negative, and k wont be larger that the amount of nodes we have


    # Move the fast pointer k steps ahead
    # Then move the slow and fast one step at a time (slow starting at head), until fast reaches the end
    # At that point, slow will be at the node before the target node
    fast = head
    for i in range(k):
        fast = fast.next

    if fast == None:
        # Then k == length of the list... so the node we want to move is the head itself
        return head

    slow = head

    while fast.next:
        fast = fast.next
        slow = slow.next

    # Slow is on the node before the target node

    targetNode = slow.next
    slow.next = targetNode.next
    targetNode.next = head

    head = targetNode

    return head
    

# 17 minutes


# Test Cases
arr1 = [15, 2, 8, 7, 20, 9, 11, 6, 19]

def arrayToLinkedList(arr):

    if len(arr) == 0:
        return None
    
    head = Node(arr[0])


    walker = head

    for i in range(1, len(arr)):

        newNode = Node(arr[i])

        walker.next = newNode

        walker = walker.next


    return head


list1 = arrayToLinkedList(arr1)
list2 = arrayToLinkedList(arr1)


def printLinkedList(head):

    if head == None:
        return
    
    s = []
    
    curr = head

    while curr:
        s.append(curr.data)
        curr = curr.next

    print(" -> ".join(str(x) for x in s))


movedList1 = moveNthLastToFront(list1, 2)
movedList2 = moveNthLastToFront(list2, 7)

printLinkedList(movedList1)
printLinkedList(movedList2)
