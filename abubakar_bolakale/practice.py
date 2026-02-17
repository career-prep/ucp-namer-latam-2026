class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        ans = []
        i = 0
        
        while i < n:
            lst = []
            letters = 0
            
            while i < n:
                if letters + len(words[i]) + len(lst) > maxwidth:
                    break
                lst.append(words[i])
                letters += len(word[i])
                i += 1
                
            last_word = (i == n)
            k = len(lst)
            
            if last_word or k == 1:
                line = " ".join(lst)
                rem = maxwidh - len(line)
                ans.append(line + (" " * rem))
                continue
            
            space = maxwidth - letters
            gaps = k - 1
            extra = space // gaps
            left = space % gaps
            
            parts = []
            for i in range(gaps):
                parts.append(lst[g])
                parts.append(" " *(extra + (1 if g < left else 0)))
            parts.append(lst[-1])
            
            ans.append("".join(parts))
            
        return ans
    
    
    
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:  
        ans = []
        def backtrack ( path, start, curr):
            if curr == target:
                ans.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                val = candidates[i]
                
                if val + curr > target:
                    continue
                
                path.append(val)
                backtrack(path, i , curr + val)
                path.pop()
                
        backtrack([], 0, 0 )
        return ans
                
            