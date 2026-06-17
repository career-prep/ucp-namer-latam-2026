# Homework 3

## Problems Completed

### Q1 - Graph Algorithms (q1_graph_algorithms.py)

**Problem:** Build an adjacency list from edge pairs, then implement DFS search, BFS search, DFS topological sort, and Kahn's algorithm (BFS topological sort).

**Thought Process:**
I started by building an undirected adjacency set using a defaultdict(set) from the edge pairs. From there I implemented four things.

For DFS Search I recursively visit neighbors while tracking visited nodes in a set to avoid going in circles. As soon as the target is found I return True.

For BFS Search I used a deque as a queue and marked nodes as visited before enqueuing them. The first time the target comes out of the queue I return True.

For DFS Topological Sort I used a post-order approach where a node only gets added to the result after all of its descendants are fully processed. Reversing at the end gives the correct order since nodes with no outgoing edges finish first.

For Kahn's Algorithm I counted in-degrees for every node and started the queue with anything that had an in-degree of 0. Each time I processed a node I decremented the in-degree of its neighbors and enqueued any that hit 0.

**Complexity:** O(V+E) time, O(V+E) space for all four.

---

### Q2 - MinHeap (q2_heap.py)

**Problem:** Implement a MinHeap class backed by an array with top(), insert(), and remove().

**Thought Process:**
I used a standard array-based binary heap. The parent of index i lives at (i-1)//2, left child at 2i+1, and right child at 2i+2.

For insert I append to the end and push the value up by swapping it with its parent until the heap property is restored. For remove I swap the root with the last element, pop the last, and push the new root down by swapping it with its smaller child until everything is back in order.

**Complexity:** O(log n) for insert and remove, O(1) for top, O(n) space.
**Time Spent:** ~30 mins

---

### Q3 - Priority Queue (q3_priority_queue.py)

**Problem:** Implement a PriorityQueue that stores (value, priority) pairs and always removes the highest priority element first.

**Thought Process:**
I reused the MinHeap structure from Q2 and just changed what gets stored. Instead of raw values I store tuples of (priority, value) so Python's tuple comparison automatically orders by priority. The top() method returns arr[0][1] to get the value without the priority tag. Everything else stayed the same.

**Complexity:** O(log n) insert/remove, O(1) top, O(n) space.
**Time Spent:** ~30 mins

---

### Q4 - Number of Islands (q4_Numbers_of_island.py)

**Problem:** Given a binary matrix of '1' (land) and '0' (water), count the number of islands.

**Thought Process:**
Classic DFS flood-fill. I iterate every cell and whenever I hit a '1' I increment the island count and immediately run DFS from that cell to mark the whole connected land mass as '0'. That way I never count the same island twice. The DFS checks all four directions and stops when it goes out of bounds or hits water. Mutating the grid in place means I don't need a separate visited structure.

**Complexity:** O(m x n) time and space.
**Time Spent:** ~30 mins

---

### Q5 - First K Binary Numbers (q5_FirstKBinary.py)

**Problem:** Return the first k binary numbers as strings, starting with "0".

**Thought Process:**
I came up with two approaches here.

The queue approach seeds the result with ["0"] and a queue with "1". Each step I dequeue a value, add it to the result, then enqueue that value with "0" and "1" appended. This works because every binary number is just its parent with a 0 or 1 tacked on, so the queue naturally produces them in order.

The DP approach came after I noticed a pattern: the binary representation of i is just the binary of i//2 with a '0' if i is even or a '1' if i is odd. So I built the array bottom-up using previously computed values.

**Complexity:** O(n) time and space for both.
**Time Spent:** ~20 mins

---

### Q6 - Road Networks (q6_RoadNetworks.py)

**Problem:** Given towns and roads, return the number of disconnected road networks.

**Thought Process:**
This is basically a connected components problem. I built an adjacency list for all towns including isolated ones. Then I iterated through every town and each time I found one that hadn't been visited I incremented the network count and ran DFS to mark that whole component as visited. Each DFS call fully explores one network.

**Complexity:** O(V+E) time, O(V+E) space.

---

### Q7 - Reverse Words (q7_ReverseWords.py)

**Problem:** Reverse the order of words in a string.

**Thought Process:**
I used a min-heap with negative indices. I split the string into words and pushed each one as (-index, word). Popping from the heap gives words from the highest index down to the lowest, which is exactly reverse order. I joined the result with spaces at the end. A simple words[::-1] would also work but the heap approach ties into the week's theme.

**Complexity:** O(n log n) time, O(n) space.
**Time Spent:** ~15 mins

---

### Q8 - Alternating Path (q8_alternatingPath.py)

**Problem:** In a directed graph with red and blue edges, find the shortest path from origin to destination where edge colors strictly alternate. Return -1 if no such path exists.

**Thought Process:**
I used BFS for shortest path but the tricky part is that the state can't just be the current node. It also has to include the color of the last edge taken, otherwise you can't know which colors are valid next. So I tracked visited as a set of (node, last_color) pairs.

BFS starts with (origin, None, 0) meaning no color restriction on the first move. At each step I only expand to neighbors whose edge color is different from last_color. The first time the destination comes out of the queue is the shortest valid path.

**Complexity:** O(V+E) time and space.
**Note:** Honestly one of the hardest problems in the set. Had to get some help from AI to work through the state tracking piece.

---

### Q9 - Merge K Sorted Arrays (q9_MergeK.py)

**Problem:** Given k sorted arrays, merge them into a single sorted array.

**Thought Process:**
The key idea is to always pick the global minimum across all arrays efficiently. I seeded a min-heap with the first element from each non-empty array stored as (value, array_index, element_index). Each time I pop the minimum I add it to the result and then push the next element from that same array if one exists. That way only k elements ever live in the heap at once instead of loading everything upfront.

**Complexity:** O(n log k) time, O(k) space.
**Time Spent:** ~30 mins

---

### Q10 - Prerequisite Courses (q10_prerequisite.py)

**Problem:** Given courses and a prerequisite map, return a valid order to take the courses (topological sort).

**Thought Process:**
I used Kahn's algorithm. The prerequisite map is given as course -> list of prereqs which is the reverse of what I need, so I flipped it to prereq -> list of courses that depend on it. Then I computed in-degrees (how many prereqs each course still has) and seeded the BFS queue with anything that has 0 prereqs. Each time a course is processed I decrement the in-degree of everything that depends on it and enqueue anything that drops to 0.

**Complexity:** O(V+E) time, O(V+E) space.
**Time Spent:** ~40 mins

---

### Q11 - Vacation Destinations (q11_vacationDes.py)

**Problem:** Given an origin, travel pairs with times, and a max time k, count reachable destinations within k hours where stopovers add 1 extra hour.

**Status:** Problem statement is written, solution in progress.

---

## Summary

| | |
|---|---|
| **Completed** | 10 / 11 problems |
| **Total Time** | ~8 hrs |
| **CC** | careerprep@uber.com |
