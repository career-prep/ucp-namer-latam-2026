def ReverseWords(sentence):

    words = sentence.split()

    def dfs(words):

        if len(words) <= 1:
            return words
        
        return [words[-1]] + dfs(words[:-1])
    
    return " ".join(dfs(words))

sentence = "Uber Career Prep"
# Output: "Prep Career Uber"

sentence = "Emma lives in Brooklyn, New York."
# Output: "York. New Brooklyn, in lives Emma"

print(ReverseWords(sentence))

# 30