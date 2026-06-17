# Homework 4 - Benjamin Silva

## Question 1: BuildATrie (q1_build_a_trie.py)

**Technique:** Trie data structure implementation

**Time Spent:** 40 minutes

**Approach:** Each TrieNode holds an array of 26 child pointers and a boolean flag. `insert` walks the trie creating nodes as needed and marks the last node. `is_valid_word` walks the trie and checks the flag at the end. `remove` uses a recursive post-order traversal, it unsets the flag then deletes nodes on the way back up if they have no remaining children.

**Time Complexity:** O(L) for insert, search, and remove, where L is the word length
**Space Complexity:** O(N * L), where N is the number of words and L is the average word length

---

## Question 2: Boggle (q2_boggle.py)

**Technique:** Trie + DFS 

**Time Spent:** 40 minutes

**Approach:** For this one I built a trie from the dictionary. For every cell on the board, launch a DFS that follows trie edges while tracking visited cells. When a node with `valid_word = True` is reached (and the word is at least 3 characters), record it. Backtrack by removing cells from the visited set so other paths can reuse them.

**Time Complexity:** O(W * L + R * C * 8^(R * C)): O(W * L) to build the trie (W words, avg length L). O(R * C * 8^(R * C)) for the DFS, one search per cell, branching up to 8 directions each step. 
**Space Complexity:** O(W * L) for the trie, O(R * C) for the visited set.

---

## Question 3: RunningMedian (q3_running_median.py)

**Technique:** Two heaps (max-heap for lowerhalf min-heap for upper half)

**Time Spent:** 40 minutes

**Approach:** For this problem I maintained a max-heap for the lower half of values and a min-heap for the upper half . After each insertion, I restore the ordering like max of lower <= min of upper, then rebalance so the sizes differ by at most 1. The median is the average of both tops when sizes are equal, or the top of the larger heap when odd.

**Time Complexity:** O(n log n)
**Space Complexity:** O(n)

---

## Question 4: CatalanNumbers (q4_catalan_numbers.py)

**Technique:** Tabulation

**Time Spent:** 40 minutes

**Approach:** For this one I built a table of size n + 1 and filled each entry directly using C(n) = (2n)! / ((n + 1)! * n!).

**Time Complexity:** O(n^2), outer loop runs n times, each iteration has inner loops up to 2i steps to compute the factorials.
**Space Complexity:** O(n)

---

## Question 5: MinCostStairClimbing (q5_min_cost_stair_climbing.py)

**Technique:** Tabulation

**Time Spent:** 30 minutes

**Approach:** For this one I built a dp table of size n + 1 where dp[i] is the minimum cost to reach stair i. I seeded `dp[0] = dp[1] = 0` since I can start from either. For each stair, I take the minimum of arriving from one or two steps back, adding that step's cost.

**Time Complexity:** O(n)
**Space Complexity:** O(n)

---

## Question 6: WordBreak (q6_word_break.py)

**Technique:** Tabulation

**Time Spent:** 40 minutes

**Approach:** I built a boolean dp table of size n + 1 where `dp[i]` means the first i characters of s can be segmented into valid dictionary words. I seed `dp[0] = True`. For each position i, I check all split points `j`: if dp[j] is True and s[j:i] is in the word set, I set dp[i] = True

**Time Complexity:** O(n^2 * L), n = string length, L = avg word length for substring checks
**Space Complexity:** O(n)

---

## Question 7: LargestSquareOf1s (q7_largest_square_of_1s.py)

**Technique:** Tabulation

**Time Spent:** 40 minutes

**Approach:** I built a dp table where dp[i][j] is the side length of the largest square of 1s whose bottom-right corner is at `(i, j)`. If matrix[i][j] == 1, I set dp[i][j] = min(top, left, diagonal) + 1, otherwise 0. I seed the first row and column directly. I track the max value seen across the whole table.

**Time Complexity:** O(m * n)
**Space Complexity:** O(m * n)

---

## Question 8: CoinChange (q8_coin_change.py)

**Technique:** Tabulation
 
**Time Spent:** 20 minutes

**Approach:** I built a dp table of size target + 1 where dp[amount] is the number of ways to make that amount. I seed dp[0] = 1. For each coin, I terate from coin to target and add dp[amount - coin] to dp[amount]. I return dp[target]

**Time Complexity:** O(k * n), k = target amount, n = number of coin denominations
**Space Complexity:** O(k)

---

## Question 9: AdoptAPet (q9_adopt_a_pet.py)

**Technique:** Two queues

**Time Spent:** 40 minutes

**Approach:** For this question I maintain seperate FIFO queues for dogs and cats. Populate them from initial_animals, which is already sorted longest-waiting first. For each event, enqueue new animals to the appropriate queue. For adopters, dequeue from their preferred species queue; if it is empty, dequeue from the other species instead.

**Time Complexity:** O(A + E), A = number of initial animals, E = number of events
**Space Complexity:** O(A + E)