# Homework 3

## Problems Completed

---

### Q1 — Graph Algorithms (`q1_graph_algorithms.py`)

**Problem:** Build an adjacency list from edge pairs, then implement DFS search, BFS search, DFS topological sort, and Kahn's algorithm (BFS topological sort).

**Thought Process:**
- Started by building an undirected adjacency set using a `defaultdict(set)` from edge pairs.
- **DFS Search:** Recursively visit neighbors, tracking visited nodes in a set to avoid cycles. Return `True` as soon as the target is found.
- **BFS Search:** Use a `deque` as a queue. Mark nodes visited before enqueuing to avoid revisiting. Return `True` when the target is dequeued.
- **DFS Topological Sort:** Post-order DFS — append a node to the result only after all its descendants are processed, then reverse. Works because nodes with no outgoing edges finish first.
- **Kahn's Algorithm:** Count in-degrees for all nodes. Enqueue nodes with in-degree 0 (no prerequisites). Process each node, decrement neighbor in-degrees, and enqueue those that reach 0.

**Complexity:** O(V+E) time, O(V+E) space for all four implementations.

---

### Q2 — MinHeap (`q2_heap.py`)

**Problem:** Implement a `MinHeap` class backed by an array with `top()`, `insert()`, and `remove()`.

**Thought Process:**
- Used a standard array-based binary heap where the parent of index `i` is at `(i-1)//2`, left child at `2i+1`, right child at `2i+2`.
- **Insert:** Append to the end, then `push_up` — swap with parent while smaller than parent.
- **Remove:** Replace root with last element, pop the last, then `push_down` — swap with the smaller child while larger than either child.
- Both operations maintain the heap invariant in O(log n) time.

**Complexity:** O(log n) insert/remove, O(1) top — O(n) space.
**Time Spent:** ~30 mins

---

### Q3 — Priority Queue (`q3_priority_queue.py`)

**Problem:** Implement a `PriorityQueue` that stores `(value, priority)` pairs and removes elements in priority order.

**Thought Process:**
- Reused the MinHeap structure from Q2. The key insight: store tuples of `(priority, value)` so Python's tuple comparison naturally orders by priority first.
- `insert(val, priority)` pushes `(priority, val)` and calls `push_up`.
- `top()` returns `arr[0][1]` (the value, not the priority).
- `remove()` is identical to MinHeap's remove since the heap logic is the same.

**Complexity:** O(log n) insert/remove, O(1) top — O(n) space.
**Time Spent:** ~30 mins

---

### Q4 — Number of Islands (`q4_Numbers_of_island.py`)

**Problem:** Given a binary matrix of `'1'` (land) and `'0'` (water), count the number of islands (connected groups of `'1'`s).

**Thought Process:**
- Classic DFS flood-fill approach. Iterate every cell in the grid. When a `'1'` is found, increment the island counter and immediately DFS to mark the entire connected land mass as `'0'` (visited).
- DFS moves in 4 directions (up, down, left, right). Base cases: out-of-bounds or cell is already `'0'`.
- Mutating the grid in place avoids a separate visited set.

**Complexity:** O(m×n) time and space.
**Time Spent:** ~30 mins

---

### Q5 — First K Binary Numbers (`q5_FirstKBinary.py`)

**Problem:** Return the first `k` binary numbers as strings, starting with `"0"`.

**Thought Process (Two approaches):**

**Queue approach:** Start the result with `["0"]`. Seed a queue with `"1"`. Each iteration, dequeue a value, append it to results, then enqueue `val + "0"` and `val + "1"`. This naturally produces binary numbers in order because each number's children are just itself with a 0 or 1 appended.

**DP approach (bonus):** Noticed a pattern — the binary representation of `i` is the binary of `i//2` with a `'0'` or `'1'` appended depending on whether `i` is even or odd. Built the result array bottom-up.

**Complexity:** O(n) time and space for both.
**Time Spent:** ~20 mins

---

### Q6 — Road Networks (`q6_RoadNetworks.py`)

**Problem:** Given towns and roads, return the number of disconnected road networks (connected components).

**Thought Process:**
- Modeled as a connected-components problem on an undirected graph.
- Built an adjacency list for all towns (including isolated ones with empty lists).
- Iterated through every town — if unvisited, increment `networks` and DFS to mark the entire component as visited.
- Each DFS call covers exactly one connected component.

**Complexity:** O(V+E) time, O(V+E) space.

---

### Q7 — Reverse Words (`q7_ReverseWords.py`)

**Problem:** Reverse the order of words in a string.

**Thought Process:**
- Used a min-heap with negative indices. Split the string into words and push each as `(-index, word)`.
- Popping from the heap yields words from highest index to lowest, which is reverse order.
- Joined the result with spaces.
- Note: using a heap here is a creative but unconventional approach — a direct `words[::-1]` would be simpler, but the heap demonstrates heap usage.

**Complexity:** O(n log n) time, O(n) space.
**Time Spent:** ~15 mins

---

### Q8 — Alternating Path (`q8_alternatingPath.py`)

**Problem:** In a directed graph with red/blue edges, find the shortest path from origin to destination where edge colors strictly alternate. Return -1 if none exists.

**Thought Process:**
- Standard BFS for shortest path, but the state must track not just the current node but also the color of the last edge taken — so visited is a set of `(node, last_color)` pairs.
- Start BFS with `(origin, None, 0)` — no color constraint on the first step.
- At each node, only expand neighbors whose edge color differs from `last_color`.
- First time destination is dequeued is the shortest valid path.

**Complexity:** O(V+E) time and space.
**Note:** One of the toughest problems in this set — required AI assistance.

---

### Q9 — Merge K Sorted Arrays (`q9_MergeK.py`)

**Problem:** Given `k` sorted arrays, merge them into a single sorted array.

**Thought Process:**
- Used a min-heap for efficient selection of the global minimum at each step.
- Initialized the heap with the first element of each non-empty array as `(value, array_index, element_index)`.
- Each iteration: pop the minimum, add it to the result, then push the next element from the same array (if any). The tuple includes array and element index so we can find the next element in O(1).
- This avoids loading all elements into memory at once — only k elements live in the heap at any time.

**Complexity:** O(n log k) time, O(k) space (heap size).
**Time Spent:** ~30 mins

---

### Q10 — Prerequisite Courses (`q10_prerequisite.py`)

**Problem:** Given courses and a prerequisite map, return a valid course order (topological sort).

**Thought Process:**
- Applied Kahn's algorithm (BFS-based topological sort).
- The prerequisite map is inverted — keys are courses, values are their prerequisites. Rebuilt it as `graph[prereq] → [course]` so edges point forward (prerequisite → dependent).
- Computed in-degrees: how many prerequisites each course has.
- Seeded the BFS queue with all courses that have 0 prerequisites.
- Each time a course is "taken" (dequeued), decrement the in-degree of all dependent courses. Enqueue any that drop to 0.

**Complexity:** O(V+E) time, O(V+E) space.
**Time Spent:** ~40 mins

---

### Q11 — Vacation Destinations (`q11_vacationDes.py`)

**Problem:** Given an origin, travel pairs with times, and a max time `k`, count reachable destinations within `k` hours (stopovers add 1 hour).

**Status:** Problem statement present — solution in progress.

---

## Summary

| | |
|---|---|
| **Completed** | 10 / 11 problems |
| **Total Time** | ~8 hrs |
| **CC** | careerprep@uber.com |
