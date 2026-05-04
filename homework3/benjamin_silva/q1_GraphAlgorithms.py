from collections import defaultdict, deque

def adjacencySet(edges):
    graph = defaultdict(set)
    for i in range(len(edges)):
            graph[edges[i][0]].add(edges[i][1])
            graph[edges[i][1]]
    return graph


def bfs(target, graph):
    visit = set()
    queue = deque(graph.keys())

    while queue:
         curr = queue.popleft()
         if curr == target:
              return True
         if curr in visit:
              continue
         
         visit.add(curr)

         for neighbor in graph[curr]:
              if neighbor not in visit:
                   visit.add(neighbor)
                   queue.append(neighbor)
    return False

def dfs(target, graph):
    visit = set()
    stack = list(graph)

    while stack:
         curr = stack.pop()

         if curr == target:
              return True
         if curr in visit:
              continue
         
         visit.add(curr)

         for neighbor in graph[curr]:
              if neighbor not in visit:
                   visit.add(neighbor)
                   stack.append(neighbor)
    return False


def topologicalSort(graph):
     in_degree = {node: 0 for node in graph}
     for node in graph:
         for neighbor in graph[node]:
              in_degree[neighbor] += 1
     queue = deque([node for node in in_degree if in_degree[node] == 0])
    
     result = []

     while queue:
         curr = queue.popleft()
         result.append(curr)
         for neighbor in graph[curr]:
              in_degree[neighbor] -= 1
              if in_degree[neighbor] == 0:
                   queue.append(neighbor)
     return result if len(result) == len(graph) else []


def topologicalSortDfs(graph):
     visit = set()
     result = []

     def dfs(node):
          if node in visit:
               return 
          visit.add(node)
          for neighbor in graph[node]:
              dfs(neighbor)
          result.append(node)
     
     for node in graph:
          dfs(node)
     return result[::-1]


if __name__ == "__main__":
    edges1 = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
    g1 = adjacencySet(edges1)
    print("=== adjacencySet ===")
    print("Expected: {0: set(), 1: {2,3}, 2: {0,3}, 3: {2}}")
    print("Got:     ", dict(g1))

    print("\n=== BFS ===")
    print("BFS target=0 (expect True):", bfs(0, g1))
    print("BFS target=5 (expect False):", bfs(5, g1))
    print("BFS target=3 (expect True):", bfs(3, g1))

    print("\n=== DFS ===")
    print("DFS target=0 (expect True):", dfs(0, g1))
    print("DFS target=5 (expect False):", dfs(5, g1))
    print("DFS target=3 (expect True):", dfs(3, g1))

    dag_edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
    dag = adjacencySet(dag_edges)
    print("\n=== Topological Sort - Kahn's ===")
    print("DAG edges:", dag_edges)
    print("Valid orderings: 1 must come before 2,3 | 2,3 before 4 | 4 before 5")
    print("Got:", topologicalSort(dag))

    dag_edges2 = [(0, 1), (0, 2), (1, 3), (2, 3)]
    dag2 = adjacencySet(dag_edges2)
    print("Got:", topologicalSort(dag2), "(expected: 0 before 1,2 before 3)")

    print("\n=== Topological Sort - DFS ===")
    print("Got:", topologicalSortDfs(dag))
    print("Got:", topologicalSortDfs(dag2), "(expected: 0 before 1,2 before 3)")

