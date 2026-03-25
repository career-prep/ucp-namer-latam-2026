# Technique: Linked list reset/catch-up two-pointer
# Time: O(n) - single pass through the list
# Space: O(1) - just rewiring, no extra space
 
# since the list is sorted, duplicates are always adjacent
# so we just need to look at curr and curr.next - if they match, skip next
 
def dedupSortedList(head):
    curr = head
    while curr is not None and curr.next is not None:
        if curr.data == curr.next.data:
            # skip over the duplicate
            curr.next = curr.next.next
            # don't advance curr yet - there might be more duplicates of same val
        else:
            curr = curr.next
    return head
 
