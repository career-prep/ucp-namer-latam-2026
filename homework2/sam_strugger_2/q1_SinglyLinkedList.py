class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def insertAtFront(head, val): # Time: O(1), Space: O(1)
    newNode = Node(val)
    newNode.next = head

    return head

def insertAtBack(head, val): # Time: O(n), Space: O(1)
    newNode = Node(val)
    cur = head
    while cur.next:
        cur = cur.next

    cur.next = newNode

    return newNode


def insertBefore(head, val, loc): # Time: O(n), Space: O(1)
    newNode = Node(val)

    cur = head
    while cur and loc < 1:
        cur = cur.next
        loc-=1

    if loc == 1 and cur:
        newNode.next = cur.next
        cur.next = newNode

    return head


def deleteFront(head): # Time: O(1), Space: O(1)
    head.next = None
    head.val = None

    return head.next

def deleteBack(head): # Time: O(n), Space: O(1)
    # list = [1,2,3,4,5,None]
    cur = head
    while cur.next.next:
        cur = cur.next

    if cur and cur.next:
        cur.next = None

    return head

def deleteNode(head, loc): # Time: O(n), Space: O(1)
    cur = head
    while cur and loc > 1:
        cur = cur.next
        loc-=1
    
    if cur and loc == 1:
        cur.next = cur.next.next

    return head
        

def length(head): # Time: O(n), Space: O(1)
    len = 0
    cur = head

    while cur:
        cur = cur.next
        len += 1

    return len

def reverseIterative(head): # Time: O(n), Space: O(1)
    cur = head.next
    prev = head
    head.next = None

    # order of operations: cur.next = prev, but we need to remember the cur.next

    while cur:
        next = cur.next
        cur.next = prev

        prev = cur
        cur = next

    return prev


## Ran out of time for the following
# def reverseRecursive(head):

#     def recursion(cur):
#         if cur:
#             next = cur.next
#             cur.next = prev 

#             prev = cur
#             cur = next


#             recursion(cur.nex)
#         else:
#             return


# Everything above took me 40 minutes. FYI, I used AI to help build the functions to test my code

# Helper to build a linked list from a Python list
def buildList(vals):
    if not vals:
        return None
    head = Node(vals[0])
    cur = head
    for v in vals[1:]:
        cur.next = Node(v)
        cur = cur.next
    return head

# Helper to convert linked list to Python list for easy printing
def toList(head):
    result = []
    cur = head
    while cur:
        result.append(cur.val)
        cur = cur.next
    return result

def main():
    head = buildList([1, 2, 3, 4, 5])
    print("Original:       ", toList(head))

    head = insertAtFront(head, 0)
    print("InsertAtFront(0):", toList(head))

    head = insertAtBack(head, 6)
    print("InsertAtBack(6): ", toList(head))

    head = buildList([1, 2, 3, 4, 5])
    head = deleteFront(head)
    print("DeleteFront:     ", toList(head))

    head = buildList([1, 2, 3, 4, 5])
    head = deleteBack(head)
    print("DeleteBack:      ", toList(head))

    head = buildList([1, 2, 3, 4, 5])
    head = deleteNode(head, 2)
    print("DeleteNode(pos2):", toList(head))

    # 
    head = buildList([1, 2, 3, 4, 5])
    print("Length:          ", length(head))

    head = buildList([1, 2, 3, 4, 5])
    head = reverseIterative(head)
    print("ReverseIterative:", toList(head))

if __name__ == "__main__":
    main()
