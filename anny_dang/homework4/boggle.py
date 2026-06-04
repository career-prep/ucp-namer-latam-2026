def boggle(dictionary, board):
    """
    idea:
    - create dictionary trie
        - walk through each word in dictionary
        - if len(word) < 3:
            continue
        - convert word to lowercase
        - have cur = trie
        - for each character in word:
            - if character not in cur:
                - add it
            - move cur to that character node
        - at the end of word:
            - store full word at key "KEY"

    - backtracking function
        - base cases:
            - if cell out of board -> return
            - if board cell is "#" -> return
            - convert board character to lowercase
            - if character not in current trie node -> return
        - move to next trie node
        - if "KEY" in that node:
            - add that word to ans
            - delete "KEY" so we do not add duplicate again
        - mark current board cell as visited with "#"
        - walk through all 8 directions:
            - call backtrack on neighbor cell with next trie node
        - change board cell back to original character

    - main loop:
        - walk through each cell in board
        - if lowercase character at board cell is in trie:
            - call backtrack(cell, trie)
    
    n: number of all characters, L: max length of a word
    time: O(n)
    space: O(n + L)
    """
    trie = {}
    ans = []
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, -1), (-1, 1), (1, 1), (-1, -1)]
    for word in dictionary:
        if len(word) < 3:
            continue

        lower_word = word.lower()
        cur = trie
        for ch in lower_word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        
        cur["KEY"] = word

    def backtrack(r, c, node):
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
            return 

        if board[r][c] == "#":
            return 
        
        ch = board[r][c].lower()
        if ch not in node:
            return 
        
        next_node = node[ch]

        if "KEY" in next_node:
            ans.append(next_node["KEY"])
            del next_node["KEY"]
        
        temp = board[r][c]
        board[r][c] = "#"
        for x, y in directions:
            backtrack(r + x, c + y, next_node)
        
        board[r][c] = temp
    
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c].lower() in trie:
                backtrack(r, c, trie)
    
    return ans 


if __name__ == "__main__":
    dictionary = [
        "Ace", "Ape", "Cape", "Clap", "Clay",
        "Gape", "Grape", "Lace", "Lap", "Lay",
        "Mace", "Map", "May", "Pace", "Pay",
        "Race", "Rap", "Ray", "Tap", "Tape",
        "Trace", "Trap", "Tray", "Yap",
    ]

    board = [
        ["A", "D", "E"],
        ["R", "C", "P"],
        ["L", "A", "Y"],
    ]

    expected = [
        "Ace", "Race", "Pace", "Lace", "Pay",
        "Lay", "Clay", "Ray", "Lap", "Rap",
        "Clap", "Ape", "Cape", "Yap",
    ]

    print("Dictionary:")
    print(dictionary)
    print()

    print("Board:")
    for row in board:
        print(row)
    print()

    print("Expected Output:")
    print(expected)
    print()

    print("Your Output:")
    print(boggle(dictionary, board))
