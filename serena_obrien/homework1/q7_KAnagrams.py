# Time complexity: O(n)
# Space complexity: O(n)

# Technique: Two arrays increment/decrement hashmap counts

def KAnagrams(str1, str2, k):
    if len(str1) != len(str2):
        return False

    freq = {}

    for ch in str1:
        freq[ch] = freq.get(ch, 0) + 1

    changes = 0
    for ch in str2:
        if freq.get(ch, 0) > 0:
            freq[ch] -= 1
        else:
            changes += 1
            if changes > k:
                return False

    return True
        
if __name__ == '__main__':

    # inputStr1 = "debit curd"
    # inputStr2 = "bad credit"
    # k = 1
    inputStr1 = "baseball"
    inputStr2 = "basketball"
    k = 2
    # inputStr1 = ""
    # inputStr2 = ""
    # k = 2
    print("Input Strings:", inputStr1, ',', inputStr2)
    print("Input K:", k)
    print("Output:", KAnagrams(inputStr1, inputStr2, k))

# ~ time spent: 20 minutes