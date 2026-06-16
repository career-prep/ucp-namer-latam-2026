#Samaksh Arora
#Question 2 - Boggle
#Trie as a parameter
#Time Complexity: O(N * M^8) where N is number of cells on board and M is max path length (8 directions with backtracking)
#Space Complexity: O(D * L) for trie where D is dictionary size and L is average word length; O(M) for recursion stack 
#Time Spent: >40 minutes


from q1_buildTrie import Trie


def findWordsOnBoggle(board, dictionary):

    if not board or not board[0] or not dictionary:
        return []

    board = [[letter.lower() for letter in row] for row in board]

    trie = Trie()
    words = [word.lower() for word in dictionary]
    for i, word in enumerate(words):
        trie.insert(word, i)

    numberOfRows, numberOfCols = len(board), len(board[0])
    foundWords = []

    def dfs(currentRow, currentCol, currentNode):
        if currentRow < 0 or currentRow >= numberOfRows:
            return
        if currentCol < 0 or currentCol >= numberOfCols:
            return
        if board[currentRow][currentCol] == '*':
            return

        currentChar = board[currentRow][currentCol]
        charIndex = ord(currentChar) - ord('a')

        if not currentNode.children[charIndex]:
            return

        board[currentRow][currentCol] = '*'
        prevNode = currentNode
        currentNode = currentNode.children[charIndex]

        if currentNode.idx != -1:
            foundWords.append(words[currentNode.idx])
            currentNode.idx = -1
            currentNode.refs -= 1
            if not currentNode.refs:
                prevNode.children[charIndex] = None
                currentNode = None
                board[currentRow][currentCol] = currentChar
                return

        dfs(currentRow + 1, currentCol, currentNode)
        dfs(currentRow - 1, currentCol, currentNode)
        dfs(currentRow, currentCol + 1, currentNode)
        dfs(currentRow, currentCol - 1, currentNode)
        dfs(currentRow + 1, currentCol + 1, currentNode)
        dfs(currentRow + 1, currentCol - 1, currentNode)
        dfs(currentRow - 1, currentCol + 1, currentNode)
        dfs(currentRow - 1, currentCol - 1, currentNode)

        board[currentRow][currentCol] = currentChar

    for row in range(numberOfRows):
        for col in range(numberOfCols):
            dfs(row, col, trie.root)

    return foundWords


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
