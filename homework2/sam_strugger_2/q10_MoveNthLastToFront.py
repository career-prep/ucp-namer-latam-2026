class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def moveNthLastToFront(head,k): # O(n) time, O(1) space

    front = head

    for i in range(k):
        front = front.next

    back = head
    while front.next:
        front = front.next
        back = back.next

    move = back.next
    back.next = back.next.next

    move.next = head

    return move

# This solution took me 8 minutes

def buildList(vals):
    if not vals:
        return None
    head = Node(vals[0])
    cur = head
    for v in vals[1:]:
        cur.next = Node(v)
        cur = cur.next
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
    head = moveNthLastToFront(head, 1)
    print("k=1:", toList(head))  

    head = buildList([1, 2, 3, 4, 5])
    head = moveNthLastToFront(head, 2)
    print("k=2:", toList(head)) 

    head = buildList([1, 2, 3, 4, 5])
    head = moveNthLastToFront(head, 3)
    print("k=3:", toList(head)) 

    head = buildList([1, 2])
    head = moveNthLastToFront(head, 1)
    print("k=1, [1,2]:", toList(head)) 

if __name__ == "__main__":
    main()
