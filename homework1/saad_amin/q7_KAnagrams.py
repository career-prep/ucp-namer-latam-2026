#Technique: Two strings increment/decrement hashmap count

#Time Complexity: O(n + m)
#Space Complexity: O(n)

def Kanagrams(str1, str2, k):

    if len(str1) != len(str2):
        return False
    
    freq = {}

    for ch in str1:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in str2:
        if ch not in freq:
            k -= 1

            if k < 0:
                return False
            
        else:
            freq[ch] -= 1
            if freq[ch] == 0:
                del freq[ch]

    return True

print(Kanagrams("apple", "peach", 2))
print(Kanagrams("apple", "peach", 1))
print(Kanagrams("cat", "dog", 3))
print(Kanagrams("Saad", "Rish", 4))

#Time taken: 26 min