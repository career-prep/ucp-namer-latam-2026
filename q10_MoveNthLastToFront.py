#Time: 40 Minutes
#Technqiue: Linked list fixed-distance two-pointer

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def MoveNthLastToFront(head, val):
    distance = 0 

    fast = head
    slow = head

    while distance != val:
        distance += 1
        fast = fast.next
    
    while fast.next is not None:
        slow = slow.next
        fast = fast.next
    
    target = slow.next
    slow.next = target.next
    target.next = head
    return target

def _from_list(values):
    if not values:
        return None
    head = Node(values[0])
    cur = head
    for v in values[1:]:
        cur.next = Node(v)
        cur = cur.next
    return head

def _to_list(head):
    out = []
    cur = head
    while cur is not None:
        out.append(cur.data)
        cur = cur.next
    return out

if __name__ == "__main__":
    head = _from_list([1, 2, 3, 4, 5])

    # Move 2nd last (which is 4) to front => [4,1,2,3,5]
    new_head = MoveNthLastToFront(head, 2)
    print(_to_list(new_head))