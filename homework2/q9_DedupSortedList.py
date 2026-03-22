# Hash Linked List Nodes
# O(n) Time Complexity
# O(m) Space Complexity, where m is the number of unique values in the sorted linked list
# Given a sorted singly linked list, remove any duplicates so that no value appears more than once

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def dedupSortedList(head):

    if head == None:
        return head

    # Keep track of any seen values
    seen = set()
    # The linked list is sorted so all duplicates are together

    curr = head

    # prev will hold the last seen unique node value
    prev = None
    

    while curr:

        if curr.data not in seen:
            # Unique Value
            seen.add(curr.data)

            # Keep Iterating
            prev = curr
            curr = curr.next
        else:
            # Deal with duplicate

            # Its impossible that prev == None now because that is only the case at the first node

            prev.next = curr.next
            curr.next = None

            curr = prev.next
            # Do not update prev because the next node may still be a duplicate
            

    return head


# 10 minutes

# Test Cases
arr1 = [1, 2, 2, 4, 5, 5, 5, 10, 10]
arr2 = [8, 8, 8, 8]

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
list2 = arrayToLinkedList(arr2)

list1AfterDedup = dedupSortedList(list1)
list2AfterDedup = dedupSortedList(list2)

def printLinkedList(head):

    if head == None:
        return
    
    s = []
    
    curr = head

    while curr:
        s.append(curr.data)
        curr = curr.next

    print(" -> ".join(str(x) for x in s))

printLinkedList(list1AfterDedup)
printLinkedList(list2AfterDedup)

