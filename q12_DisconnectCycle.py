#Time: 40 minutes
#Technqiue: Linked list fast-slow two-pointer

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def DisconnectCycle(head):
    fast = head
    slow = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow is fast:
            break
    else:
        return head
        
    slow = head
    while slow is not fast:
        slow = slow.next
        fast = fast.next
    entry = slow

    current = entry
    while current.next is not entry:
        current = current.next
    current.next = None

    return head

def _build_cycle_case():
    n10 = Node(10)
    n18 = Node(18)
    n12 = Node(12)
    n9  = Node(9)
    n11 = Node(11)
    n4  = Node(4)

    n10.next = n18
    n18.next = n12
    n12.next = n9
    n9.next  = n11
    n11.next = n4
    n4.next  = n12  
    return n10

def _to_list_limited(head, limit=20):
    out = []
    cur = head
    steps = 0
    while cur is not None and steps < limit:
        out.append(cur.data)
        cur = cur.next
        steps += 1
    return out

if __name__ == "__main__":
    head = _build_cycle_case()
    print("before (limited):", _to_list_limited(head, 15))  

    head = DisconnectCycle(head)
    print("after:", _to_list_limited(head, 20)) # should be [10,18,12,9,11,4]