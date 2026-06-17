from collections import defaultdict, deque


class Graph:
    def __init__(self, edges):
        self.adj = defaultdict(list)
        self.nodes = set()

        for u, v in edges:
            self.adj[u].append(v)
            self.nodes.add(u)
            self.nodes.add(v)

        
    def dfs(self, target):
        visited = set()

        def helper(node):
            if node == target:
                return True

            visited.add(node)

            for nei in self.adj[node]:
                if nei not in visited:
                    if helper(nei):
                        return True
            return False

        for node in self.nodes:
            if node not in visited:
                if helper(node):
                    return True
        return False

    def bfs(self, target):
        visited = set()

        for start in self.nodes:
            if start in visited:
                continue

            queue = deque([start])
            visited.add(start)

            while queue:
                node = queue.popleft()

                if node == target:
                    return True

                for nei in self.adj[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)

        return False

    def topo_sort_dfs(self):
        visited = set()
        visiting = set()
        result = []

        def dfs(node):
            if node in visiting:
                return False  # cycle

            if node in visited:
                return True

            visiting.add(node)

            for nei in self.adj[node]:
                if not dfs(nei):
                    return False

            visiting.remove(node)
            visited.add(node)
            result.append(node)
            return True

        for node in self.nodes:
            if node not in visited:
                if not dfs(node):
                    return None  # cycle detected

        return result

    def topo_sort_bfs(self):
        indegree = {node: 0 for node in self.nodes}

        # compute indegrees
        for u in self.adj:
            for v in self.adj[u]:
                indegree[v] += 1

        # start with nodes that have 0 indegree
        queue = deque()
        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)

        result = []

        while queue:
            node = queue.popleft()
            result.append(node)

            for nei in self.adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        # if not all nodes processed → cycle
        if len(result) != len(self.nodes):
            return None

        return result

#Time-taken: 40 minutes