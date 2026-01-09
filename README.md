# Algorithm Practice - Hash Tables & Arrays

## Overview
This repository contains solutions to algorithmic problems focusing on hash tables, arrays, and string manipulation.

---

## Problem 1: ZeroSum (No Reuse)

**Problem Type**: Array, Hash Table, Two Sum Variant

**Description**: Given an array of integers, return the number of pairs that sum to 0. Each element can be used in at most one pair.

**Time Spent**: 7 minutes

**Approach**: 
- Use a hash map to track seen numbers
- For each number, check if its complement (-num) exists
- Mark elements as used after pairing

**Complexity Analysis**:
- **Time Complexity**: O(n) - Single pass through the array
- **Space Complexity**: O(n) - Hash map stores up to n elements

**Examples**:
```
Input: [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
Output: 2
Pairs: (1, -1), (2, -2)
```

**Notes**: Initial implementation had a bug with element reuse tracking. Corrected to properly mark used elements.

---

## Problem 2: ZeroSum (Reuse Allowed)

**Problem Type**: Array, Hash Table, Combinatorics

**Description**: Count pairs that sum to 0, allowing elements to be reused across different pairs (but pairs must use elements from different indices).

**Time Spent**: 20 minutes

**Approach**:
- Build frequency map of all numbers
- For each unique number, calculate pairs with its complement
- Handle special case when number equals its complement (n * (n-1) / 2)
- Avoid double counting by only counting when `num < complement`

**Complexity Analysis**:
- **Time Complexity**: O(n) - One pass to build frequency map, one pass through unique elements
- **Space Complexity**: O(n) - Frequency map stores unique elements

**Examples**:
```
Input: [1, 10, 8, -2, 2, 5, 7, 2, -2, -1]
Output: 5
Pairs: (1,-1), (2,-2) x4
```

---

## Problem 3: UniqueSum

**Problem Type**: Array, Set Operations

**Description**: Return the sum of unique elements in an array.

**Time Spent**: 10 minutes

**Approach**:
- Convert array to set to get unique elements
- Sum all elements in the set

**Complexity Analysis**:
- **Time Complexity**: O(n) - Converting to set and summing
- **Space Complexity**: O(n) - Set stores unique elements

**Examples**:
```
Input: [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
Output: 35
```

**Alternative One-Liner**:
```python
return sum(set(arr))
```

---

## Problem 4: FirstOccurrence

**Problem Type**: String, Hash Set

**Description**: Return a string containing only the first occurrence of each character.

**Time Spent**: 10 minutes

**Approach**:
- Use a set to track seen characters
- Build result string by appending only unseen characters

**Complexity Analysis**:
- **Time Complexity**: O(n) - Single pass through string
- **Space Complexity**: O(n) - Set stores unique characters, result string up to n chars

**Examples**:
```
Input: "Uber Career Prep"
Output: "Uber CaPp"
```

**Notes**: Maintains original case and includes spaces.

---

## Total Time Spent
**47 minutes** across all problems

## Key Learnings
1. Hash maps are effective for O(1) lookup in pair-finding problems
2. Frequency maps enable efficient counting for reuse scenarios
3. Sets are perfect for uniqueness constraints
4. Edge cases matter: zero pairing with itself, element reuse rules

## Testing
All solutions tested with provided examples and edge cases including:
- Empty arrays
- Arrays with no pairs
- Arrays with all zeros
- Single element arrays