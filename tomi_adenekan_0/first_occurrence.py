"""
Time Cmplexity = O(n)
Space Complexity = O(n)
Time used = 10 minutes

"""
def main(mes):
    res = ""
    seen = set()
    for ch in mes:
        if ch not in seen:
            res += ch
        seen.add(ch)

    return res
       

    

message = "abracadabra"
print(main(message))
second = "Uber Career Prep"
print(main(second))
