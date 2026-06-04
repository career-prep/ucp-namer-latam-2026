def breakWord(word, dictionary):
    """
    idea: 
    - create an empty trie
    - walk through each word in dictionary 
        - record it into trie, if reaching the end of word -> add it as KEY
    - backtrack function
        - unlocal i 
        - base case: if i >= len(word) -> return
        - if word[i] not in current node 
        -> if key != None -> add it into ans list
        -> return 
        - if "KEY" in node -> key = new key 
        - backtrack(i + 1, cur[i], key)
 
    - while loop (i < len(word)) (i starts from 0)
        - if word[i] not in trie -> return False 
        - backtrack(i, trie, key)
    
    - return True, ans list
    """
    trie = {}
    s = word.lower()
    ans = []
    for w in dictionary:
        cur = trie
        lower_word = w.lower()
        for ch in lower_word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur["KEY"] = lower_word
    
    def backtrack(i, node, first_key, first_key_end):
        # first_key tracks the first complete word we've seen
        # first_key_end is the index where that word ended

        if i >= len(s):
            if first_key is not None:
                ans.append(first_key)
                return first_key_end
            return -1

        if s[i] not in node:
            if first_key is not None:
                ans.append(first_key)
                return first_key_end
            return -1

        next_node = node[s[i]]

        # If this node marks the end of a word and we haven't found one yet, use it
        if "KEY" in next_node and first_key is None:
            first_key = next_node["KEY"]
            first_key_end = i

        return backtrack(i + 1, next_node, first_key, first_key_end)

    i = 0
    while i < len(s):
        if s[i] not in trie:
            return False, []
        endIdx = backtrack(i, trie, None, -1)
        if endIdx == -1:
            return False, []
        i = endIdx + 1
        
    return True, ans


dictionary = [
    "Elf",
    "Go",
    "Golf",
    "Man",
    "Manatee",
    "Not",
    "Note",
    "Pig",
    "Quip",
    "Tee",
    "Teen",
]

print('Input: "mangolf" ->', breakWord("mangolf", dictionary))
print('Input: "manateenotelf" ->', breakWord("manateenotelf", dictionary))
print('Input: "quipig" ->', breakWord("quipig", dictionary))