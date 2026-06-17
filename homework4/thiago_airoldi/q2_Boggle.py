# Trie as a parameter

# O(m * n * 8^L) Time Complexity, where 'm' is the number of rows in board, 'n' is the number of columns in board, and '8^L' stands for the maximum recursion depth
# for the longest word. At any char we have 8 directions to choose from, and L is the length of the longest word in the dictionary. At each step of the DFS we explore
# up to 8 neighbors and the recursion depth is at most L

# O(L + W*L) Space Complexity, we use O(L) from the DFS recursion depth, and we use O(W*L) to store the words in res, where 'W' is the number of words found and 'L' is the
# longest word length

# Boggle is a word game in which players compete to find the most words on a square grid of random letters. 
# Valid words must be at least three characters and formed from non-overlapping (i.e., a position on the board can only be used once in a word) adjacent (including diagonal) 
# letters. Given a Boggle board and a dictionary of valid words, return all valid words on the board.


from q1_Trie import Trie

# I am passing in a trie as 'dictionary' since the most relevant problem solving technique from this assignment was "Trie as a parameter", but reading the problem description
# made me think that 'dictionary' was really just an array of Strings which I then needed to insert all of those strings into a Trie, and then solve the problem using
# the trie I created inside my function.
def boggle(board, dictionary):
    
    # If we have no board or not dictionary of valid words, then we cannot return any valid words
    if not board or not board[0] or not dictionary:
        return []
    
    ROWS = len(board)
    COLS = len(board[0])
    
    visited = set() # Stores (r, c), however this set starts empty for each new word search

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def isValid(r, c):
        if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited:
            return False
        else:
            return True
        

    def dfs(r, c, node, path):

        path.append(board[r][c].lower())
        visited.add((r, c))

        # If we reach the end of a valid word in the dictionary, add it to the result set
        if node.validWord:
            res.add("".join(path))


        # Traverse to all neighbors that were not visited yet AND are valid nodes in the trie
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if not isValid(nr, nc):
                continue

            nextChar = board[nr][nc].lower()
            nextIdx = ord(nextChar) - ord('a')

            if node.children[nextIdx] != None:
                dfs(nr, nc, node.children[nextIdx], path)


        # Backtrack
        path.pop()
        visited.remove((r, c))







    res = set() # I chose to use a set so that I do not add duplicate words
    root = dictionary.root

    path = [] # Current dfs path we took to reach the end of a word. Once we backtrack, we pop the char we just added so that each new word search has a blank path
              # to start out

    for r in range(ROWS):
        for c in range(COLS):

            # Start a DFS from this cell if this char is the first letter to a valid word
            char = board[r][c].lower()
            idx = ord(char) - ord('a')

            if root.children[idx] != None:
                dfs(r, c, root.children[idx], path)



    # I ran into a slight issue. Since I make all chars lowercase so that my Trie can work as expected, all words in res are lowercase, when they might need to be returned
    # in the exact case they were given.

    # If the 'dictionary' parameter is actually supposed to be an array of strings, I can make a hashmap which maps a lowercase word to the original word
    # but I passed in dictionary as a Trie... Since the only input I was given just had the first char in each word as a capital letter, I can use the .title() function
    # to fix all the words in res, however that only works for all cases IF every case gives me words that only have the first letter capitalized. 
    
    # If I ever get a word which is like "aBcdEf", my code would not be able to return the original word UNLESS the dictionary parameter was actually an array of strings 
    # so that I could build the trie inside this function AND create a hashmap of {lowercaseWord: originalWord}


    # Apart from the case issue, I am still able to return the correct words
    return list(res)

    

    

# 34 minutes





# Test Cases

dictionary1 = ["Ace", "Ape", "Cape", "Clap", "Clay",  "Gape", "Grape", "Lace", "Lap", "Lay", "Mace", "Map", "May", "Pace", "Pay", "Race", "Rap", "Ray", "Tap", "Tape",
               "Trace", "Trap", "Tray", "Yap", ]

board1 = [['A', 'D', 'E'],
          ['R', 'C', 'P'],
          ['L', 'A', 'Y']]

def makeTrie(dictionary):
    trie = Trie()

    for word in dictionary:
        trie.insert(word.lower()) # The trie I created in q1 uses Ascii value of lowercase characters to work correctly

    return trie

trie1 = makeTrie(dictionary1)


print(boggle(board1, trie1))