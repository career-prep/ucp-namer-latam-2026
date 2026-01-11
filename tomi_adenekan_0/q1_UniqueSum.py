"""
Time Cmplexity = O(n)
Space Complexity = O(n)
Time used = 12 minutes

"""
from collections import defaultdict
def main(lst):
    res = 0
    seen = set()
    for num in lst:
        if num not in seen:
            res += num
        seen.add(num)

    return res
       

    

lst = [1,10,8,3,2,5,7,2,-2,-1]
print(main(lst))
