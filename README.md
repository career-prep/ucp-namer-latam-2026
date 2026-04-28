# UCP NAMER LATAM 2026

Solutions to coding problems by **Aung Nanda Oo**.

## Problems Overview

| # | Problem | Technique | Time | Space |
|---|---------|-----------|------|-------|
| 1 | [GraphAlgorithms](#q1-graphalgorithms) | Adjacency Set, BFS, DFS, Topological Sort | O(V + E) | O(V + E) |
| 2 | [Heap](#q2-heap) | Array-based Min Heap | O(log n) per op | O(n) |
| 3 | [PriorityQueue](#q3-priorityqueue) | Array-based Max Heap | O(log n) per op | O(n) |
| 4 | [NumberOfIslands](#q4-numberofislands) | Graph DFS (Flood Fill) | O(m × n) | O(m × n) |
| 5 | [FirstKBinaryNumbers](#q5-firstkbinarynumbers) | Queue (prefix expansion) | O(k) | O(k) |
| 6 | [RoadNetworks](#q6-roadnetworks) | Graph DFS (Connected Components) | O(V + E) | O(V + E) |
| 7 | [ReverseWords](#q7-reversewords) | Stack | O(n) | O(n) |
| 8 | [AlternatingPath](#q8-alternatingpath) | Graph BFS with state | O(V + E) | O(V + E) |
| 9 | [MergeKSortedArrays](#q9-mergeKsortedarrays) | Min Heap | O(n log k) | O(k) |
| 10 | [PrerequisiteCourses](#q10-prerequisitecourses) | Graph Topological Sort (Kahn's) | O(V + E) | O(V + E) |
| 11 | [VacationDestinations](#q11-vacationdestinations) | Graph Dijkstra's Algorithm | O((V + E) log V) | O(V + E) |

---

## Q1: GraphAlgorithms

**Problem:** Given an array of directed edge pairs, build an adjacency set representation. Implement BFS and DFS that search for a target value, and two topological sorts — one using Kahn's algorithm (BFS-based) and one using DFS.

**Example:**
```
Input edges: [(1,2),(2,3),(1,3),(3,2),(2,0)]
adjacencySet -> {0: {}, 1: {2,3}, 2: {0,3}, 3: {2}}
bfs(target=3)         -> True
dfs(target=9)         -> False
topologicalSort       -> [5, 4, 2, 0, 3, 1]  (Kahn's)
topologicalSortDfs    -> [4, 5, 2, 3, 1, 0]  (DFS)
```

**Approach:** Build the graph by iterating edges, creating empty sets for any node that appears only as a destination. BFS uses a deque and visits all connected components. DFS uses recursion. Kahn's algorithm tracks in-degrees and enqueues zero-in-degree nodes. DFS topological sort appends each node to a stack after all its neighbors are visited, then reverses.

**Complexity:** O(V + E) time, O(V + E) space for all operations

---

## Q2: Heap

**Problem:** Implement a min heap class using an array as the underlying data structure, with top, insert, and remove operations.

**Example:**
```
insert(5), insert(3), insert(8), insert(1), insert(4)
top()    -> 1
remove() -> 1
top()    -> 3
```

**Approach:** Maintain the heap property via sift-up (after insert) and sift-down (after remove). Parent of node at index i is at (i-1)//2; children are at 2i+1 and 2i+2. On remove, swap root with last element, pop the last, then sift-down from root.

**Complexity:** O(1) top, O(log n) insert and remove; O(n) space

---

## Q3: PriorityQueue

**Problem:** Implement a priority queue that stores (string, int) pairs and serves elements in descending order of priority, using a max heap as the underlying data structure.

**Example:**
```
insert("low", 1), insert("high", 10), insert("urgent", 15)
top()    -> "urgent"
remove() -> "urgent"
top()    -> "high"
```

**Approach:** Adapted from the min heap in Q2 — comparisons are flipped so the element with the largest integer priority bubbles to the top. Sift-up swaps when the parent's priority is smaller; sift-down swaps toward the child with the largest priority.

**Complexity:** O(1) top, O(log n) insert and remove; O(n) space

---

## Q4: NumberOfIslands

**Problem:** Given a binary matrix where 1s represent land and 0s represent water, return the number of islands (contiguous groups of 1s surrounded by 0s or the matrix edge).

**Example:**
```
Input:
[[1,0,1,1,1],
 [1,0,1,0,1],
 [1,1,1,0,0],
 [0,0,0,0,0],
 [0,0,0,0,1]]
Output: 3
```

**Approach:** Treat the matrix as a graph where each land cell is a node connected to its four neighbors. Iterate over every cell; when an unvisited land cell is found, run DFS to mark all connected land cells as visited and increment the island count.

**Complexity:** O(m × n) time, O(m × n) space

---

## Q5: FirstKBinaryNumbers

**Problem:** Given a number k, return an array of the first k binary numbers represented as strings.

**Example:**
```
Input: 5   -> ["0", "1", "10", "11", "100"]
Input: 10  -> ["0", "1", "10", "11", "100", "101", "110", "111", "1000", "1001"]
```

**Approach:** Seed the result with "0" and a queue with "1". On each dequeue of string `x`, append `x` to the result then enqueue `x+"0"` and `x+"1"`. This produces binary numbers in order because each number is the prefix of exactly its two children in the binary counting tree.

**Complexity:** O(k) time, O(k) space

---

## Q6: RoadNetworks

**Problem:** Given a list of towns and a list of road pairs, return the number of road networks — connected components with at least two towns. Isolated towns with no roads are not counted.

**Example:**
```
Input: 11 towns, 7 roads
Output: 2  (Gustavus-Glacier Bay and Anchorage-Fairbanks-McCarthy-Copper Center-Homer-Healy)
```

**Approach:** Build an undirected adjacency list. Run DFS from every unvisited town, collecting the component. Increment the network count only when the component contains more than one town.

**Complexity:** O(V + E) time, O(V + E) space

---

## Q7: ReverseWords

**Problem:** Given a string, return the string with the space-separated words in reversed order.

**Example:**
```
Input:  "Uber Career Prep"
Output: "Prep Career Uber"

Input:  "Emma lives in Brooklyn, New York."
Output: "York. New Brooklyn, in lives Emma"
```

**Approach:** Split the string into a list of words (which acts as a stack), then repeatedly pop from the end to build the reversed sequence. Join with spaces.

**Complexity:** O(n) time, O(n) space

---

## Q8: AlternatingPath

**Problem:** Given a directed graph with blue and red edges, find the length of the shortest path from origin to destination where edge colors alternate. Return -1 if no such path exists.

**Example:**
```
Edges: [(A,B,blue),(A,C,red),(B,D,blue),(B,E,blue),(C,B,red),(D,C,blue),(A,D,red),(D,E,red),(E,C,red)]
origin=A, destination=E -> 4  (A→D red, D→C blue, C→B red, B→E blue)
origin=E, destination=D -> -1
```

**Approach:** BFS where each state is `(node, last_color)`. Starting from `(origin, None)`, expand only blue edges if the last was not blue, and only red edges if the last was not red. BFS guarantees the first time destination is reached is the shortest alternating path.

**Complexity:** O(V + E) time, O(V + E) space

---

## Q9: MergeKSortedArrays

**Problem:** Given k sorted arrays, merge them into a single sorted array.

**Example:**
```
Input: 2, [[1,2,3,4,5],[1,3,5,7,9]]
Output: [1,1,2,3,3,4,5,5,7,9]

Input: 3, [[1,4,7,9],[2,6,7,10,11,13,15],[3,8,12,13,16]]
Output: [1,2,3,4,6,7,7,8,9,10,11,12,13,13,15,16]
```

**Approach:** Seed a min-heap with the first element of each array as a tuple `(value, array_index, element_index)`. Repeatedly extract the minimum, append it to the result, and push the next element from the same array if one exists.

**Complexity:** O(n log k) time where n = total elements; O(k) space for the heap

---

## Q10: PrerequisiteCourses

**Problem:** Given a list of courses and a map of courses to their prerequisites, return a valid order to take the courses (one at a time).

**Example:**
```
Input: ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"],
       {"Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"], ...}
Output: ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]
```

**Approach:** Model courses as graph nodes and prerequisites as directed edges. Apply Kahn's topological sort: compute in-degrees, enqueue all zero-in-degree courses, and repeatedly dequeue a course, append it to the result, and decrement the in-degree of its dependents.

**Complexity:** O(V + E) time, O(V + E) space

---

## Q11: VacationDestinations

**Problem:** Given an origin city, a max travel time k, and weighted undirected edges between cities, return the number of destinations reachable within k hours. Each stopover at an intermediate city adds 1 extra hour.

**Example:**
```
Connections: [("Boston","New York",4),("New York","Philadelphia",2),
              ("Boston","Newport",1.5),("Washington, D.C.","Harper's Ferry",1),
              ("Boston","Portland",2.5),("Philadelphia","Washington, D.C.",2.5)]

Origin="New York", k=5 -> 2  (Boston=4h, Philadelphia=2h)
Origin="New York", k=7 -> 4  (+ Newport=6.5h, Washington D.C.=5.5h)
Origin="New York", k=8 -> 6  (+ Portland=7.5h, Harper's Ferry=7.5h)
```

**Approach:** Dijkstra's algorithm on the weighted undirected graph. When relaxing edges from a city that is not the origin, add 1 hour for the stopover at that city before adding the edge's travel time. Count all cities (excluding origin) whose shortest distance is ≤ k.

**Complexity:** O((V + E) log V) time, O(V + E) space

---

## How to Run

```bash
python aungnanda_oo/q1_GraphAlgorithms.py
python aungnanda_oo/q2_Heap.py
python aungnanda_oo/q3_PriorityQueue.py
python aungnanda_oo/q4_NumberOfIslands.py
python aungnanda_oo/q5_FirstKBinaryNumbers.py
python aungnanda_oo/q6_RoadNetworks.py
python aungnanda_oo/q7_ReverseWords.py
python aungnanda_oo/q8_AlternatingPath.py
python aungnanda_oo/q9_MergeKSortedArrays.py
python aungnanda_oo/q10_PrerequisiteCourses.py
python aungnanda_oo/q11_VacationDestinations.py
```
