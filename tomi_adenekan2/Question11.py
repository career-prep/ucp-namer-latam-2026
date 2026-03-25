"""
34 minutes
"""


def isPalindrome(head: Node) -> bool:
    
    count = 0
    cur = head
    while cur:
        cur = cur.next
        count += 1
    #print(f"The length is {count}")
    sec = head
    for _ in range(count // 2):
        sec = sec.next
    mov = sec
    prev = None
    while mov:
        temp = mov.next
        mov.next = prev
        mov.prev = temp
        prev = mov
        mov = temp
    second = prev  
    first = head
    while second and second.next:
        if first.data != second.data:
            return False
        first = first.next
        second = second.next
    return True
    
