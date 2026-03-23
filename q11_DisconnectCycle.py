#Time: O(n)
#Space: O(n)

def disconnect_cycle(head):
    sett = set()
    sett.add(head)
    curr = head

    while curr.next:
        node = curr.next 
        if node in sett:
            curr.next = None 
            break
        else:
            sett.add(node)
            curr = curr.next 
    
    return head

#Time-taken: 20 minutes
            