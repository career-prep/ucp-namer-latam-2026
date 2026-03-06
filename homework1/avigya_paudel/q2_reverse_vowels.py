# TIME COMPLEXITY: O(N) 
# SPACE COMPEXITY: O(N)
# TIME TAKEN: ~7 minutes
# TECHNIQUE: Not sure if it aligns with any

def reverse_vowels(input_str):
    """
    returns a string with everything the same as input_str
    except index of vowels are reversed
    """

    vowels = {"a", "e", "i", "o", "u"}
    vowel_arr = collect_vowels(input_str, vowels)
    vowel_arr.reverse()
    vowel_idx = 0
    
    res = ""
    for c in input_str:
        if c.lower() in vowels:
            res += vowel_arr[vowel_idx] 
            vowel_idx += 1 
        else:
            res += c
    return res

def collect_vowels(str, vowels):
    """
    returns an array of all the vowels in the sequence from left to right
    """
    ans = []
    for chr in str:
        if chr.lower() in vowels:
            ans.append(chr)
    return ans 

if __name__ == "__main__":
    print(reverse_vowels("Uber Career Prep"))
    print(reverse_vowels("xyz"))
    print(reverse_vowels("flamingo"))
    