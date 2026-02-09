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
                

