"""
1 hour and 45 minutes
"""

from collections import deque

class graph:
    def __init__(self):
        self.dic = {}

    def create(self, input):
        for x, y in input:
            if x in self.dic:
                self.dic[x].append(y)
            else:
                self.dic[x] = [y]
            if y not in self.dic:
                self.dic[y] = []

    def dfs(self, target):
        """
        set = 1,2,
        queue = [3, 3,0]
        
        """
        if not self.dic:
            return False
        visited = set()
        queue = []
        first_key = next(iter(self.dic))
        queue.append(first_key)

        while queue:
            val = queue.pop()
            if val in visited:
                continue
            if val == target:
                return True
            if val in self.dic:
                queue.extend(self.dic[val])

            visited.add(val)
        return False

    def bfs(self, target):
        """
        set = 1,2,
        queue = [3, 3,0]
        
        """
        if not self.dic:
            return False
        visited = set()
        queue = []
        first_key = next(iter(self.dic))
        queue.append(first_key)

        while queue:
            val = queue.pop(0)
            if val in visited:
                continue
            if val == target:
                return True
            if val in self.dic:
                queue.extend(self.dic[val])

            visited.add(val)
        return False
    
    def topo(self):
        """
        
        """
        
        ind = {}
        for key, items in self.dic.items():
            ind[key] = 0

        for key, val in ind.items():
            for ch in self.dic[key]:
                ind[ch] += 1
        

        queue = deque()
        for key, val in ind.items():
            if ind[key] == 0:
                queue.append(key)
        
        res = []
        visited = set()
        while queue:
            val = queue.popleft()
            for ch in self.dic[val]:
                ind[ch] -= 1
                if ind[ch] == 0:
                    queue.append(ch)      
            res.append(val)

        return  res

    def topo_dfs(self):
        """
        
        """
        
        ind = {}
        for key, items in self.dic.items():
            ind[key] = 0

        for key, val in ind.items():
            for ch in self.dic[key]:
                ind[ch] += 1
        

        queue = deque()
        for key, val in ind.items():
            if ind[key] == 0:
                queue.append(key)
        
        res = []
        visited = set()
        while queue:
            val = queue.pop()
            for ch in self.dic[val]:
                ind[ch] -= 1
                if ind[ch] == 0:
                    queue.append(ch)
           
            res.append(val)

        return  res
    
