# Trie as a parameter & Dynamic Programming Memoization
# O(n * L) Time Complexity, where n is the length of the input string and L is the length of the longest dictionary word
# O(n) Space Complexity, where n is the length of the input string (because memo has (n+1) entries)
# Given a string of characters without spaces and a dictionary of valid words, determine if it can be broken into a list of valid words by adding spaces. 

from q1_Trie import Trie

def wordBreak(input, dictionary):

    # You cannot put spaces inside nothing, and if we have no valid words then we cannot determine if the input can be broken into valid words
    if not input or not dictionary:
        return False
    

    # At this point of the interview, I would ask if it is safe to assume that all inputs will be lowercase and be valid alphabetical characters
    # If not all characters were lowercase, I would have to convert each char to lowercase so that my Trie class can handle it properly


    # My first attempt at this problem was to iterate through the input and the trie simultaneously but I started to realize that in some cases,
    # I would have to kind of backtrack to an earlier index and re-iterate through parts I have already iterated through... 
    # That seems inefficient and weird, but can also probably be optimized with dynamic programming

    # I believe memoization is best for solving this problem because if we reach the end of a valid word, we would then need to check if the rest of the 
    # substring can be segmented correctly. We would have to do this for every valid word, which would lead to us re-doing a lot of work.
    # Instead we can use memoization to store the results of our work in a cache so that we do not repeat any work we do.

    # memo[i] holds a boolean value on whether the substring starting at index i can be segmented into valid words
    # therefore, memo[0] is the answer to this problem

    memo = {}

    # An empty string is segmentable
    memo[len(input)] = True 


    def dfs(index):

        # To avoid redoing work, check if the result is already in the memo (cache)
        if index in memo:
            return memo[index]


        # If we get here then we need to figure out if the substring starting at 'index' is segmentable

        node = dictionary.root

        # Walk down the trie starting at char input[index]
        for k in range(index, len(input)):

            char = input[k]
            childIndex = ord(char) - ord('a')

            # If the char node we want is not down this trie path, we have encountered an invalid word
            if node.children[childIndex] == None:
                break

            # Otherwise, the char node we want is inside the trie path, so traverse to it
            node = node.children[childIndex]


            # If we reached a valid word, act as if we put a space after this word, and recurse on the next substring
            if node.validWord:

                if dfs(k+1) == True: # If the next substring is segmentable, then this word can be added to the left of the next substring, and still be segmentable
                    memo[index] = True
                    return True
                
        
        # If we get here then this part of the substring is not segmentable because there are invalid words or unsegmentable substrings
        memo[index] = False
        return False



    dfs(0)

    return memo[0]




# 36 minutes

# Test Cases

input1 = "mangolf"
input2 = "manateenotelf"
input3 = "quipig"
input4 = "brazilworldcupchampionsthisyear"

dictionary1 = ["Elf", "Go", "Golf", "Man", "Manatee", "Not", "Note", "Pig", "Quip", "Tee", "Teen"]
dictionary2 = ["Brazil", "Bra", "World", "Cup", "Champ", "Champions", "Ions", "This", "Year"]

def makeTrie(dictionary):
    trie = Trie()

    for word in dictionary:
        trie.insert(word.lower()) # The trie I created in q1 uses Ascii value of lowercase characters to work correctly

    return trie

trie1 = makeTrie(dictionary1)
trie2 = makeTrie(dictionary2)


print(wordBreak(input1, trie1))
print(wordBreak(input2, trie1))
print(wordBreak(input3, trie1))
print(wordBreak(input4, trie2))
