# Problems Submission
---

## q0_Trie

**Problem Type:** Data Structure / Trie  

**Description:**  
Implements a Trie (prefix tree) data structure with insert, validation, and removal operations. Supports efficient string insertion, prefix-based search, and word removal with automatic cleanup of unused nodes.

**Time Spent:** 30 minutes  

**Complexity Analysis:**  
- **Insert:** O(m), where *m* is length of word  
- **isValidWord:** O(m)  
- **Remove:** O(m)  
- **Space Complexity:** O(N*m), where *N* is number of words and *m* is average word length  

---

## q1_Boggle

**Problem Type:** Graph / DFS / Backtracking  

**Description:**  
Finds all valid words in a Boggle board using depth-first search with prefix pruning. Words must be adjacent on the board and have a minimum length of 3 characters.

**Time Spent:** 35 minutes  

**Complexity Analysis:**  
- **Time Complexity:** O(D*L + rows*cols*8^L), where *D* is dictionary size, *L* is max word length  
- **Space Complexity:** O(D*L + rows*cols), for storing words, prefixes, and visited cells  

---

## q2_RunningMedian

**Problem Type:** Data Structure / Heap  

**Description:**  
Computes the median of a stream of numbers as each element is added using two heaps (max-heap for lower half, min-heap for upper half).

**Time Spent:** 30 minutes  

**Complexity Analysis:**  
- **Insert and Median Calculation:** O(log n) per element  
- **Time Complexity:** O(n log n), where *n* is total number of elements  
- **Space Complexity:** O(n)  

---

## q3_CatalanNumbers

**Problem Type:** Dynamic Programming / Combinatorics  

**Description:**  
Generates the first *n* Catalan numbers using the recursive formula: C(n) = sum of C(i) * C(n-1-i) for all i from 0 to n-1.

**Time Spent:** 30 minutes  

**Complexity Analysis:**  
- **Time Complexity:** O(n²)  
- **Space Complexity:** O(n)  

---

## q4_MinCostStairClimbing

**Problem Type:** Dynamic Programming  

**Description:**  
Finds the minimum cost to climb stairs where you can take 1 or 2 steps at a time. Uses space-optimized DP with two variables.

**Time Spent:** 30 minutes  

**Complexity Analysis:**  
- **Time Complexity:** O(n), where *n* is number of stairs  
- **Space Complexity:** O(1), using only two variables for DP state  

---

## q5_WordBreak

**Problem Type:** Dynamic Programming / String  

**Description:**  
Determines if a string can be segmented into dictionary words and returns the segmentation. Uses DP with backtracking to reconstruct the solution.

**Time Spent:** 30 minutes  

**Complexity Analysis:**  
- **Time Complexity:** O(n³), where *n* is length of input string  
- **Space Complexity:** O(n)  

---

## q6_LargestSquareOf1s

**Problem Type:** Dynamic Programming / Matrix  

**Description:**  
Finds the side length of the largest square submatrix containing only 1s using a DP table that tracks square sizes at each position.

**Time Spent:** 30 minutes  

**Complexity Analysis:**  
- **Time Complexity:** O(R × C), where *R* and *C* are rows and columns  
- **Space Complexity:** O(R × C)  

---

## q7_CoinChange

**Problem Type:** Dynamic Programming  

**Description:**  
Finds the minimum number of coins needed to make a given amount using DP. Returns -1 if the amount cannot be made.

**Time Spent:** 35 minutes  

**Complexity Analysis:**  
- **Time Complexity:** O(Coins × Amount)  
- **Space Complexity:** O(Amount)  

---

## q8_AdoptAPet

**Problem Type:** Data Structure / Queue / Deque  

**Description:**  
Manages an animal shelter with separate queues for dogs and cats. Adopts animals based on preference, falling back to other species if the preferred type is unavailable. Prioritizes older animals.

**Time Spent:** 35 minutes  

**Complexity Analysis:**  
- **Initialization:** O(n log n), sorting animals by age  
- **Adopt:** O(1)  
- **Space Complexity:** O(n), where *n* is number of animals  

---
