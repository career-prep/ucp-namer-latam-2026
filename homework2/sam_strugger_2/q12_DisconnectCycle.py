class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
  
def disconnectCycle(head): # Time O(n), Space, O(n). Could be O(1) space with fast/slow pointer approach

    seen = set()
    if head is None:
        return None
    
    cur = head
    prev = head

    while cur:
        if cur in seen:
            prev.next = None
            return head
        
        seen.add(cur)
        prev = cur
        cur = cur.next

    return head

# This took me 30 minutes. I know there is a fast/slow pointer approach to this problem but I couldn't get it right 
# and pivoted to hash approach. 

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
    node3 = head.next.next
    node5 = node3.next.next
    node5.next = node3  
    disconnectCycle(head)
    print("Cycle at 3:", toList(head))  

    head = buildList([1, 2, 3])
    head.next.next.next = head  
    disconnectCycle(head)
    print("Cycle at 1:", toList(head))  #

  
    head = buildList([1, 2, 3, 4])
    disconnectCycle(head)
    print("No cycle:  ", toList(head))  

  
    head = Node(1)
    head.next = head
    disconnectCycle(head)
    print("Self loop: ", toList(head))  

   
    print("Empty:     ", disconnectCycle(None))  

if __name__ == "__main__":
    main()
