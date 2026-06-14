# Dynamic Programming - Tabulation (Bottom-Up)
# O(n) Time Complexity
# O(n) Space Complexity
# The Catalan numbers are a mathematical sequence of numbers. The nth Catalan number is defined as (2n)! / (n+1)!n!. 
# Given a non-negative integer n, return the Catalan numbers in the range [0, n]

def catalanNumbers(n):

    # After reading the description of this problem, I started to get reminded of Fibonnaci Number Leetcode,
    # which can be solved with tabulation and memoization. Although the process which stood out most to me was tabulation.
    # In Fibonnaci, you need the last two results to calcualte the next result, so you could keep a table of 0 to n (inclusive)
    # where index 0 has Fib(0) = 0 and index 1 has Fib(1) = 1 initially. With those two spots filled out, you can
    # easily fill out the remaining spots with a for loop and this line: Fib[i] = Fib[i-2] + Fib[i-1]

    # Factorials work similarly. 5! = 5 * 4 * 3 * 2 * 1. So if I know 4!, I can easily get 5! by multiplying the value of 4! by 5.
    # Factorial of n can easily be acquired if we knew factorial of (n-1)... because n! = n * (n-1)!

    
    # Let's get some base cases out of the way
    if n == 0:
        return [1]
    
    if n == 1:
        return [1, 1]



    # Perhaps we should use Tabulation to get and store the values of factorials up to 2n. Then using the factorials table,
    # We can easily get the values of (2n)!, (n+1)!, and n! for the Catalan Number

    factorials = [0] * (2*n + 1) # We must do (2 * n + 1) so we have an index for 2n. Index of 2n will acces value of (2n)!
    factorials[0] = 1 # 0! = 1
    factorials[1] = 1 # 1! = 1

    # Populate the factorials table
    for i in range(2, len(factorials)):
        factorials[i] = i * factorials[i-1]

    

    # Now that we have the value of all the factorials, we can easily generate the catalan numbers
    catalan = []

    for i in range(n+1):
        numerator = factorials[2 * i]
        denominator = factorials[i+1] * factorials[i]

        catalanNum = numerator // denominator

        catalan.append(catalanNum)



    return catalan




# 22 minutes



# Test Cases

print(catalanNumbers(1))
print(catalanNumbers(5))
print(catalanNumbers(3))
print(catalanNumbers(4))
print(catalanNumbers(0))