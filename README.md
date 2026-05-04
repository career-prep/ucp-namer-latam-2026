# Homework 3 — Graphs & Data Structure Selection

---

## Question 1: Graph Algorithms Using Adjacency List/Set Representation

**Problem:** Given an array of pairs of values representing edges in an unweighted graph, create the equivalent adjacency list/set representation (a map from element to a list or set of elements). Pairs represent directed edges: (A, B) means there is an edge from A to B. If the pair (B, A) is also provided, then there is an undirected edge between A and B. Implement a basic DFS and BFS that search for a target value and two topological sorts (using each of DFS and Kahn's algorithm).

**Data Structure:** Graph (adjacency map of node → set of neighbors)

**Problem Type:** Graph traversal, Topological Sort

| Algorithm | Time Complexity | Space Complexity |
|---|---|---|
| Build adjacency set | O(E) where E is the number of edges | O(N + E) where N is nodes and E is edges |
| DFS search | O(N + E) where N is nodes and E is edges | O(N) for the visited set and call stack |
| BFS search | O(N + E) where N is nodes and E is edges | O(N) for the visited set and queue |
| Topological sort (DFS) | O(N + E) where N is nodes and E is edges | O(N) for the visited set and result list |
| Topological sort (Kahn's) | O(N + E) where N is nodes and E is edges | O(N) for the dependency count map and queue |

---

## Question 2: Build a Heap

**Problem:** Write a min heap class using an array as the underlying data structure. The class must support `top()` which returns the minimum element, `insert(x)` which adds an integer to the heap in the correct position, and `remove()` which removes the minimum element.

**Data Structure:** Heap (min heap backed by a list)

**Problem Type:** Data structure implementation

| Operation | Time Complexity | Space Complexity |
|---|---|---|
| `top()` | O(1) | O(1) |
| `insert(x)` | O(log N) where N is the number of elements in the heap | O(1) |
| `remove()` | O(log N) where N is the number of elements in the heap | O(1) |
| Overall space | — | O(N) where N is the number of elements stored |

---

## Question 3: Build a Priority Queue

**Problem:** Write a priority queue class using a max heap as the underlying data structure. The class stores pairs of string elements and integer priorities, and must support `top()` which returns the highest priority element, `insert(string x, int weight)` which adds a string with a given priority, and `remove()` which removes the highest priority element.

**Data Structure:** Priority Queue (max heap backed by a list, storing (string, priority) tuples)

**Problem Type:** Data structure implementation

| Operation | Time Complexity | Space Complexity |
|---|---|---|
| `top()` | O(1) | O(1) |
| `insert(x, weight)` | O(log N) where N is the number of elements in the heap | O(1) |
| `remove()` | O(log N) where N is the number of elements in the heap | O(1) |
| Overall space | — | O(N) where N is the number of elements stored |

---

## Question 4: Number of Islands

**Problem:** Given a binary matrix in which 1s represent land and 0s represent water, return the number of islands (contiguous 1s surrounded by 0s or the edge of the matrix).

**Data Structure:** Graph

**Algorithm:** DFS (generic traversal. Neither BFS nor DFS is preferable in Big O so DFS chosen for simplicity)

**Problem Type:** Connected components in a graph

| | Time Complexity | Space Complexity |
|---|---|---|
| | O(N * M) where N is the number of rows and M is the number of columns in the matrix once | O(N * M) where N is the number of rows and M is the number of columns 
---

## Question 5: First K Binary Numbers

**Problem:** Given a number k, return an array of the first k binary numbers represented as strings.

**Data Structure:** Queue

**Problem Type:** BFS level-by-level generation

| | Time Complexity | Space Complexity |
|---|---|---|
| | O(K) where K is the number of binary numbers to generate | O(K) where K is the size of the result array and queue combined |

---

## Question 6: Road Networks

**Problem:** In some states, it is not possible to drive between any two towns because they are not connected to the same road network. Given a list of towns and a list of pairs representing roads between towns, return the number of road networks. A state in which all towns are connected has 1 road network, and a state in which none of the towns are connected has 0 road networks.

**Data Structure:** Graph

**Algorithm:** DFS (generic traversal)

**Problem Type:** Connected components in a graph

| | Time Complexity | Space Complexity |
|---|---|---|
| | O(T + R) where T is the number of towns and R is the number of roads | O(T + R) where T is the number of towns and R is the number of roads |

---

## Question 7: Reverse Words

**Problem:** Given a string, return the string with the order of the space-separated words reversed.

**Data Structure:** Stack

**Problem Type:** Stack-based string manipulation

| | Time Complexity | Space Complexity |
|---|---|---|
| | O(N) where N is the number of characters in the string | O(W) where W is the number of words in the string |

---

## Question 8: Alternating Path

**Problem:** Given an origin and a destination in a directed graph in which edges can be blue or red, determine the length of the shortest path from the origin to the destination in which the edges traversed alternate in color. Return -1 if no such path exists.

**Data Structure:** Graph

**Algorithm:** BFS (BFS guarantees shortest path in unweighted graphs)

**Problem Type:** Shortest path with constraints

| | Time Complexity | Space Complexity |
|---|---|---|
| | O(N + E) where N is the number of nodes and E is the number of edges | O(N + E) where N is the number of nodes and E is the number of edges |

---

## Question 9: Merge K Sorted Arrays

**Problem:** Given an array of k sorted arrays, merge the k arrays into a single sorted array.

**Data Structure:** Min Heap

**Problem Type:** K-way merge using a heap

| | Time Complexity | Space Complexity |
|---|---|---|
| | O(N log K) where N is the total number of elements across all arrays and K is the number of arrays | O(N + K) where N is the size of the result array and K is the heap size |

---

## Question 10: Prerequisite Courses

**Problem:** Given a list of courses that a student needs to take to complete their major and a map of courses to their prerequisites, return a valid order for them to take their courses assuming they only take one course for their major at once.

**Data Structure:** Graph

**Algorithm:** Topological Sort (Kahn's Algorithm — naturally processes zero-dependency courses first, mirroring how a student would plan their schedule)

**Problem Type:** Topological sort

| | Time Complexity | Space Complexity |
|---|---|---|
| | O(C + P) where C is the number of courses and P is the number of prerequisite relationships | O(C + P) where C is the number of courses and P is the number of prerequisite relationships |

---

## Question 11: Vacation Destinations

**Problem:** Given an origin city, a maximum travel time k, and pairs of destinations that can be reached directly from each other with corresponding travel times in hours, return the number of destinations within k hours of the origin. Assume that having a stopover in a city adds an hour of travel time.

**Data Structure:** Graph

**Algorithm:** Dijkstra's Algorithm (weighted shortest path — uses a min heap to always expand the closest unvisited city first)

**Problem Type:** Weighted shortest path

| | Time Complexity | Space Complexity |
|---|---|---|
| | O((C + R) log C) where C is the number of cities and R is the number of routes | O(C + R) where C is the number of cities and R is the number of routes |