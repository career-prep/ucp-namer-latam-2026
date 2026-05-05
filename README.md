# Graph Algorithms & Data Structures – Practice Assignment
#Readme created using AI!
This repository contains Java implementations of core data structures and graph algorithm problems, split into two parts.

---

# Part 1 – Data Structure Implementations

## Question 1 – Graph (Adjacency Set)

**File:** `DataStructureImplementationPart1/question1AdjSet.java`

Implemented a directed graph using an adjacency set (`Map<Integer, Set<Integer>>`) with the following algorithms:

| Method | Description |
|---|---|
| `createGraph(length, edges)` | Builds the graph from an edge list |
| `bfsSearch(target, graph)` | BFS traversal to locate a target node |
| `dfsSearch(target, graph)` | DFS traversal to locate a target node |
| `topologicalSortKhans(graph)` | Topological sort via Khan's algorithm (in-degree + BFS) |
| `topologicalSortDFS(graph)` | Topological sort via DFS + stack |

**Time Complexity:** O(N + M) for all operations — N = nodes, M = edges  
**Space Complexity:** O(N) visited set, O(N) recursion/queue

---

## Question 2 – Min Heap

**File:** `DataStructureImplementationPart1/Heap.java`

Implemented a min-heap backed by an `ArrayList<Integer>`.

| Method | Time Complexity |
|---|---|
| `top()` | O(1) |
| `insert(x)` | O(log n) |
| `remove()` | O(log n) |

**Space Complexity:** O(n)

---

## Question 3 – Max Priority Queue

**File:** `DataStructureImplementationPart1/PriorityQueue.java`

Implemented a max-priority queue using a custom `Pair(String value, int priority)` stored in an `ArrayList`. Maintains max-heap order by priority.

| Method | Time Complexity |
|---|---|
| `top()` | O(1) |
| `insert(x, weight)` | O(log n) |
| `remove()` | O(log n) |

**Space Complexity:** O(n)

---

## Question 4 – Singly Linked List

Implemented a singly linked list with `Node(int data, Node next)`.

| Method | Description |
|---|---|
| `insertAtFront(head, val)` | Insert at the front |
| `insertAtBack(head, val)` | Insert at the back |
| `insertAfter(head, val, loc)` | Insert after a given node |
| `insertBefore(head, val, loc)` | Insert before a given node |
| `deleteFront(head)` | Remove first node |
| `deleteBack(head)` | Remove last node |
| `deleteNode(head, loc)` | Remove a specific node |
| `length(head)` | Return number of nodes |
| `reverseIterative(head)` | Reverse list iteratively — O(n) |
| `reverseRecursive(head)` | Reverse list recursively — O(n) |

---

## Question 5 – Doubly Linked List

Implemented a doubly linked list with `Node(int data, Node next, Node prev)`.

Same operations as the singly linked list plus `tail`-aware variants for back insertions/deletions.

---

## Question 6 – Binary Search Tree

Implemented a BST with the following operations:

| Method | Avg Complexity | Worst Case |
|---|---|---|
| `min()` | O(h) | O(n) |
| `max()` | O(h) | O(n) |
| `contains(val)` | O(h) | O(n) |
| `insert(val)` | O(h) | O(n) |
| `delete(val)` | O(h) | O(n) |

---

## Question 7 – Queue (Linked List)

Implemented a queue using a linked list structure.

| Method | Complexity |
|---|---|
| `peek()` | O(1) |
| `enqueue(x)` | O(1) |
| `dequeue()` | O(1) |
| `isEmpty()` | O(1) |

---

## Question 8 – Stack (Linked List)

Implemented a stack using a linked node structure.

| Method | Complexity |
|---|---|
| `top()` | O(1) |
| `push(x)` | O(1) |
| `pop()` | O(1) |
| `isEmpty()` | O(1) |

---

## Question 9 – Deque (Doubly Linked List)

Implemented a double-ended queue using a doubly linked list.

| Method | Complexity |
|---|---|
| `front()` / `back()` | O(1) |
| `pushFront(x)` / `pushBack(x)` | O(1) |
| `popFront()` / `popBack()` | O(1) |
| `isEmpty()` | O(1) |

---

# Part 2 – Algorithm Problems

## Question 1 (P2) – Number of Islands

**File:** `Part2Questions/q4_NumberOfIslands.java`

**Problem:** Given a 2D grid of `0`s and `1`s, count the number of distinct islands (connected groups of `1`s).

**Approach:** DFS flood-fill. For each unvisited land cell, run DFS to mark all connected cells as `0`, then increment the island counter.

**DSA:** Graph + DFS  
**Time Complexity:** O(m × n)  
**Space Complexity:** O(m × n) — recursion stack worst case  
**Time Spent:** ~20 minutes

---

## Question 2 (P2) – First K Binary Numbers

**File:** `Part2Questions/q5_FirstKBinaryNumbers.java`

**Problem:** Generate the first `n` binary numbers as strings (e.g., `"1"`, `"10"`, `"11"`, `"100"`, …).

**Approach:** BFS-style queue. Start with `"1"`; for each dequeued string, enqueue it appended with `"0"` and `"1"`. Repeat until `n` numbers are collected.

**DSA:** Queue  
**Time Complexity:** O(n)  
**Space Complexity:** O(n)

---

## Question 3 (P2) – Road Networks

**File:** `Part2Questions/Q6_RoadNetworks.java`

**Problem:** Given a list of towns and bidirectional roads, count the number of disconnected road networks.

**Approach:** Build an undirected adjacency list. Run BFS from each unvisited town with connections; each BFS run represents one connected component.

**DSA:** Graph + BFS (connected components)  
**Time Complexity:** O(N + M) — N = towns, M = roads  
**Space Complexity:** O(N + M)  
**Time Spent:** ~30 minutes

---

## Question 4 (P2) – Reverse Words

**File:** `Part2Questions/q7_ReverseWords.java`

**Problem:** Reverse the order of words in a string, correctly handling multiple spaces and edge cases.

**Approach:** Two-pointer traversal from end to start. Track word boundaries and build result via `StringBuilder`. Handles null input and consecutive spaces.

**DSA:** Two Pointers + StringBuilder  
**Time Complexity:** O(n)  
**Space Complexity:** O(n)  
**Time Spent:** ~35 minutes

---

## Question 5 (P2) – Alternating Path

**File:** `Part2Questions/q8_AlternatingPath.java`

**Problem:** Find the shortest path between two nodes in a colored-edge graph where edges must alternate colors.

**Approach:** BFS with state `(node, lastColorUsed, distance)`. Only traverse edges whose color differs from the last used edge. Visited set uses key `"node-lastColor"` to allow revisiting nodes via different-colored paths.

**DSA:** Graph + BFS (state-space search)  
**Time Complexity:** O(N + M)  
**Space Complexity:** O(N + M)

---

## Question 6 (P2) – Merge K Sorted Arrays

**File:** `Part2Questions/q9_MergeKSortedArrays.java`

**Problem:** Merge `k` sorted integer arrays into a single sorted array.

**Approach:** Min-heap solution. Insert the first element of each array as `Node(value, arrayIdx, elemIdx)`. Repeatedly poll the minimum, append to result, and push the next element from the same source array.

**DSA:** Min-Heap (Priority Queue)  
**Time Complexity:** O(n log k) — n = total elements, k = number of arrays  
**Space Complexity:** O(n + k)  
**Time Spent:** ~40 minutes

---

## Question 7 (P2) – Prerequisite Courses

**File:** `Part2Questions/q10_PrerequisiteCourses.java`

**Problem:** Given courses and their prerequisites, return a valid course ordering. Return empty list if a cycle makes it impossible.

**Approach:** Topological sort via Khan's algorithm. Build directed graph (prereq → course), track in-degrees, seed queue with courses having 0 prerequisites, process and decrement dependents. Cycle detected if result size ≠ course count.

**DSA:** Graph + BFS + Topological Sort (Khan's)  
**Time Complexity:** O(N + M) — N = courses, M = prerequisite edges  
**Space Complexity:** O(N + M)  
**Time Spent:** ~35 minutes

---

## Question 8 (P2) – Vacation Destination

**File:** `Part2Questions/q11_VacationDestination.java`

**Problem:** Given weighted flight routes, count how many cities are reachable from an origin within a time limit, with a 1-hour stopover added at each non-origin city.

**Approach:** Dijkstra's algorithm with a min-heap on total time. State = `(city, totalTime)`. Stopover cost of +1 hour applied when departing a non-origin city. Count all cities where shortest time ≤ timeLimit (excluding origin).

**DSA:** Graph + Dijkstra's Algorithm + Min-Heap  
**Time Complexity:** O(M log N) — M = routes, N = cities  
**Space Complexity:** O(N + M)


