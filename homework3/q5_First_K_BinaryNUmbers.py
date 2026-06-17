# Time complexity: O(k)
# Space complexity: O(k)
#Time Spent: 28 minutes

from collections import deque

def FirstKBinaryNumbers(k):
    if k < 1:
        return None
    
    res = []
    q = deque()

    q.append("1")

    while k > 0:
        curr = q.popleft()
        res.append(curr)

        q.append(curr + "0")
        q.append(curr + "1")

        k -= 1

    return res


if __name__ == "__main__":
    ks = (1, 2, 3, 4, 5)
    for k in ks:
        print(f"K is {k}:")
        print(FirstKBinaryNumbers(k))
