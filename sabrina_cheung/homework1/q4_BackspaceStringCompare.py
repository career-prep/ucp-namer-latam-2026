"""
Technique Used: two string two pointer
Time Complexity: O(n+m)
Space Complexity: O(1)

Intuition: Use two pointers to compare the two strings from end to beginning.
When hitting a hashtag, move pointer backward until the next non-hashtag character is found. If the characters are different, return False. 
If both pointers reach the beginning of the strings, return True.
"""

def BackspaceStringCompare(str1, str2):
    p1 = len(str1) - 1
    p2 = len(str2) - 1
    
    back1 = 0
    back2 = 0

    while p1 >= 0 or p2 >= 0:
        while p1 >= 0:
            if str1[p1] == '#':
                p1 -= 1
                back1 += 1
            elif back1 > 0:
                p1 -= 1
                back1 -= 1
            else:
                break
        while p2 >= 0:
            if str2[p2] == '#':
                p2 -= 1
                back2 += 1
            elif back2 > 0:
                p2 -= 1
                back2 -= 1
            else:
                break
        
        if p1 >= 0 and p2 >= 0:
            if str1[p1] != str2[p2]:
                return False
        elif p1 >= 0 or p2 >= 0:
            return False
        p1 -= 1
        p2 -= 1
    return True



test = [('abcde', 'abcde'),
        ('Uber Career Prep', 'u#Uber Careee#r Prep'),
        ('xy#z', 'xzz#'),
        ('abcdef###xyz', 'abcw#xyz'),
        ('helloworld', 'heelloworlddd##'),
        ('', '###')]

for i in (test):
    print(BackspaceStringCompare(i[0], i[1]))

# Time Spent: 40 mins