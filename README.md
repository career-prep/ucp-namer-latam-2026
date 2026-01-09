# Problem Solutions Documentation

This repository contains solutions to various coding problems. Below is a detailed breakdown of each problem.

---

## Problem 1: Zero Sum Pairs

**File:** `abubakar_bolakale/q1_Zerosum.py`

**Problem Type:** Array, Hash Table / Dictionary

**Time Spent:** 30 minutes

**Problem Description:**  
Find the number of pairs of numbers in an array that sum to zero. Handles duplicate values and special case for zero.

**Solution Approach:**
- Use a dictionary to count the frequency of each number
- For each unique number, check if its complement (negative value) exists
- Count pairs based on minimum frequency between number and its complement
- Special handling for zero: count pairs as `count[0] // 2`

**Complexity Analysis:**
- **Time Complexity:** O(n)
  - O(n) to build the frequency dictionary by iterating through the array
  - O(n) to iterate through dictionary keys (worst case all elements are unique)
  - Overall: O(n)
  
- **Space Complexity:** O(n)
  - O(n) for the frequency dictionary
  - O(n) for the `seen` set to track processed pairs
  - Overall: O(n)

---

## Problem 1 (Follow-up): Zero Sum Pairs (Optimized)

**File:** `abubakar_bolakale/q1_ZerosumFollowup.py`

**Problem Type:** Array, Hash Table / Dictionary

**Time Spent:** Not specified (follow-up version)

**Problem Description:**  
Optimized version of the zero sum pairs problem, removing the `seen` set check while maintaining correctness.

**Solution Approach:**
- Similar to Problem 1, but without the `seen` set
- Relies on dictionary iteration order and logic to avoid double counting

**Complexity Analysis:**
- **Time Complexity:** O(n)
  - O(n) to build the frequency dictionary
  - O(n) to iterate through dictionary keys
  - Overall: O(n)
  
- **Space Complexity:** O(n)
  - O(n) for the frequency dictionary
  - No additional `seen` set, slightly more space-efficient than Problem 1
  - Overall: O(n)

---

## Problem 2: Unique Sum

**File:** `abubakar_bolakale/q2_UniqueSum.py`

**Problem Type:** Array, Set

**Time Spent:** 3 minutes

**Problem Description:**  
Calculate the sum of all unique elements in an array (each distinct value counted only once).

**Solution Approach:**
- Convert the array to a set to get unique elements
- Sum all elements in the set

**Complexity Analysis:**
- **Time Complexity:** O(n)
  - O(n) to convert array to set (iterating through all elements)
  - O(n) to iterate through set elements and calculate sum
  - Overall: O(n)
  
- **Space Complexity:** O(n)
  - O(n) for the set storing unique elements
  - Overall: O(n)

---

## Problem 3: First Occurrence

**File:** `abubakar_bolakale/q3_FirstOccurence.py`

**Problem Type:** String, Hash Table / Set

**Time Spent:** 10 minutes

**Problem Description:**  
Return a string containing only the first occurrence of each character from the input string, preserving the order of first appearance.

**Solution Approach:**
- Use a set to track seen characters
- Use a list to maintain order of first occurrences
- Iterate through the string, adding characters to the result only if not seen before
- Join the list to form the result string

**Complexity Analysis:**
- **Time Complexity:** O(n)
  - O(n) to iterate through each character in the input string
  - Set operations (add, contains) are O(1) on average
  - List append is O(1)
  - String join is O(k) where k is the number of unique characters (k ≤ n)
  - Overall: O(n)
  
- **Space Complexity:** O(n)
  - O(n) for the `seen` set (worst case: all characters are unique)
  - O(n) for the `unique` list (worst case: all characters are unique)
  - Overall: O(n)

---
**Total Time Spent:** ~43 minutes (excluding follow-up)

