# This is a tabulation approach, time complexity is O(n^2) and space complexity is O(n)

# Formula (2n)!/ (n+1)!n!

# Recursive formula 

# My instinct is memoization since this seems very similar to fibonacci and other
# recursively defined sequences of numbers

# I couldn't algebraically derive the recursive formula for Catalan numbers so I did look that part up

# Also switched from memoization to tabulation since I was having trouble with the memoization approach

def catalanNumbers(n):
    if n == 1:
        return [1,1]
    elif n == 0:
        return [1]

    result = [0] * (n+1)
    result[0] = 1
    result[1] = 1

    for k in range(2,n+1):
        for i in range(k):
            left_subproblem = result[i]
            right_subproblem = result[k - 1 - i]
            
            result[k] += left_subproblem * right_subproblem

    return result[:n+1]

# This took me around 30 minutes total

# Test Cases
test1 = catalanNumbers(3)
print(test1)

test2 = catalanNumbers(1)
print(test2)

test3 = catalanNumbers(0)
print(test3)
test4 = catalanNumbers(12)
print(test4)