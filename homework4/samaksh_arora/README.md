# Homework 4 - Data Structures & Algorithms

## Q1 - Build a Trie
**Type:** Data Structure Implementation

**Time Complexity:** O(M) for insert, isValidWord, and remove where M is the length of the word

**Space Complexity:** O(1) for operations; O(ALPHABET_SIZE × N × M) for total trie storage where N is number of words

**Time Spent:** >40 minutes

---

## Q2 - Boggle
**Type:** Trie as a parameter (DFS with Backtracking)

**Time Complexity:** O(N × M^8) where N is number of cells on board and M is max path length (8 directions with backtracking)

**Space Complexity:** O(D × L) for trie where D is dictionary size and L is average word length; O(M) for recursion stack

**Time Spent:** >40 minutes

---

## Q3 - Running Median
**Type:** Two Heaps (Max Heap + Min Heap)

**Time Complexity:** O(n log n) where n is the length of the stream (each push/pop is O(log n))

**Space Complexity:** O(n) for the two heaps

**Time Spent:** >40 minutes

---

## Q4 - Catalan Numbers
**Type:** Dynamic Programming (Tabulation)

**Time Complexity:** O(n)

**Space Complexity:** O(n)

**Time Spent:** <40 minutes

---

## Q5 - Min Cost Stair Climbing
**Type:** Dynamic Programming (Tabulation)

**Time Complexity:** O(n) where n is the number of stairs

**Space Complexity:** O(n)

**Time Spent:** 33 minutes

---

## Q6 - Word Break
**Type:** Dynamic Programming (Tabulation) + Trie

**Time Complexity:** O(n^2 × m) where n is the length of string and m is average word length (trie lookup)

**Space Complexity:** O(n) for DP array; O(D × m) for trie where D is dictionary size

**Time Spent:** >40 minutes

---

## Q7 - Largest Square of 1s
**Type:** Dynamic Programming (Tabulation - 2D)

**Time Complexity:** O(m × n) where m and n are the dimensions of the matrix

**Space Complexity:** O(m × n) for the DP table

**Time Spent:** >40 minutes

---

## Q8 - Coin Change
**Type:** Dynamic Programming (Tabulation)

**Time Complexity:** O(n × m) where n is the target sum and m is the number of coins

**Space Complexity:** O(n)

**Time Spent:** >40 minutes

---

## Q9 - Adopt a Pet
**Type:** Queue Data Structure (Multi-Queue)

**Time Complexity:** O(1) for enqueueAnimal; O(n) for adoptAnimal in worst case due to remove() operations

**Space Complexity:** O(n) where n is the number of animals in the shelter

**Time Spent:** >40 minutes

---

