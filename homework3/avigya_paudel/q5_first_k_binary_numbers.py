# Time taken: 15 minutes
# Time Complexity: O(k)
# Space Complexity: O(k)
# Algorithm: BFS

from collections import deque

def first_k_binary_numbers(k):
    """
        Given a number, k, return an array of the first k binary numbers, 
        represented as strings.
    """
    if k == 0: return []
    if k == 1: return ["0"]

    res = ["0"]
    q = deque(["1"])
    while len(res) < k:
        num = q.popleft()
        res.append(num)
        q.append(num+"0")
        q.append(num+"1")
    return res
    

if __name__ == "__main__":
    print(first_k_binary_numbers(5))
    print(first_k_binary_numbers(10))
