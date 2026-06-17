# Homework 4
## Problems Completed
### Q1 - Trie (q1_trie.py)
**Problem:** Implement a Trie class with insert, search, and delete.
**Thought Process:** I used nodes with a children map and a boolean that marks complete words. Insert and search walk through the word one character at a time. Delete uses recursion so it can remove unused nodes while returning back up the word path.
**Time Spent:** ~35 mins
**Complexity:** O(k) time for insert/search/remove where k is word length. O(n * k) space for n words.
---
### Q2 - Boggle (q2_boggle.py)
**Problem:** Given a board and dictionary, return all valid dictionary words on the board.
**Thought Process:** I loaded the dictionary into a trie, then started DFS from each board position. Passing the current trie node into DFS lets the search stop early whenever the current path is not a prefix of any valid word.
**Technique:** Trie as a parameter.
**Time Spent:** ~40 mins
**Complexity:** O(m * n * 8^L) time, O(W * L + m * n) space.
---
### Q3 - Running Median (q3_running_median.py)
**Problem:** Return the median after each incoming number in a stream.
**Thought Process:** I used two heaps. The lower half is stored as a max heap using negative numbers, and the upper half is stored as a min heap. After each insert I rebalance so the lower heap is either the same size or one larger.
**Technique:** Maintain two heaps.
**Time Spent:** ~25 mins
**Complexity:** O(n log n) time, O(n) space.
---
### Q4 - Catalan Numbers (q4_catalan_numbers.py)
**Problem:** Return Catalan numbers from 0 through n.
**Thought Process:** Each Catalan number can be built from earlier Catalan numbers, so I used bottom-up tabulation instead of factorials.
**Technique:** Tabulation.
**Time Spent:** ~20 mins
**Complexity:** O(n^2) time, O(n) space.
---
### Q5 - Min Cost Stair Climbing (q5_min_cost_stair_climbing.py)
**Problem:** Return the minimum toll needed to climb past the staircase.
**Thought Process:** The cheapest way to reach each stair depends only on the cheapest ways to reach the previous two stairs. I kept only those two values instead of storing the whole table.
**Technique:** Dynamic programming.
**Time Spent:** ~20 mins
**Complexity:** O(n) time, O(1) space.
---
### Q6 - Word Break (q6_word_break.py)
**Problem:** Determine if a string can be split into valid dictionary words.
**Thought Process:** I used a DP array where dp[i] means the prefix ending at i can be segmented. For each ending position, I check earlier split points.
**Technique:** Dynamic programming.
**Time Spent:** ~25 mins
**Complexity:** O(n^2 * k) time, O(n) space.
---
### Q7 - Largest Square Of 1s (q7_largest_square_of_1s.py)
**Problem:** Return the dimension of the largest all-1 square in a binary matrix.
**Thought Process:** For every 1, I looked at the square sizes immediately above, left, and diagonal-up-left. The current cell can extend only the smallest of those three.
**Technique:** Tabulation.
**Time Spent:** ~25 mins
**Complexity:** O(n^2) time, O(n^2) space.
---
### Q8 - Coin Change (q8_coin_change.py)
**Problem:** Return the number of ways to make a target sum from coin denominations.
**Thought Process:** I used a one-dimensional DP table where dp[amount] counts the ways to make that amount. Iterating coins first avoids counting the same combination in different orders.
**Technique:** Tabulation.
**Time Spent:** ~20 mins
**Complexity:** O(k * c) time, O(k) space.
---
### Q9 - Adopt A Pet (q9_adopt_a_pet.py)
**Problem:** Simulate pet adoptions where adopters choose species but receive the longest-waiting pet of that species, or the other species if needed.
**Thought Process:** I used one queue for cats and one queue for dogs. Initial pets are sorted by days waiting before entering queues. New pets enter the back of their species queue.
**Technique:** Maintain a queue.
**Time Spent:** ~30 mins
**Complexity:** O(n + e) time, O(n + e) space.
---
## Summary
| | |
|---|---|
| **Completed** | 9 / 9 problems |
| **Total Time** | ~4 hrs |
| **CC** | careerprep@uber.com |
