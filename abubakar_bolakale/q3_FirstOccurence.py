class solution:
    def FirstOcurrence(self, word):
        unique = []
        seen = set()
        for letter in word:
            if letter not in seen:
                unique.append(letter)
                seen.add(letter)
        return "".join(unique)

sol = solution()
arr = ["abracadabra",
       "Uber Career Prep",
       "zzyzx"]

for test in arr:
    print(sol.FirstOcurrence(test)) 
    
# Spent a total of 10 mins on this question