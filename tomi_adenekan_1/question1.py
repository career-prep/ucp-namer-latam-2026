"""
fixed-size sliding window
10 minuutes
time complexity = O(n)
space complexity = O(1)
"""

def get_name(lis, k):
    val = 0
   
    for i in range(len(lis)-k+1):
        total = sum(lis[i:i+k])
        val = max(val, total/k)


    return val

lis = [1,1,1,1,-1,-1,2,-1,-1,6]
k = 5

print(get_name(lis, k))
