#Given a sorted singly linked list, remove any duplicates so that no value appears more than once.


#time and space O(n) and O(1)
## time taken to solve: 16 mins: first failed attempt
## time taken to solve: 5 mins: second attempt
# linked list
# remove duplicates
# return the head

# what if the given head is null
#return null

# if only one node return 
# that node

#algo
#initial thinking:
# using two pointers 1st at the first node and 2nd at the second node
#iterate until the end of the linked list
## during each iternation 
## compare the data of the first node with second node
## if not equal both of them will go to .next
## if equal only 2nd will go to .next and flag = true

# eg 1 2 3 4 4 4 5 5
#          i j
# flag 
# i.next to j
# flag to false

#2 3  // did not work in this case
def dedupSortedList(head):
    curr1 = head
    # curr2 = head.next
    # flag = False
    if not head:
        return None
    
    if not curr1.next:
        return curr1
    
    # while curr1 and curr2:
    #     if curr1.data != curr2.data:
    #         if flag:
    #             curr1.next = curr2
    #             flag = False
    #         else:
    #             curr1 = curr1.next
    #             curr2 = curr2.next

    #     else:
    #         temp = curr2.next
    #         curr2.next = None
    #         curr2 = temp
    #         flag = True


#new approach:
#2 3 3
# if curr.data == curr.next.data
# curr.next = curr.next.next

    
    while curr1 and curr1.next:
        if curr1.data == curr1.next.data:
            curr1.next = curr1.next.next
        else:
            curr1 = curr1.next

    return head

  

#given: head of a linked list(sorted)
#todo: remove the duplicates and return the head

# 2 3 4 5
#     s f
# 2 3 4 5 

#edge cases
#we dont have head
#what if we are given with a linked list with no duplicates: return head

# 1-> none
# s   f
# 1

# 1 -> none
# s    f

#brute force
def dedup(head):

    if not head: return None
    
    slow = head
    fast = head.next

    while fast:
        if slow.data == fast.data:
            fast = fast.next
            slow.next = fast
        else:
            fast = fast.next
            slow = slow.next

    return head