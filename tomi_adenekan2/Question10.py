# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next

        if n > count:
            return None

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        move = head

        for _ in range(count - n):
            prev = move
            move = move.next
        if move.next:
            prev.next = move.next
        else:
            prev.next = None

        move.next= dummy.next
        dummy.next = move
        return dummy.next


