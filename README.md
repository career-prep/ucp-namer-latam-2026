# UCP NAMER LATAM 2026

Solutions to coding problems by **Aung Nanda Oo**.

## Problems Overview

| # | Problem | Technique | Time | Space |
|---|---------|-----------|------|-------|
| 1 | [Trie](#q1-trie) | Trie (insert, search, delete) | O(m) per op | O(total chars) |
| 2 | [Boggle](#q2-boggle) | Trie as a parameter + DFS | O(N·M·8^L) | O(W·L) |
| 3 | [RunningMedian](#q3-runningmedian) | Maintain two heaps | O(n log n) | O(n) |
| 4 | [CatalanNumbers](#q4-catalannumbers) | Dynamic programming (tabulation) | O(n²) | O(n) |
| 5 | [MinCostStairClimbing](#q5-mincoststairclimbing) | Dynamic programming (tabulation) | O(n) | O(n) |
| 6 | [WordBreak](#q6-wordbreak) | Dynamic programming (tabulation) | O(n·W·L) | O(n) |
| 7 | [LargestSquareOf1s](#q7-largestsquareof1s) | Dynamic programming (tabulation) | O(n²) | O(n²) |
| 8 | [CoinChange](#q8-coinchange) | Dynamic programming (tabulation) | O(k·C) | O(k) |
| 9 | [AdoptAPet](#q9-adoptapet) | Maintain two queues | O(1) per event | O(n) |

---

## Q1: Trie

**Problem:** Implement a Trie class with `insert`, `isValidWord`, and `remove` methods. Each node has 26 children (one per lowercase letter) and a `validWord` boolean marking end-of-word. `remove` must delete nodes that are no longer part of any word.

**Example:**
```
insert("apple"), insert("app"), insert("apt")
isValidWord("apple") -> True
isValidWord("ap")    -> False
remove("app")
isValidWord("app")   -> False
isValidWord("apple") -> True  (shared prefix nodes not deleted)
```

**Approach:** Traverse character by character, creating nodes as needed. `isValidWord` traverses and checks the `validWord` flag. `remove` uses a recursive helper: after unwinding the recursion, it nulls a child pointer when the child has no remaining children and is not a valid word end itself.

**Complexity:** O(m) time per operation where m is word length; O(total characters) space

---

## Q2: Boggle

**Problem:** Given a Boggle board and a dictionary of valid words (minimum 3 characters), return all valid words that can be formed from non-overlapping adjacent (including diagonal) letters.

**Example:**
```
Board (3×3):
A D E
R C P
L A Y

Dictionary: Ace, Ape, Cape, Clap, Clay, ...
Output: Ace, Race, Pace, Lace, Pay, Lay, Clay, Ray, Lap, Rap, Clap, Ape, Cape, Yap
```

**Approach:** Build a trie from the dictionary. DFS from each board cell, walking the trie simultaneously so that any branch not matching a trie prefix is pruned immediately. Track visited cells per path and backtrack. Collect words when a node's `word` field is set.

**Complexity:** O(N·M·8^L) worst-case where N·M is board size and L is max word length; trie pruning cuts the practical search dramatically. O(W·L) space for the trie.

---

## Q3: RunningMedian

**Problem:** Given a stream of numbers received one at a time, return an array of medians after each new number is received.

**Example:**
```
Input:  [1, 11, 4, 15, 12]
Output: [1, 6.0, 4, 7.5, 11]
```

**Approach:** Maintain a max-heap `lo` for the lower half and a min-heap `hi` for the upper half. After each insertion, rebalance so sizes differ by at most 1 and `lo`'s max ≤ `hi`'s min. Python's `heapq` is a min-heap; negate values to simulate a max-heap for `lo`. The median is either `-lo[0]` (odd count) or the average of both tops (even count).

**Complexity:** O(n log n) time; O(n) space

---

## Q4: CatalanNumbers

**Problem:** Given a non-negative integer n, return the Catalan numbers C(0) through C(n).

**Example:**
```
Input: 5
Output: [1, 1, 2, 5, 14, 42]
```

**Approach:** Use the recurrence C(0) = 1, C(n) = Σ C(i)·C(n−1−i) for i in 0..n−1. Build the table bottom-up from C(0) to C(n). This avoids large factorial arithmetic and naturally gives all values 0..n.

**Complexity:** O(n²) time; O(n) space

---

## Q5: MinCostStairClimbing

**Problem:** Each stair has a toll paid only when stepped on. You can climb 1 or 2 stairs at a time, starting from either stair 0 or stair 1. You exit after passing the last stair (can stop on stair n-1 or n-2). Return the minimum total toll.

**Example:**
```
Input: [4, 1, 6, 3, 5, 8]  -> 9  (step on stairs 1, 3, 4: 1+3+5)
Input: [11, 8, 3, 4, 9, 13, 10] -> 25 (step on stairs 1, 3, 5: 8+4+13)
```

**Approach:** `dp[i] = cost[i] + min(dp[i-1], dp[i-2])` with base cases `dp[0] = cost[0]` and `dp[1] = cost[1]`. The answer is `min(dp[n-1], dp[n-2])` since either of the last two stairs can be the final step.

**Complexity:** O(n) time; O(n) space

---

## Q6: WordBreak

**Problem:** Given a string without spaces and a dictionary, determine whether the string can be segmented into a sequence of valid dictionary words.

**Example:**
```
Dictionary: Elf, Go, Golf, Man, Manatee, Not, Note, Pig, Quip, Tee, Teen
"mangolf"       -> True  ("man" + "golf")
"manateenotelf" -> True  ("manatee" + "not" + "elf")
"quipig"        -> False
```

**Approach:** `dp[i] = True` if `s[:i]` can be broken into valid words. `dp[0] = True`. For each position i, check every dictionary word: if `dp[i - len(w)]` is True and `s[i-len(w):i]` equals the word, set `dp[i] = True`. Matching is case-insensitive.

**Complexity:** O(n·W·L) time where n = string length, W = dictionary size, L = max word length; O(n) space

---

## Q7: LargestSquareOf1s

**Problem:** Given a square matrix of 0s and 1s, return the side length of the largest square consisting only of 1s.

**Example:**
```
Input (4×4):         Input (5×5):
0 1 0 1              0 1 0 1 1
0 0 1 1              0 0 1 1 1
0 1 1 1              1 1 1 1 1
0 0 1 1              1 1 1 1 1
Output: 2            0 1 1 0 0
                     Output: 3
```

**Approach:** `dp[i][j]` = side length of largest all-1s square with bottom-right corner at (i, j). If `matrix[i][j] == 1`: `dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1`. Track the global maximum.

**Complexity:** O(n²) time; O(n²) space

---

## Q8: CoinChange

**Problem:** Given a list of coin denominations and a target sum k, return the number of ways to make change for k.

**Example:**
```
Coins: [2, 5, 10]
Sum=20 -> 6  (10×2; 4×5; 2×10; 5×2+2×5; 5×2+1×10; 2×5+1×10)
Sum=15 -> 3  (5×2+1×5; 1×5+1×10; 3×5)
```

**Approach:** Classic unbounded knapsack — `dp[j]` = number of ways to reach amount j. `dp[0] = 1`. For each coin, iterate amounts from the coin value to k and accumulate: `dp[j] += dp[j - coin]`. Outer loop over coins (not amounts) ensures combinations are counted, not permutations.

**Complexity:** O(k·C) time where C = number of coin types; O(k) space

---

## Q9: AdoptAPet

**Problem:** An animal shelter assigns pets on a first-in-first-out basis per species. Adopters choose a species; if unavailable, they get the other species. Process a sequence of arrivals (new animals) and adopters, printing the name and species of each adopted pet.

**Example:**
```
Initial: Sadie(dog,4d), Woof(cat,7d), Chirpy(dog,2d), Lola(dog,1d)
Bob wants dog  -> Sadie, dog
Floofy cat arrives
Sally wants cat -> Woof, cat
Ji wants cat    -> Floofy, cat
Ali wants cat   -> Chirpy, dog  (no cats left, fallback to dog)
```

**Approach:** Maintain two deques — one for dogs, one for cats — ordered by time in shelter (longest-waiting at front). Initial animals are sorted by days descending before enqueuing. New arrivals are appended to the back. On adoption, dequeue from the preferred species' deque; if empty, dequeue from the other.

**Complexity:** O(n log n) for initial sort; O(1) per adopt/add event; O(n) space

---

## How to Run

```bash
python aungnanda_oo/q1_Trie.py
python aungnanda_oo/q2_Boggle.py
python aungnanda_oo/q3_RunningMedian.py
python aungnanda_oo/q4_CatalanNumbers.py
python aungnanda_oo/q5_MinCostStairClimbing.py
python aungnanda_oo/q6_WordBreak.py
python aungnanda_oo/q7_LargestSquareOf1s.py
python aungnanda_oo/q8_CoinChange.py
python aungnanda_oo/q9_AdoptAPet.py
```
