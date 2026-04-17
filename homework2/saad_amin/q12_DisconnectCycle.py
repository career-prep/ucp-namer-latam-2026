#Time Complexity: O(n)
#Space Complexity: O(1)
#Technique: Slow Fast pointer

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def disconnectCycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return head
        
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    start = slow
    temp = start
    while temp.next != start:
        temp = temp.next

    temp.next = None

    return head


head1 = ListNode(10)
head1.next = ListNode(18)
head1.next.next = ListNode(12)
head1.next.next.next = ListNode(9)
head1.next.next.next.next = ListNode(11)
head1.next.next.next.next.next = ListNode(4)
head1.next.next.next.next.next.next = head1.next.next

def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")
    
disconnectCycle(head1)  
print_list(head1)

#Time taken: 35 min