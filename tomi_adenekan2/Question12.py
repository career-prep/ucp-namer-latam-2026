def detectAndRemoveCycle(head: Node) -> bool:
    fast = head
    slow = head
    check = False

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            check = True
            break

    if not check:
      return False
        

    slow = head
    while fast != slow:
        slow = slow.next
        fast = fast.next

    entry = slow.next
    while entry.next != slow:
        entry = entry.next
    entry.next = None
    print(f"slow: {slow}")
    print(f"fast: {fast}")
    print(f"entry: {entry}")
  return True
  
