# spent 15 minutes
# stack but i like delimiter better
# TC - O(n) 
# SC - O(n)

def reverse_words(s: str) -> str:
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

    
def reverse_words_stack(s: str) -> str:
    if not s: 
        return ""
    
    stack = []
    word = ""
    
    # push words into stack
    for c in s:
        if c == " ":
            if word:
                stack.append(word)
                word = ""
        else:
            word += c
            
    if word: # last word
        stack.append(word)
        
    # pop from stack to reverse
    res = []
    while stack:
        res.append(stack.pop())
        
    res_str = res[0] # already checked for empty case
    for i in range(1, len(res)):
        res_str += " " + res[i]
    return res_str
    
    
if __name__ == "__main__":
    s1 = "Uber Career Prep"
    print("Expected: Prep Career Uber")
    print("Actual  :", reverse_words_stack(s1))
    
    s2 = "Emma lives in Brooklyn, New York."
    print("Expected: York. New Brooklyn, in lives Emma")
    print("Actual  :", reverse_words_stack(s2))

    