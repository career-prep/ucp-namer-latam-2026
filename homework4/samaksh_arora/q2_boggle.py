#Samaksh Arora
#Question 2 - Boggle
#Trie as a parameter
#Time Complexity:
#Space Complexity:
#Time Spent:


from q1_buildTrie import Trie


def findWordsOnBoggle(board, dictionary):

    if not board or not board[0] or not dictionary:
        return []
    
    board = [[letter.lower() for letter in row] for row in board]

    trie = Trie()
    for word in dictionary:
        trie.insert(word.lower())

    numberOfRows, numberOfCols = len(board), len(board[0])
    foundWords = set()
    setOfVisitedLetters = set()
    def dfs(currentRow, currentCol, currentNode, path):
        if currentNode.validWord:
            foundWords.add(path)

        # Check boundaries and visited
        if currentRow < 0 or currentRow >= numberOfRows:
            return
        if currentCol < 0 or currentCol >= numberOfCols:
            return
        if (currentRow, currentCol) in setOfVisitedLetters:
            return  
        currentChar = board[currentRow][currentCol]
        if currentChar not in currentNode.children:
            return
        setOfVisitedLetters.add((currentRow, currentCol))
        nextNode = currentNode.children[currentChar]
        dfs(currentRow + 1, currentCol, nextNode, path + currentChar)
        dfs(currentRow - 1, currentCol, nextNode, path + currentChar)
        dfs(currentRow, currentCol + 1, nextNode, path + currentChar)
        dfs(currentRow, currentCol - 1, nextNode, path + currentChar)
        setOfVisitedLetters.remove((currentRow, currentCol))
        
    for row in range(numberOfRows):
        for col in range(numberOfCols):
            dfs(row, col, trie.root, "")

    return list(foundWords)


#Test Cases
board = [["A","D","E"],["R","C","P"],["L","A","Y"]]
dictionary = ["Ace","Ape","Cape","Clap","Clay","Gape","Grape","Lace","Lap","Lay","Mace","Map","May","Pace","Pay","Race","Rap","Ray","Tap","Tape","Trace","Trap","Tray","Yap"]
expected = ["Ace","Race","Pace","Lace","Pay","Lay","Clay","Ray","Lap","Rap","Clap","Ape","Cape","Yap"]
assert findWordsOnBoggle(board, dictionary) == expected

#Extra: 
board = [["C","A","T"],["O","D","O"],["G","X","Z"]]
dictionary = ["CAT","DOG","COD","CAD","ODD"]
expected = ["CAT","DOG","COD"]
assert findWordsOnBoggle(board, dictionary) == expected
