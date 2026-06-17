#Time Complexity :O(n)
#Space Complexity: O(1)
#Technique : Linked list fixed distance two pointer

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def moveNthLastToFront(head, k):
    dummy = ListNode(0)
    dummy.next = head
    behind = ahead = dummy

    for _ in range(k + 1):
        ahead = ahead.next

    while ahead:
        ahead = ahead.next
        behind = behind.next

    temp = behind.next
    behind.next = behind.next.next
    temp.next = dummy.next
    dummy.next = temp
    
    return dummy.next

#Time taken 35 min

head1 = ListNode(15)
head1.next = ListNode(2)
head1.next.next = ListNode(8)
head1.next.next.next = ListNode(7)
head1.next.next.next.next = ListNode(20)
head1.next.next.next.next.next = ListNode(9)
head1.next.next.next.next.next.next = ListNode(11)
head1.next.next.next.next.next.next.next = ListNode(6)
head1.next.next.next.next.next.next.next.next = ListNode(19)

def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

print_list(moveNthLastToFront(head1, 2))
        