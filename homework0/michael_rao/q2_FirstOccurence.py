# time: O(n), space: O(n)

def first_occurence(str):
    res = ""
    seen = set()

    for c in str:
        if c not in seen:
            res += c
            seen.add(c)
    
    return res

print("Input String: abracadabra")
print("Output:", first_occurence("abracadabra"))

print("Input String: Uber Career Prep")
print("Output:", first_occurence("Uber Career Prep"))

print("Input String: aabcbc")
print("Output:", first_occurence("aabcbc"))

# took 5 minutes