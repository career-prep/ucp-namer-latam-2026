#Samaksh Arora
#ReverseVowels
#Time Complexity: O(n)
#Space Complexity: O(n)
#Two Pointers
def ReverseVowels(string1):
    leftPtr = 0
    rightPtr = len(string1) - 1

    string1 = list(string1)

    vowels = {"a", "e", "i", "o", "u", "A", "E","I", "O", "U"}

    while leftPtr < rightPtr:
        while leftPtr < rightPtr and (string1[leftPtr] not in vowels):
            leftPtr+=1
        while leftPtr < rightPtr and ((string1[rightPtr] not in vowels)):
            rightPtr-=1
        
        temp = string1[leftPtr]
        string1[leftPtr] = string1[rightPtr]
        string1[rightPtr] = temp

        leftPtr += 1
        rightPtr -=1

    result = ''.join(string1)
    return result

test = "Uber Career Prep"
print(ReverseVowels(test)) #output = eber Ceraer PrUp

test = "Flamingo"
print(ReverseVowels(test)) #output = Flominga

#Time Spent: 15 minutes