# Homework 3

## Question 1: Graph Algorithms Using Adjacency List/Set Representation
- **Problem Description:** Implementation of an adjacency list from edges, plus BFS, DFS, and two versions of Topological Sort.
- **Problem Type:** Graph Representation & Traversal
- **Approach:** Map of sets for representation; standard iterative BFS (Queue) and recursive DFS (Stack/Post-order).
- **Time Complexity:** O(V + E)
- **Space Complexity:** O(V + E)
- **Time Taken:** 1 hr 40 min

## Question 2: Build a Heap
- **Problem Description:** Implementation of a Min-Heap class using an underlying array.
- **Problem Type:** Data Structure (Priority Queue)
- **Approach:** Complete binary tree logic with sift-up and sift-down operations.
- **Time Complexity:** O(log n) for insert/remove, O(1) for top.
- **Space Complexity:** O(n)
- **Time Taken:** 40 min

## Question 3: Build a Priority Queue
- **Problem Description:** Implementation of a Max-Heap that stores string elements with integer weights.
- **Problem Type:** Data Structure (Priority Queue)
- **Approach:** Max-heap sift operations comparing integer priorities.
- **Time Complexity:** O(log n) for insert/remove, O(1) for top.
- **Space Complexity:** O(n)
- **Time Taken:** 20 min

## Question 4: NumberOfIslands
- **Problem Description:** Counting contiguous 1s in a 2D binary matrix.
- **Problem Type:** Graph (Grid Traversal)
- **Approach:** DFS traversal to "sink" islands and mark visited nodes.
- **Time Complexity:** O(M * N)
- **Space Complexity:** O(M * N)
- **Time Taken:** 32 min

## Question 5: FirstKBinaryNumbers
- **Problem Description:** Return an array of the first k binary numbers represented as strings.
- **Problem Type:** Linear Data Structure (Queue)
- **Approach:** BFS generation using a queue to append "0" and "1" to existing strings.
- **Time Complexity:** O(k)
- **Space Complexity:** O(k)
- **Time Taken:** 35 min

## Question 6: RoadNetworks
- **Problem Description:** Count the number of disconnected road networks (connected components) in a state.
- **Problem Type:** Graph (Connected Components)
- **Approach:** Iterative DFS traversal from every unvisited town.
- **Time Complexity:** O(V + E)
- **Space Complexity:** O(V + E)
- **Time Taken:** 40 min

## Question 7: ReverseWords
- **Problem Description:** Reverse the order of space-separated words in a string.
- **Problem Type:** String Manipulation
- **Approach:** Splitting the string by whitespace, reversing the list, and joining.
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Time Taken:** 40 min

## Question 8: AlternatingPath
- **Problem Description:** Find the shortest path between two nodes where edges alternate between blue and red.
- **Problem Type:** Graph (Shortest Path)
- **Approach:** BFS tracking both current node and the color used to reach it (state-space search).
- **Time Complexity:** O(V + E)
- **Space Complexity:** O(V + E)
- **Time Taken:** 40 min

## Question 9: MergeKSortedArrays
- **Problem Description:** Merge k sorted arrays into a single sorted array.
- **Problem Type:** Heap (Priority Queue)
- **Approach:** K-way merge using a min-heap to track the smallest element across all arrays.
- **Time Complexity:** O(N log k)
- **Space Complexity:** O(N)
- **Time Taken:** 30 min

## Question 10: PrerequisiteCourses
- **Problem Description:** Find a valid course order given a map of prerequisites.
- **Problem Type:** Graph (Topological Sort)
- **Approach:** Kahn's Algorithm (BFS) using in-degrees to resolve dependencies.
- **Time Complexity:** O(V + E)
- **Space Complexity:** O(V + E)
- **Time Taken:** 40 min

## Question 11: VacationDestinations
- **Problem Description:** Count destinations reachable within travel time k, including stopover penalties.
- **Problem Type:** Graph (Shortest Path)
- **Approach:** Modified BFS that tracks cumulative time and applies a +1 hour penalty for stopovers.
- **Time Complexity:** O(V + E)
- **Space Complexity:** O(V + E)
- **Time Taken:** 40 min