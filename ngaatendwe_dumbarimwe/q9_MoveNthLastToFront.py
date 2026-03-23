#Time: O(n)
#Space: O(1)

def move_node(head,k):
    curr = head 
    length = 0

    while curr:
        length += 1
        curr = curr.next
    
    if k == length:
        return head 
    
    prev_pos =  length - k
    curr = head

    for _ in range(prev_pos - 1):
        curr = curr.next
    
    temp = curr.next
    curr.next = temp.next
    temp.next = head 

    return head 

#Time-taken: 25 minutes

