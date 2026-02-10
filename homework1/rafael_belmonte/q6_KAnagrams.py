#two arrays/strings increment/decrement hashmap counts
#time complexity: O(n)
#space complexity: O(1) - since the character set is fixed (assuming only lowercase letters)
#31 minutes

def k_anagrams(s1, s2, k):
    if len(s1) != len(s2):
        return False
    count = {}
    for char in s1:
        count[char] = count.get(char, 0) + 1
    for char in s2:
        if char in count:
            count[char] -= 1
    changes_needed = sum(value for value in count.values() if value > 0)
    return changes_needed <= k

#test cases

s1_1, s1_2 = "apple", "peach"
assert k_anagrams(s1_1, s1_2, 1) == False

s2_1, s2_2 = "apple", "peach"
assert k_anagrams(s2_1, s2_2, 2) == True

s3_1, s3_2 = "cat", "dog"
assert k_anagrams(s3_1, s3_2, 3) == True

s4_1, s4_2 = "debit curd", "bad credit"
assert k_anagrams(s4_1, s4_2, 1) == True

s5_1, s5_2 = "baseball", "basketball"
assert k_anagrams(s5_1, s5_2, 2) == False

print("wow")