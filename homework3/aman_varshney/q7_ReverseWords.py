# spent 25 minutes
# can use stack but i like delimiter better
# TC - O(n) 
# SC - O(n)

def reverseWords(s: str) -> str:
    if not s: # empty case
        return ""
    
    # split phrase into words by space delimiter and reverse
    words = s.split(" ")
    words.reverse()
    
    # build string
    res = words[0]
    for i in range(1, len(words)):
        res += " " + words[i]
    return res

    
    
    
if __name__ == "__main__":
    s1 = "Uber Career Prep"
    print("Expected: Prep Career Uber")
    print("Actual  :", reverseWords(s1))
    
    s2 = "Emma lives in Brooklyn, New York."
    print("Expected: York. New Brooklyn, in lives Emma")
    print("Actual  :", reverseWords(s2))

    