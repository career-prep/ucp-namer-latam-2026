# Homework 1 - Solutions

---

## Problems Completed

### ✅ Question 1: MaxMeanSubArray
**File:** [q1_maxmean_subarray.py](q1_maxmean_subarray.py)

**Problem:** Given an array of integers and an integer k, find the maximum mean of a subarray of size k.

**Approach:** Sliding window technique to efficiently calculate sums without recalculating the entire window each time.

**Complexity Analysis:**
- **Time Complexity:** O(n) - Single pass through the array with constant time window updates
- **Space Complexity:** O(1) - Only using a few variables for tracking
- **Time Spent:** 10 minutes

---

### ✅ Question 2: ReverseVowels
**File:** [q2_reverse_vowels.py](q2_reverse_vowels.py)

**Problem:** Given a string, reverse the order of the vowels in the string.

**Approach:** Two-pointer technique - one pointer from the start and one from the end, swapping vowels when both pointers find them.

**Complexity Analysis:**
- **Time Complexity:** O(n) - Single pass through the string
- **Space Complexity:** O(n) - Converting string to list for in-place modifications
- **Time Spent:** 20 minutes

---

### ✅ Question 3: ZeroSumSubArrays
**File:** [q3_zero_subarrays.py](q3_zero_subarrays.py)

**Problem:** Given an array of integers, count the number of subarrays that sum to zero.

**Approach:** Brute force approach using nested loops to check all possible subarrays.

**Complexity Analysis:**
- **Time Complexity:** O(n²) - Nested loops to check all subarrays
- **Space Complexity:** O(1) - Only using variables for counting
- **Time Spent:** 10 minutes

---

### ✅ Question 4: BackspaceCompare
**File:** [q4_backspace_compare.py](q4_backspace_compare.py)

**Problem:** Given two strings representing series of keystrokes, determine whether the resulting text is the same. Backspaces are represented by the '#' character.

**Approach:** Use a stack to process each string, pushing characters and popping when encountering '#', then compare the final results.

**Complexity Analysis:**
- **Time Complexity:** O(n + m) - Where n and m are the lengths of the two strings
- **Space Complexity:** O(n + m) - Stack space for both strings
- **Time Spent:** 12 minutes

---

### ✅ Question 5: ShortestSubstrings
**File:** [q5_shortest_substrings.py](q5_shortest_substrings.py)

**Problem:** Given a string and a second string representing required characters, return the length of the shortest substring containing all the required characters.

**Approach:** Sliding window with two pointers - expand the window to include all required characters, then shrink from the left while maintaining validity to find the minimum length.

**Complexity Analysis:**
- **Time Complexity:** O(n + m) - Where n is the length of the string and m is the length of required characters
- **Space Complexity:** O(m) - Space for character frequency maps
- **Time Spent:** 15 minutes

---

### ✅ Question 6: MissingNumber
**File:** [q6_missing_number.py](q6_missing_number.py)

**Problem:** Given an integer n and a sorted array of integers of size n-1 which contains all but one of the integers in the range 1-n, find the missing integer.

**Approach:** Mathematical approach using the formula for sum of first n natural numbers. Calculate expected sum and subtract actual sum.

**Complexity Analysis:**
- **Time Complexity:** O(n) - Single pass to calculate sum
- **Space Complexity:** O(1) - Only using constant extra space
- **Time Spent:** 7 minutes

---

### ✅ Question 7: K-Anagrams
**File:** [q7_kanagram.py](q7_kanagram.py)

**Problem:** Two strings are considered to be "k-anagrams" if they can be made into anagrams by changing at most k characters in one of the strings. Determine if two strings are k-anagrams.

**Approach:** Use Counter from collections to count character frequencies, then calculate the minimum number of character changes needed.

**Complexity Analysis:**
- **Time Complexity:** O(n + m) - Where n and m are the lengths of the two strings
- **Space Complexity:** O(n + m) - Space for Counter dictionaries
- **Time Spent:** 10 minutes

---

### ✅ Question 8: MergeIntervals
**File:** [q8_Merge_Intervals.py](q8_Merge_Intervals.py)

**Problem:** Given a list of integer pairs representing intervals, merge all overlapping intervals.

**Approach:** Sort intervals by start time, then iterate through and merge overlapping intervals by extending the end value when necessary.

**Complexity Analysis:**
- **Time Complexity:** O(n log n) - Dominated by sorting step
- **Space Complexity:** O(n) - Space for the merged result list
- **Time Spent:** 12 minutes

---

### ✅ Question 9: DedupArray
**File:** [q9_DedupArray.py](q9_DedupArray.py)

**Problem:** Given a sorted array of non-negative integers, modify the array by removing duplicates so each element only appears once.

**Approach:** Iterate through the array and maintain a list of seen elements, only adding new elements that haven't been seen before.

**Complexity Analysis:**
- **Time Complexity:** O(n) - Single pass through the array
- **Space Complexity:** O(n²) - Due to list containment checks (can be optimized to O(n) using a set)
- **Time Spent:** 4 minutes

---


