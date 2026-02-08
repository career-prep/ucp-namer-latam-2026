# Homework 1

## Q1: MaxMeanSubArray

**Problem Type:** Array, Sliding Window

**Time Spent:** 8 minutes

**Complexity:**
- Time: O(n) - single pass through the array with a sliding window
- Space: O(1) - only tracking window sum and max

## Q2: ReverseVowels

**Problem Type:** String, Two Pointers

**Time Spent:** 5 minutes

**Complexity:**
- Time: O(n) - two pointers traverse the string once
- Space: O(1) - vowel set is constant size, swap in place

## Q3: ZeroSumSubArrays

**Problem Type:** Array, Prefix Sum, Hash Map

**Time Spent:** 10 minutes

**Complexity:**
- Time: O(n) - single pass tracking prefix sums
- Space: O(n) - hash map to store prefix sum counts

## Q4: BackspaceStringCompare

**Problem Type:** String, Stack

**Time Spent:** 12 minutes

**Complexity:**
- Time: O(n + m) - single pass through each string to process backspaces
- Space: O(n + m) - building the processed strings

## Q5: ShortestSubstring

**Problem Type:** String, Sliding Window, Hash Map

**Time Spent:** 20 minutes

**Complexity:**
- Time: O(n) - sliding window with two pointers over the string
- Space: O(k) - hash maps where k is the number of unique required characters

## Q6: MissingInteger

**Problem Type:** Array, Math

**Time Spent:** 5 minutes

**Complexity:**
- Time: O(n) - single pass to compute the sum
- Space: O(1) - only tracking sums

## Q7: KAnagrams

**Problem Type:** String, Hash Map

**Time Spent:** 10 minutes

**Complexity:**
- Time: O(n) - single pass through each string to count characters
- Space: O(k) - hash map where k is the number of unique characters

## Q8: MergeIntervals

**Problem Type:** Array, Sorting, Intervals

**Time Spent:** 23 minutes

**Complexity:**
- Time: O(n log n) - sorting dominates, then single pass to merge
- Space: O(n) - output list of merged intervals

## Q9: DedupArray

**Problem Type:** Array, Two Pointers

**Time Spent:** 25 minutes

**Complexity:**
- Time: O(n) - single pass with read/write pointers
- Space: O(1) - in-place modification
