class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = None


def insertAtFront(head, val):
    # Creates new Node with data val at front; returns head
    # Time Complexity: O(1)
    newNode = Node(val)
    newNode.next = head
    return newNode


def insertAtBack(head, val):
    # Creates new Node with data val at end; returns head
    '''
    To get the last node I need to traverse the entire list until I reach the last node.
    Then I set the last nodes next reference to point to the new node.
    This will make the new node the last element in the list.
    '''
    # Time Complexity: O(n)
    newNode = Node(val)

    if head is None:
        return newNode
    last = head
    while last.next is not None:
        last = last.next
    last.next = newNode
    return head
    


def insertAfter(head, val, loc):
    # Creates new Node with data val after Node loc; returns head
    # Time Complexity: O(n)
    '''
    For this function I am finding the node loc, then inserting after that node once I've found it.
    '''
    curr = head
    while curr is not None:
        if curr == loc:
            newNode = Node(val)
            newNode.next = curr.next
            curr.next = newNode
            return head
        curr = curr.next
    return head


def insertBefore(head, val, loc):
    # Creates new Node with data val before Node loc; returns head
    # Time Complexity: O(n)
    '''
    For this function I go through the list until I find the node before loc, once I have I make the next node of the node before loc the new node. 
    '''
    # This takes care of the case we are inserting before the head
    if head == loc:
        return insertAtFront(head, val)

    curr = head
    while curr is not None and curr.next != loc:
        curr = curr.next
    
    if curr is not None:
        newNode = Node(val)
        newNode.next = curr.next
        curr.next = newNode
    return head
    


def deleteFront(head):
    # Removes first Node returns head
    # Time Complexity: O(1)
    '''
    To remove the first node of the linked list I store the current head
    in a temp node and move the head pointer to the next node, delete the temp head node
    and finally return the new head of the linked list.
    '''
    if head is None:
        return None
    
    temp = head

    head = head.next

    temp = None

    return head
    


def deleteBack(head):
    # Removes last Node returns head
    # Time Complexity: O(n)
    '''
    To delete from the end of the list, I need to traverse the list
    to find the second to last node, then set its next pointer to None.
    If the list empty there is no node to delete or has only one node then point head
    to none.
    '''
    if head is None:
        return None
    
    if head.next is None:
        return None
    
    secondLast = head

    while secondLast.next.next is not None:
        secondLast = secondLast.next

    secondLast.next = None

    return head
    


def deleteNode(head, loc):
    # Deletes Node loc returns head
    # Time Complexity: O(n)
    '''
    To delete from a specific position, first if the position is 1, I update the head to point to the next node
    and delete the current head. For other positions, I traverse the list to reach the node just before the specified position. If the target node exists I 
    adjust the next of this previous node to point to next of next nodes, which will result in skipping the target node.

    '''

    if head is None:
        return None
    
    if head == loc:
        return head.next
    
    curr = head
    while curr.next is not None:
        if curr.next == loc:
            curr.next = curr.next.next
            return head
        curr = curr.next
    
    return head

def length(head):
    # Returns length of the list
    # Time Complexity: O(n)
    count = 0
    current_node = head
    while current_node:
        count += 1
        current_node = current_node.next
    return count

def reverseIterative(head):
    # Reverses the linked list iteratively
    '''
    For the iterative version of reversing a linked list the idea is by changing the direction
    of links using three pointers, prev, curr, and next. At each step, point the current node to its previous node and then move all three
    pointers forward until the list is fully reversed.
    '''

    curr = head
    prev = None

    while curr is not None:
        nextNode = curr.next

        curr.next = prev

        prev = curr
        curr = nextNode
    return prev
    pass


def _reverseRecursiveHelper(head):
    # Helper function for reverseRecursive
    '''
    Recursively traverses to the end of the linked list, then rewires
    each node's next pointer on the way back up the call stack.
    The base case returns when it reaches the last node (or an empty list),
    which becomes the new head. As the recursion unwinds, each node points
    back to its predecessor, effectively reversing the direction of the list.
    '''
    if head is None or head.next is None:
        return head
    
    new_head = _reverseRecursiveHelper(head.next)
    head.next.next = head
    head.next = None
    return new_head
    


def reverseRecursive(head):
    # Reverses the linked list recursively
    return _reverseRecursiveHelper(head)
    



def printList(head):
    result = []
    curr = head
    while curr:
        result.append(str(curr.data))
        curr = curr.next
    print(" -> ".join(result))


if __name__ == "__main__":
    head = None
    
    head = insertAtFront(head, 3)
    head = insertAtFront(head, 2)
    head = insertAtFront(head, 1)
    printList(head)  

    head = insertAtBack(head, 4)
    head = insertAtBack(head, 5)
    printList(head) 

    print(length(head))  

    head = deleteFront(head)
    printList(head)  

    head = deleteBack(head)
    printList(head)  

    head = reverseIterative(head)
    printList(head)  

    head = reverseRecursive(head)
    printList(head)  