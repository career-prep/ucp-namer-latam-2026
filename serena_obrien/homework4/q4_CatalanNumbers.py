from math import factorial

# Time complexity: O(n*k) -> O(n^2), where n is the number of factorial calls and k is the average depth of the factorial
# Space complexity: O(n)

# Technique: Dynamic programming: memoization? I looked this one up and saw another solution but I didn't really understand it...

def CatalanNumbers(n):
    res = []
    facts = {}

    def fact(x):
        if x not in facts:
            facts[x] = factorial(x)
        return facts[x]
    
    for i in range(n + 1):
        cn = fact(2*i) // (fact(i + 1)*fact(i))
        res.append(cn)

    return res

if __name__ == "__main__":
    ns = [0, 1, 3, 5, 10]
    for n in ns:
        print(CatalanNumbers(n))
    

# ~ time spent: ~20 minutes