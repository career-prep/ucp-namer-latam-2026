# Time complexity: O(n)
# Space complexity: O(n)

def FirstOccurrence(str):
    uniqueChars = {}
    chars = []
    for char in str:
        if char not in uniqueChars:
            uniqueChars[char] = 1
            chars.append(char)
    return "".join(chars)

if __name__ == '__main__':
    inputStr = "abracadabra"
    #inputStr = "Uber Career Prep"
    #inputStr = "zzyzx"
    #inputStr = ""
    print("Input String:", inputStr)
    print("Output:", FirstOccurrence(inputStr))

# ~ time spent: 7 minutes