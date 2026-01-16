# UCP NAMER LATAM 2026 - Problem Solutions

## Problem 1: Zero Sum (Part 1)

**File:** `q1_ZeroSum.py`

**Problem Type:** Array, Hash Map

**Description:** Given an array of integers, return the number of pairs that sum to 0, where each element can only be used once.

**Time Spent:** 30 minutes

**Complexity Analysis:**

- **Time Complexity:** O(n²) - Nested loops to check all pairs
- **Space Complexity:** O(n) - Hash map to track used indices

---

## Problem 1: Zero Sum (Part 2 - Follow-up)

**File:** `q1_ZeroSumFollowup.py`

**Problem Type:** Array, Hash Map

**Description:** Given an array of integers, return the number of pairs that sum to 0, where elements can be reused across different pairs (but pairs must use different indices).

**Time Spent:** 50 minutes

**Complexity Analysis:**

- **Time Complexity:** O(n²) worst case (when many duplicates exist), O(n) average case
- **Space Complexity:** O(n) - Hash map to store frequency counts

---

## Problem 2: Unique Sum

**File:** `q2_UniqueSum.py`

**Problem Type:** Array, Hash Set

**Description:** Given an array of integers, return the sum of unique elements in the array.

**Time Spent:** 7 minutes

**Complexity Analysis:**

- **Time Complexity:** O(n) - Single pass through the array
- **Space Complexity:** O(n) - Hash set to track seen elements

---

## Problem 3: First Occurrence

**File:** `q3_FirstOccurence.py`

**Problem Type:** String, Hash Set

**Description:** Given a string, return a string containing only the first occurrence of each character.

**Time Spent:** 7 minutes

**Complexity Analysis:**

- **Time Complexity:** O(n) - Single pass through the string
- **Space Complexity:** O(n) - Hash set to track seen characters, plus output string
