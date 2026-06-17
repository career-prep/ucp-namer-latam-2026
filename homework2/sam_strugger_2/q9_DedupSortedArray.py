class Node:
    def __init__(self,value):
        self.next = None
        self.value = value

# list = [1,2,2,3]


def dedup(head): # O(n) time and O(1) space complexity
    cur = head
    prev = None
    while cur:
        if prev and cur:
            if prev.value == cur.value:
                prev.next = cur.next
                cur = prev.next 
                continue 

        prev = cur
        cur = cur.next

# This solution took me about 10 minutes
def buildList(vals):
    if not vals:
        return None
    head = Node(vals[0])
    cur = head
    for v in vals[1:]:
        cur.next = Node(v)
        cur = cur.next
    return head

def toList(head):
    result = []
    cur = head
    while cur:
        result.append(cur.value)
        cur = cur.next
    return result

def main():
    # Basic case with consecutive dupes
    head = buildList([1, 2, 2, 3])
    dedup(head)
    print("Input: [1,2,2,3]     ->", toList(head))  # expect [1, 2, 3]

    # Multiple dupes in a row
    head = buildList([1, 1, 1, 2, 3, 3])
    dedup(head)
    print("Input: [1,1,1,2,3,3] ->", toList(head))  # expect [1, 2, 3]

    # No dupes
    head = buildList([1, 2, 3, 4])
    dedup(head)
    print("Input: [1,2,3,4]     ->", toList(head))  # expect [1, 2, 3, 4]

    # All same
    head = buildList([5, 5, 5, 5])
    dedup(head)
    print("Input: [5,5,5,5]     ->", toList(head))  # expect [5]

    # Single element
    head = buildList([1])
    dedup(head)
    print("Input: [1]           ->", toList(head))  # expect [1]

if __name__ == "__main__":
    main()
