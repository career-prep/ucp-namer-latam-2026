def catalanNumbers(n):
    """
    idea:
    - edge case: if n == 0-> return []
    - create empty list with n + 1 elements 
    - at first index => 1 
    - have separate function to calculate this (2n)! / (n+1)!n! -> calculate element at index n in list 
    by multiplying with previous value
    - walk through from 0 to n + 1:
        - call function with parameter i 
        - add this into answer list 
    
    - return ans 

    time: O(n)
    space: O(n)
    """
    if n == 0:
        return []
    
    ans = [1]*(n + 1)
    
    def getAns(i):
        return ans[i - 1] * 2 * (2 * i - 1) // (i + 1)
    
    for i in range(1, n + 1):
        ans[i] = getAns(i)
    
    return ans 

print(catalanNumbers(1))
print(catalanNumbers(5))