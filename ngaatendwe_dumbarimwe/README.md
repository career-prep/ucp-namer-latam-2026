# Problems Submission
---

## q0_AdjacencyList

**Problem Type:** Graph / DFS / BFS / Topological Sort  

**Description:**  
Implements a graph using an adjacency list and supports DFS search, BFS search, and topological sorting using both DFS and Kahn’s algorithm.

**Time Spent:** 40 minutes  

**Complexity Analysis:**  
- **DFS Search:** O(V + E)  
- **BFS Search:** O(V + E)  
- **Topological Sort (DFS):** O(V + E)  
- **Topological Sort (Kahn’s Algorithm):** O(V + E)  
- **Space Complexity:** O(V + E), where *V* is number of nodes and *E* is number of edges  

---

## q1_Heap

**Problem Type:** Data Structure / Heap  

**Description:**  
Implements a Min Heap using an array with operations for insert, top (peek minimum), and remove (extract minimum).

**Time Spent:** 25 minutes  

**Complexity Analysis:**  
- **Insert:** O(log n)  
- **Remove:** O(log n)  
- **Top:** O(1)  
- **Space Complexity:** O(n), where *n* is number of elements in the heap  

---

## q2_PriorityQueue

**Problem Type:** Data Structure / Heap  

**Description:**  
Implements a priority queue using a min heap where each element is stored as a (priority, value) pair.

**Time Spent:** 20 minutes  

**Complexity Analysis:**  
- **Insert:** O(log n)  
- **Remove:** O(log n)  
- **Top:** O(1)  
- **Space Complexity:** O(n), where *n* is number of elements in the queue  

---

## q3_NumberOfIslands

**Problem Type:** Graph / DFS  

**Description:**  
Counts the number of connected components (islands) in a binary grid using depth-first search.

**Time Spent:** 10 minutes  

**Complexity Analysis:**  
- **Time Complexity:** O(rows × cols)  
- **Space Complexity:** O(rows × cols), worst-case recursion stack  

---

## q4_FirstkBinaryNumbers

**Problem Type:** BFS / Queue  

**Description:**  
Generates the first `k` binary numbers using a BFS-style queue approach.

**Time Spent:** 30 minutes  

**Complexity Analysis:**  
- **Time Complexity:** O(k)  
- **Space Complexity:** O(k), where *k* is the number of binary numbers generated  

---

## q5_RoadNetworks

**Problem Type:** Graph / DFS / Connected Components  

**Description:**  
Finds the number of disconnected road networks (connected components) in an undirected graph.

**Time Spent:** 30 minutes  

**Complexity Analysis:**  
- **Time Complexity:** O(V + E)  
- **Space Complexity:** O(V + E), where *V* is towns and *E* is connections  

---

## q6_ReverseWords

**Problem Type:** String / Two Pointers  

**Description:**  
Reverses the order of words in a string using a two-pointer swapping approach.

**Time Spent:** 15 minutes  

**Complexity Analysis:**  
- **Time Complexity:** O(n)  
- **Space Complexity:** O(n), where *n* is the length of the input string  

---

## q7_AlternatingPath

**Problem Type:** Graph / BFS / State Search  

**Description:**  
Finds the shortest path in a directed graph where edge colors must alternate between steps.

**Time Spent:** 30 minutes  

**Complexity Analysis:**  
- **Time Complexity:** O(V + E)  
- **Space Complexity:** O(V + E), due to storing (node, color) states  

---

## q8_MergeKSortedArrays

**Problem Type:** Heap / Sorting  

**Description:**  
Merges multiple sorted arrays into one sorted array using a heap.

**Time Spent:** 15 minutes  

**Complexity Analysis:**  
- **Time Complexity:** O(N log N), where *N* is total number of elements  
- **Space Complexity:** O(N)  

---

## q9_PrerequisiteCourses

**Problem Type:** Graph / DFS / Cycle Detection / Topological Sort  

**Description:**  
Determines a valid order of courses based on prerequisites using DFS-based topological sorting with cycle detection.

**Time Spent:** 30 minutes  

**Complexity Analysis:**  
- **Time Complexity:** O(V + E)  
- **Space Complexity:** O(V + E), where *V* is courses and *E* is prerequisites  

---

## q10_VacationDestinations

**Problem Type:** Graph / Dijkstra’s Algorithm  

**Description:**  
Finds the number of destinations reachable within a given travel time using Dijkstra’s algorithm with an added stopover cost.

**Time Spent:** 30 minutes  

**Complexity Analysis:**  
- **Time Complexity:** O(E log V)  
- **Space Complexity:** O(V + E), where *V* is cities and *E* is routes  

---