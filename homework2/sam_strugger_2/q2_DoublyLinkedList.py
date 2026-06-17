class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def insertAtFront(head, val): # Time: O(1), Space: O(1)
    newNode = Node(val)
    newNode.next = head
    head.prev = newNode

    return newNode

def insertAtBack(head, val): # Time: O(n), Space: O(1)
    newNode = Node(val)
    cur = head
    while cur.next:
        cur = cur.next

    cur.next = newNode
    newNode.prev = cur

    return head


def insertBefore(head, val, loc): # Time: O(n), Space: O(1)
    newNode = Node(val)

    cur = head
    while cur and loc > 0:
        cur = cur.next
        loc-=1

    if loc == 0 and cur:
        newNode.next = cur
        newNode.prev = cur.prev

        cur.prev.next = newNode
        cur.next.prev = newNode

    return head


def deleteFront(head): # Time: O(1), Space: O(1)
    head.next.prev = None

    return head.next

def deleteBack(head): # Time: O(n), Space: O(1)
    # list = [1,2,3,4,5,None]
    cur = head
    while cur.next.next:
        cur = cur.next

    if cur and cur.next:
        cur.next.prev = None
        cur.next = None

    return head

def deleteNode(head, loc): # Time: O(n), Space: O(1)
    cur = head
    while cur and loc > 0:
        cur = cur.next
        loc-=1
    
    if cur and loc == 0:
        cur.prev.next = cur.next
        cur.next.prev = cur.prev

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
    head.next = None

    while cur:
        next = cur.next
        cur.next, cur.prev = cur.prev, cur.next

        prev = cur
        cur = next

    return prev

# I need to practice recursion more. Don't feel comfortable with it yet
# def reverseRecursive(head):

#     def recursion(cur):
#         

# This took me 15 minutes out of the 20 alloted

def buildList(vals):
    if not vals:
        return None
    head = Node(vals[0])
    cur = head
    for v in vals[1:]:
        node = Node(v)
        node.prev = cur
        cur.next = node
        cur = node
    return head

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

    head = buildList([1, 2, 3, 4, 5])
    head = insertAtFront(head, 0)
    print("InsertAtFront(0):", toList(head))

    head = buildList([1, 2, 3, 4, 5])
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

    head = buildList([1, 2, 3, 4, 5])
    print("Length:          ", length(head))

    head = buildList([1, 2, 3, 4, 5])
    head = reverseIterative(head)
    print("ReverseIterative:", toList(head))

if __name__ == "__main__":
    main()