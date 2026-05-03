#Time complexity: O(K)
#Space Complexirt: O(k)
#Technique: BFS (tree) 


from collections import deque

def firstk_binary(k):
    if k <= 0:
        return []
    
    result = ["0"]
    queue = deque(["1"])
    
    while len(result) < k:
        curr = queue.popleft()
        result.append(curr)
        
        queue.append(curr + "0")
        queue.append(curr + "1")
    
    return result

def test_first_k_binary():
    print(firstk_binary(5), "Expected:", ["0", "1", "10", "11", "100"])
    print(firstk_binary(10), "Expected:", ["0", "1", "10", "11", "100", "101", "110", "111", "1000", "1001"])
    
test_first_k_binary()

#Time: 35 min
    
    