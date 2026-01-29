# UCP NAMER LATAM 2026

Solutions to coding problems by **Aung Nanda Oo**.

## Problems Overview

| # | Problem | Technique | Time | Space |
|---|---------|-----------|------|-------|
| 1 | [MaxMeanSubArray](#q1-maxmeansubarray) | Sliding Window | O(n) | O(1) |
| 2 | [ReverseVowels](#q2-reversevowels) | Two Pointers | O(n) | O(1) |
| 3 | [ZeroSumSubArrays](#q3-zerosumsubarrays) | Prefix Sum + Hash Map | O(n) | O(n) |
| 4 | [BackspaceStringCompare](#q4-backspacestringcompare) | Stack/Reverse Traversal | O(n) | O(n) |
| 5 | [ShortestSubstring](#q5-shortestsubstring) | Sliding Window | O(n) | O(n) |
| 6 | [MissingInteger](#q6-missinginteger) | Math (Sum Formula) | O(n) | O(1) |
| 7 | [KAnagrams](#q7-kanagrams) | Hash Map (Counter) | O(n) | O(n) |
| 8 | [MergeIntervals](#q8-mergeintervals) | Sorting + Greedy | O(n log n) | O(n) |
| 9 | [DedupArray](#q9-deduparray) | Two Pointers | O(n) | O(1) |

---

## Q1: MaxMeanSubArray

**Problem:** Given an array of integers and an integer k, find the maximum mean of a subarray of size k.

**Example:**
```
Input: [4, 5, -3, 2, 6, 1], k = 2
Output: 4.5
```

**Approach:** Use sliding window to maintain a running sum of k elements. Slide the window and update max mean.

**Complexity:** O(n) time, O(1) space

---

## Q2: ReverseVowels

**Problem:** Given a string, reverse the order of the vowels in the string.

**Example:**
```
Input: "Uber Career Prep"
Output: "eber Ceraer PrUp"
```

**Approach:** Use two pointers from both ends, swap vowels when both pointers point to vowels.

**Complexity:** O(n) time, O(1) space (excluding output string)

---

## Q3: ZeroSumSubArrays

**Problem:** Given an array of integers, count the number of subarrays that sum to zero.

**Example:**
```
Input: [4, 5, 2, -1, -3, -3, 4, 6, -7]
Output: 2
```

**Approach:** Use prefix sum with a hash map. If the same prefix sum appears twice, the subarray between them sums to zero.

**Complexity:** O(n) time, O(n) space

---

## Q4: BackspaceStringCompare

**Problem:** Given two strings with '#' representing backspace, determine if they result in the same text.

**Example:**
```
Input: "abcdef###xyz", "abcw#xyz"
Output: True
```

**Approach:** Process strings from right to left, tracking skip count for backspaces.

**Complexity:** O(n) time, O(n) space

---

## Q5: ShortestSubstring

**Problem:** Given a string and required characters, return the length of the shortest substring containing all required characters.

**Example:**
```
Input: "abracadabra", "abc"
Output: 4 (Substring: "brac")
```

**Approach:** Sliding window with character frequency tracking. Expand right to include all required chars, contract left to minimize length.

**Complexity:** O(n) time, O(n) space

---

## Q6: MissingInteger

**Problem:** Given n and a sorted array of size n-1 containing all integers from 1 to n except one, find the missing integer.

**Example:**
```
Input: [1, 2, 3, 4, 6, 7], n = 7
Output: 5
```

**Approach:** Use the sum formula: `n * (n + 1) / 2 - sum(array)`

**Complexity:** O(n) time, O(1) space

---

## Q7: KAnagrams

**Problem:** Determine if two strings can be made into anagrams by changing at most k characters.

**Example:**
```
Input: "apple", "peach", k = 2
Output: True
```

**Approach:** Count character frequencies and calculate the number of changes needed.

**Complexity:** O(n) time, O(n) space

---

## Q8: MergeIntervals

**Problem:** Given a list of intervals, merge all overlapping intervals.

**Example:**
```
Input: [(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]
Output: [(1, 3), (4, 8), (9, 12)]
```

**Approach:** Sort intervals by start time, then merge consecutive overlapping intervals.

**Complexity:** O(n log n) time, O(n) space

---

## Q9: DedupArray

**Problem:** Given a sorted array, remove duplicates in-place so each element appears only once.

**Example:**
```
Input: [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
Output: [1, 2, 3, 4]
```

**Approach:** Two pointers - one for reading, one for writing. Write only when encountering a new value.

**Complexity:** O(n) time, O(1) space

---

## How to Run

```bash
python aungnanda_oo/q1_MaxMeanSubArray.py
python aungnanda_oo/q2_ReverseVowels.py
# ... and so on
```
