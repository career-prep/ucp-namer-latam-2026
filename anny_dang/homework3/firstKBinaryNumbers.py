from collections import deque
def firstKBinaryNumbers(k):
    """
    idea:
    use a queue to generate binary numbers in order
    start with "1" in the queue
    each time, pop the front number, add it to the result 
    then push its two children: cur + "0" and cur + "1"
    repeat until we collect k binary numbers

    Time complexity: O(k*logk)
    Space complexity: O(k)
    """
    if k == 0:
        return []
    res = ["0"]
    queue = deque(["1"])

    while queue and len(res) < k:
        cur = queue.popleft()
        res.append(cur)
        queue.append(cur + "0")
        queue.append(cur + "1")
    
    return res

print(firstKBinaryNumbers(5))
print(firstKBinaryNumbers(0))
