# Time: 21 minutes and 14 seconds
# Technique: Forward and Backward Two pointer

def ReverseVowels(word):
    list1 = list(word)
    left = 0
    right = len(list1) - 1
    while right > left:
        if right > left and list1[right].lower() not in "aieou":
            right -= 1
        elif right > left and list1[left].lower() not in "aieou":
            left += 1
        else:
            temp = list1[right]
            list1[right] = list1[left]
            list1[left] = temp
            right -= 1
            left += 1
    
    return "".join(list1)
print(ReverseVowels("Uber Career Prep"))
print(ReverseVowels("xyz"))
print(ReverseVowels("flamingo"))
