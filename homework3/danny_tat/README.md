# ucp-namer-latam-2026

## UCP Career Prep: Homework 3 Submission - Danny Tat

---

## Question 1: Graph Algorithms

- **Problem Type:** Graph
- **Time Spent:** [1 hour 24 mins]
- **Complexity Analysis:**
  - adjacencySet — Time: O(V + E) and Space: O(V + E)
  - bfs — Time: O(V + E) and Space: O(V)
  - dfs — Time: O(V + E) and Space: O(V)
  - topologicalSort — Time: O(V + E) and Space: O(V)
  - topologicalSortDfs — Time: O(V + E) and Space: O(V)

---

## Question 2: Build a Heap

- **Problem Type:** Heap
- **Time Spent:** [40 mins]
- **Complexity Analysis:**
  - top — Time and Space: O(1)
  - insert — Time: O(log n) and Space: O(1)
  - remove — Time: O(log n) and Space: O(1)

---

## Question 3: Build a Priority Queue

- **Problem Type:** Priority Queue
- **Time Spent:** [20 mins]
- **Complexity Analysis:**
  - top — Time and Space: O(1)
  - insert — Time: O(log n) and Space: O(1)
  - remove — Time: O(log n) and Space: O(1)

---

## Question 4: NumberOfIslands

- **Problem Type:** Graph / BFS
- **Time Spent:** [35 mins]
- **Complexity Analysis:**
  - Time Complexity: O(m * n) — every cell visited at most once
  - Space Complexity: O(m * n) — visited matrix + queue

---

## Question 5: FirstKBinaryNumbers

- **Problem Type:** Queue / BFS
- **Time Spent:** [20 mins]
- **Complexity Analysis:**
  - Time Complexity: O(k) — exactly k dequeue operations
  - Space Complexity: O(k) — result list and queue hold O(k) strings

---

## Question 6: RoadNetworks

- **Problem Type:** Graph / BFS
- **Time Spent:** [24 mins]
- **Complexity Analysis:**
  - Time Complexity: O(V + E) — each town and road processed at most once
  - Space Complexity: O(V + E) — adjacency map stores all towns and roads

---

## Question 7: ReverseWords

- **Problem Type:** Stack
- **Time Spent:** [10 mins]
- **Complexity Analysis:**
  - Time Complexity: O(n) — n is the length of the input string
  - Space Complexity: O(n) — stack holds all words

---

## Question 8: AlternatingPath

- **Problem Type:** Graph / BFS
- **Time Spent:** [23 mins]
- **Complexity Analysis:**
  - Time Complexity: O(V + E) — at most 2V states, each edge visited at most twice
  - Space Complexity: O(V + E) — graph storage + visited set of (node, color) pairs

---

## Question 9: MergeKSortedArrays

- **Problem Type:** Heap
- **Time Spent:** [20 mins]
- **Complexity Analysis:**
  - Time Complexity: O(n log k) — n total elements, each push/pop costs O(log k)
  - Space Complexity: O(k) — heap never exceeds k entries

---

## Question 10: PrerequisiteCourses

- **Problem Type:** Graph / Topological Sort
- **Time Spent:** [28 mins]
- **Complexity Analysis:**
  - Time Complexity: O(V + E) — V = courses, E = prerequisite relationships
  - Space Complexity: O(V + E) — graph + in-degree map + queue

---

## Question 11: VacationDestinations

- **Problem Type:** Graph / Priority Queue
- **Time Spent:** [32 mins]
- **Complexity Analysis:**
  - Time Complexity: O((V + E) log V) — each edge relaxation may push to the heap
  - Space Complexity: O(V + E) — graph adjacency map + dist hashmap + heap