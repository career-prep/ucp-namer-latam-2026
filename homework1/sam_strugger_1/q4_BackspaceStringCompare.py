# This is a sort the array then solve problem
# Time and Space complexity are O(n+m)

def main():
    test1 = backspaceStringCompare('abcde', 'abcde')
    print(test1)

    test2 = backspaceStringCompare('Uber Career Prep', 'u#Uber Career Prep')
    print(test2)

    test3 = backspaceStringCompare('#', '#######')
    print(test3)

    test4 = backspaceStringCompare('asdfadf###', 'asdfadf')
    print(test4)
def backspaceStringCompare(str1,str2):

    def applyHashtags(str):
        tag_count = 0
        new_str = ''
        for c in reversed(str):
            if c == '#':
                tag_count+=1
            elif tag_count > 0:
                tag_count-=1
                continue
            else:
                new_str+=c   # I forgot that making this a list instead of string would reduce the space complexity since strings are immutable
        return new_str[::-1]
    
    return applyHashtags(str1) == applyHashtags(str2)

main()

# this solution took me 25 minutes