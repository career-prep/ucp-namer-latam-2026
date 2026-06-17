# Homework 3

## Question 1: Graph Algorithms (q1_GraphAlgorithms.py)

### Time Spent: 1 hour 20 minutes

### Approach
For this question I implemented four core graph algorithms on a direct adjacency set representation. `adacencySet` builds the graph from a list of edge pairs. `bfs` uses an iterative queue to search level by level returning True if the target is reachable. `dfs` uses an iterative stack to search depth-first returning True if the target is reachable. Both topological sort implementations assume a DAG and return nodes in dependency order. Kahn's algoirthm uses in-degree tracking with a BFS queue, while the DFS-based approach uses post-order recording with a reversal at the end.

Functions Implemented:
- `adjacencySet` - O(v + E)
- `bfs` - O(V + E)
- `dfs` - O(V + E)
- `topologicalSort` (Kahn's) - O(V + E)
- `topologicalSortDFS` - O(V + E)

## Question 2: Min Heap (q2_Heap.py)

### Time Spent: 40 minutes

### Approach:
For this question I implemented an array-based min heap. The heap property is maintained by `_heapify_up` after every insert and `_heapify_down` after every remove. `insert` appends to the end then bubbles the element up by comparing it to its parent and swapping if smaller. `remove` swaps the root with the last element, pops the last element, then bubbles the new root down by comparing it with its children and swapping with the smallest. `top` returns `arr[0]` in O(1) since the minimum is always the root.

Methods implemented:

- `top` - O(1)
- `insert` - O(log n)
- `remove` - O(log n)
- `_heapify_up` - O(log n)
- `_heapify_down`- O(log n)

## Question 3: Priority Queue (q3_PriorityQueue.py)

## Time Spent: 20 minutes

### Approach
For this question I implemented an array-based max heap storing `(string, int)` pairs where the int is the priority weight. The structure mirrors the min heap from question 2 with one difference, all comparisons use `[1]` to access the weight field of each tuple and the comparison operator is flipped to `>` so the highest weight bubbles to the root instead of the lowest. `top` returns `arr[0][0]`, the name of the highest priority element.

Methods implemented:
- `top` - O(1)
- `insert` - O(log n)
- `remove` - O(log n)
- `_heapify_up` - O(log n)
- `_heapify_down` - O(log n)

## Question 4: Number of Islands (q4_NumberOfIslands.py)
### Technique: DFS
### Time Spent: 20 minutes

### Approach:
For this question I used DFS to count connected components of land cells in a binary matrix. The outer loop iterates every cell and whenever an univisted land cell (`1`) is found, a new island is counted and DFS is launched from that cell. The DFS marks each visited land cell as `0` in place to avoid revisited, then recursively explores all four neighbors. Since visited cells are marked directly in the matrix no seperate visited set is needed, though the call stack still is O(m * n) space in the worst case.

### Time Complexity: O(m * n)
Each cell in the grid is visited at most once.
### Space Complexity: O(m * n)
In the worst case (all land) the DFS call stack reaches m * n frames deep.

## Question 5: First K Binary Numbers (q5_FirstKBinaryNumbers.py)
### Technique: BFS
### Time Spent: 25 minutes

### Approach:
For this question I used a queue to generate binary numbers in order using BFS. `"0"` is handled as a special case and appended directly. The queue is seeded with `"1"` as the root. At each step the front string is dequeued, added to the result, and two children are enqueued by appending `"0"` and `"1"` to it. Since BFS processes nodes in order, this naturally produces binary numbers in ascending order. The loop stops as soon as the result reaches `"k"` elements.

### Time Complexity: O(k)
Each of the k numbers is enqueued and dequeued exactly once.
### Space Complexity: O(k)
The queue and result array each hold at most k elements.

## Question 6: Road Networks (q6_RoadNetworks.py)
### Technique: DFS
### Time Spent: 40 minutes
### Approach
For this question I used DFS to count connected components in an undirected graph of towns and roads. The graph is built as an undirected adjacency set by adding both directions for each road. The outer loop iterates every town and when an unvisited town is found that has at least one road, a new network is counted and DFS marks all reachable towns as visited. Isolated towns with no roads are not counted they do not form a road network.

### Time Complexity: O(V + E)
Every town and road is visited at most once across all DFS calls.
### Space Complexity: O(V + E)
The adjacency set stores all edges; the visited set stores all towns.

## Question 7: Reverse Words (q7_ReverseWords.py)
### Technique: Stack
### Time Spent: 10 minutes

### Approach:
For this question I used a stack to reverse the order of words in a sentence. Each word from the split string is pushed onto the stack. Then words are popped off one by one, which yields them in reverse order due to LIFO, and joined back together with spaces. The words themselves are unchanged, only their positions in the sentence are reversed.

### Time Complexity: O(n)
The string is split once and each word is pushed and popped once.
### Space Complexity: O(n)
The stack holds all words, proportional to the total length of the string.

## Question 8: Alternating Path (q8_AlternatingPath.py)
### Technique: BFS
### Time Spent: 40 minutes

### Approach:
For this question I used BFS where the state is `(node, last_color_used)` rather than just the node. Two separate adjacency sets are built, one for blue edges and one for red. The queue is seeded with both possible starting colors from the origin. At each step the next edge must be the opposite color of the last one used. Visited tracks `(node, color)` pairs so the same node can be reached twice if arrived at by different colors, since the allowed next edge differs. The first time the destination is dequeued its path length is the shortest alternating path.

### Time Complexity: O(V + E)
Each `(node, color)` state is visited at most once, and there are at most 2V states with E transitions.
### Space Complexity: O(V + E)
The visited set holds at most 2V states; the adjacency sets store all edges.

## Question 9: Merge K Sorted Arrays (q9_MergeKSortedArrays.py)
### Technique: Min Heap
### Time Spent: 40 minutes

### Approach:
For this question I used a min heap to efficiently merge k sorted arrays. The heap is seeded with the first element of each array stored as `(value, array_index, element_index)` so that when an element is poppoed, the next element from the same array can be pushed immediately. At each step the global minimum across all arrays is at the heap root. Popping it and pushing the next element from its source array maintains at most k elements in the heap at any time, keeping each operation at O(log k).

### Time Complexity: O(n log k)
Each of the n total elements is pushed and popped from the heap once, and each heap operation costs log k since the heap holds at most k elements.
### Space Complexity: O(k)
For the heap + O(n) for the result array.

## Question 10: Prerequisite Courses (q10_PrerequisiteCourses.py)
### Technique: Topological Sort BFS
### Time Spent: 25 minutes

### Approach:
For this question I used Kahn's algorithm to produce a valid course ordering given prerequisite constraints. An adjacency set and in-degree map are built from the prereqs dictionary. The queue is seeded with all courses that have no prerequisites. Each course dequeued is added to the result and its depended courses have their in-degree decremented. Any course whose in-degree reaches zero is now fully unlocked and is added to the queue. The result is a valid topological ordering where every prerequisite appears before the course that depends on it.

### Time Complexity: O(V + E)
Building the graph visits all edges; BFS processes each course and each prerequisite relationship once. 
### Space Complexity: O(V + E)
The adjacency set stores all edges; the in-degree map and queue store at most V entries.

## Question 11: Vaction Destinations (q11_VacationDestinations.py)
### Technique: Min heap
### Time Spent: 40 minutes
### Approach: 
For this question I used a min heap to find all cities reachable within k hours. The graph is built as an undirected weighted adjacency set. The heap stores `(travel_time, city)` and is seeded from the origin at time 0. Each time a city is popped, its neighbors are explored and a 1 hour stopover penalty is added to the travel time for every non-origin city passed through. A visited map records the shortest time to reach each city. After BFS completes, the result is the count of visited cities excluding the origin whose arrival time is within k hours.

### Time Complexity: O((V + E) log V)
Each city is pushed to the heap at most once per incoming edge, and each heap operation costs log V.
### Space Complexity: O(V + E)
The adjacency set stores all edges; the visited map and heap hold at most V entries.



