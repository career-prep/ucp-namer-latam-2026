# Approach:
# Since this is a doubly linked list, we can use two pointers:
# 1. One pointer starts at the head
# 2. Another pointer goes to the tail
# 3. Compare values from both ends while moving inward
# If all corresponding values match, the list is a palindrome

# Time Complexity: O(n)
# → one pass to reach tail, then at most half the list for comparisons

# Space Complexity: O(1)
# → only pointers are used

# time taken: 10 mins

def isPalindrome(head):
    if not head or not head.next:
        return True

    left = head
    right = head

    # move right to the tail
    while right.next:
        right = right.next

    # compare from both ends
    while left != right and left.prev != right:
        if left.data != right.data:
            return False
        left = left.next
        right = right.prev

    return True







#Given a doubly linked list determine if it is a Palindrome

#condition for palindrom, reads the same from front and back

#two pointer
#approach:
# assign the first pointer with head
#second pointer with last node(iterate throught the linkedList for that)
#count2 = last index
#while (count1 <count2):
    #if start.data != end.data:
        #return False
    #start = start.next
    count1 +=1
    #end = end.prev
    count2 -=1
    return True

#edge cases
#if not head:
# return False

def isPalin(head):
    if not head:
        return False
    
    end, start = head
    end_index = 0
    while end.next:
        end_index += 1
        end = end.next

    start_idx = 0

    while(start_idx < end_index):
        if start.data != end.data:
            return False
        start = start.next
        start_idx += 1

        end = end.prev
        end_index -= 1

        
    return True
