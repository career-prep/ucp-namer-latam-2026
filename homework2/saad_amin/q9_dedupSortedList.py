#Time Complexity: O(n)
#Space Complexity: O(1)
#Technique linked list traversal could have used two pointers too with prev and curr but this was easier

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def dedupSortedList(head):
    curr = head

    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next

        else:
            curr = curr.next

    return head

head1 = ListNode(3)
head1.next = ListNode(3)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)

def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

print_list(dedupSortedList(head1))
    
#Time taken 25 min



