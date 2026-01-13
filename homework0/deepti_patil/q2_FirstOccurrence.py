#given string return a string that only contains the first occurrence of each character
#create a hash set to store the characters we have seen so far
#loop through the string and for each character check if it is in the hash set
#if it is not in the hash set add it to the hash set and to the result string
#return the result string

def first_occurrence(string):
    seen = set() #hash set to store seen characters
    result = [] #list to store result characters

    for char in string:
        if char not in seen: #if character has not been seen before
            seen.add(char) #add character to seen set
            result.append(char) #add character to result list

    return ''.join(result) #return the result string by joining the list

#example usage
string = 'aaaaababbabbcbbccccccccc'
print(first_occurrence(string)) #prints 'abc'

#time spent: 12 min
