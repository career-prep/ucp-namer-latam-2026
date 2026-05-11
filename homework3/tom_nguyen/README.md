# Homework 3

## Q1: GraphAlgorithms

**Problem Type:** Graph, BFS, DFS, Topological Sort

**Time Spent:** 35 minutes

**Complexity:**
- Time: O(V + E) - each algorithm visits every node and edge once
- Space: O(V + E) - adjacency set and visited set

## Q2: Heap

**Problem Type:** Heap, Array

**Time Spent:** 20 minutes

**Complexity:**
- Time: O(log n) per insert/remove - bubble up/down through the tree
- Space: O(n) - underlying array

## Q3: PriorityQueue

**Problem Type:** Priority Queue, Heap

**Time Spent:** 10 minutes

**Complexity:**
- Time: O(log n) per insert/remove - same as heap
- Space: O(n) - underlying array of (string, int) pairs

## Q4: NumberOfIslands

**Problem Type:** Graph, DFS

**Time Spent:** 15 minutes

**Complexity:**
- Time: O(m * n) - visits every cell in the grid once
- Space: O(m * n) - recursion stack in the worst case

## Q5: FirstKBinaryNumbers

**Problem Type:** Queue

**Time Spent:** 10 minutes

**Complexity:**
- Time: O(k * log k) - each of the k strings has O(log k) digits
- Space: O(k) - queue and result array

## Q6: RoadNetworks

**Problem Type:** Graph, BFS

**Time Spent:** 20 minutes

**Complexity:**
- Time: O(V + E) - BFS visits every town and road once
- Space: O(V + E) - adjacency list and visited set

## Q7: ReverseWords

**Problem Type:** Stack

**Time Spent:** 8 minutes

**Complexity:**
- Time: O(n) - single pass to push words, single pass to pop
- Space: O(n) - stack holds all words

## Q8: AlternatingPath

**Problem Type:** Graph, BFS

**Time Spent:** 30 minutes

**Complexity:**
- Time: O(V + E) - BFS over (node, last_color) states
- Space: O(V + E) - visited set and queue

## Q9: MergeKSortedArrays

**Problem Type:** Priority Queue (Min Heap)

**Time Spent:** 15 minutes

**Complexity:**
- Time: O(N log k) - N total elements, each heap operation is O(log k)
- Space: O(k) - heap holds one element per array

## Q10: PrerequisiteCourses

**Problem Type:** Graph, Topological Sort

**Time Spent:** 20 minutes

**Complexity:**
- Time: O(V + E) - Kahn's algorithm processes each course and prerequisite once
- Space: O(V + E) - adjacency list and indegree map

## Q11: VacationDestinations

**Problem Type:** Graph, Dijkstra's

**Time Spent:** 25 minutes

**Complexity:**
- Time: O((V + E) log V) - Dijkstra's with a priority queue
- Space: O(V + E) - graph and distance map
