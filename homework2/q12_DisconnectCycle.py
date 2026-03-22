# Linked List fast-slow two-pointer
# O(n) Time Complexity
# O(1) Space Complexity
# Given a singly linked list, disconnect the cycle if one exists

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    
def disconnectCycle(head):

    if head == None:
        return head
    

    slow = head
    fast = head

    # fast moves 2 at a time while slow moves 1 node at a time.
    # If fast and slow meet, then a cycle is detected.
    # If fast reaches None, then there is no cycle.

    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            # Cycle detected
            break
            

    if fast == None or fast.next == None:
        # No cycle
        return head
    
    
    # Now that a cycle is detected, we need to find the start of the cycle.
    # Move slow back to the head, and keep fast where it is.
    # walk each pointer 1 step at a time until they meet. That meeting point is the start of the cycle.

    slow = head

    while fast != slow:
        fast = fast.next
        slow = slow.next

    # now fast == slow, and we found the node at the start of the cycle
    # make a new pointer starting at slow,
    # walk it forward until we find that node that ptr.next == slow
    # at that node, we can disconnect the cycle

    walker = slow

    while walker.next != slow:
        walker = walker.next

    # Now disconnect the cycle
    walker.next = None

    return head



# 32 minutes



# Test Cases
arr1 = [10, 18, 12, 9, 11, 4]

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


def getNodeAt(head, idx):

    if head == None:
        return None

    curr = head

    i = 0

    while curr and i < idx:
        curr = curr.next
        i += 1

    return curr


def printLinkedList(head):

    if head == None:
        return
    
    s = []
    
    curr = head

    while curr:
        s.append(curr.data)
        curr = curr.next

    print(" -> ".join(str(x) for x in s))




list1 = arrayToLinkedList(arr1)
list2 = arrayToLinkedList(arr1)


# Test case 1
lastNode1 = getNodeAt(list1, len(arr1) - 1)   # node with data 4
thirdNode = getNodeAt(list1, 2)               # node with data 12
lastNode1.next = thirdNode                    # create cycle

# Test case 2
lastNode2 = getNodeAt(list2, len(arr1) - 1)   # node with data 4
lastNode2.next = lastNode2                    # create cycle

# printLinkedList(list1)
# printLinkedList(list2)
# uncomment the code above to check that the cycle exists

modifiedList1 = disconnectCycle(list1)
modifiedList2 = disconnectCycle(list2)


printLinkedList(modifiedList1)
printLinkedList(modifiedList2)







