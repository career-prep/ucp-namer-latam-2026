#Technique: Variable size sliding window

#Could not solve in 40 min. The first part is where I reached at the end of 40 min and after time ran out was able to solve
# and the solution is below the actual 40 min one in comments. Took me approx 1 hr. (20 min more after additional 40)

#Time Complexity: 0(n)
#Space Complexity: O(m), where m is no of unique characters in required chars

def shortesSubstring(str1, str2):
    
    need = {}

    for ch in str2:
        need[ch] = need.get(ch, 0) + 1

    l = 0
    need_count = len(need)
    min_length = float('inf')
    have_count = 0
    have = {}

    for r in range(len(str1)):
        have[str1[r]] = have.get(str1[r], 0) + 1

        if str1[r] in need and have[str1[r]] == need[str1[r]]:
            have_count += 1

        

    return min_length

"""
def shortesSubstring(str1, str2):
    
    need = {}
    for ch in str2:
        need[ch] = need.get(ch, 0) + 1

    l = 0
    need_count = len(need)
    have_count = 0
    have = {}

    min_length = float('inf')

    for r in range(len(str1)):
        have[str1[r]] = have.get(str1[r], 0) + 1

        if str1[r] in need and have[str1[r]] == need[str1[r]]:
            have_count += 1

        while have_count == need_count:
            min_length = min(min_length, r - l + 1)

            have[str1[l]] -= 1

            if str1[l] in need and have[str1[l]] < need[str1[l]]:
                have_count -= 1

            l += 1

    return min_length if min_length != float('inf') else -1
"""               

