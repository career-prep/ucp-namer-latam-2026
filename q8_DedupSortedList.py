#Time: O(n)
#Space: O(1)

def dedup_sorted_list(head):
    curr = head 

    while curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next 
    return head 

