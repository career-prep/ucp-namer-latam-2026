# spent 40 minutes
# bfs 
# TC - O(k)
# SC - O(k)

from collections import deque


def firstKBinary(k: int) -> list[str]:
    if k <= 0: # empty case
        return []
    
    binary_num_list = ["0"] 
    queue = deque(["1"]) 
    
    for i in range(1, k): # iterate through range
        curr = queue.popleft()
        binary_num_list.append(curr) 
        # add next binary strings
        queue.append(curr + "0")
        queue.append(curr + "1")
        
    return binary_num_list
        

    
    
    
def expand_list(l): 
    # converts a list to str
    if not l:
        return ""
    res = "[" + l[0] 
    for i in range(1, len(l)):
        res += ", " + l[i]
    res += "]"
    return res
    
if __name__ == "__main__":
    input1 = 5
    print("Expected: [0, 1, 10, 11, 100]")
    print("Actual :", expand_list(firstKBinary(input1)))
    
    input2 = 10
    print("Expected: [0, 1, 10, 11, 100, 101, 110, 111, 1000, 1001]")
    print("Actual: ", expand_list(firstKBinary(input2)))