# Homework 0 – Delight Oti

## q0_ZeroSum
**Problem Type:** Array / Hash Map  
**Time Spent:** ~40 minutes  

**Approach:**
- Use a dictionary (`Counter`) to store the frequency of each number.
- Iterate through the dictionary instead of the array to avoid repeated scans.
- Handle `0` as a special case since it pairs with itself.
- For nonzero values, repeatedly pair a number with its negative while both frequencies are greater than zero.
- Count each valid pair once and return the total.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

---

## q0_ZeroSum follow-up: Elements May Be Reused
**Problem Type:** Array / Hash Map / Combinatorics
**Time Spent:** ~30 minutes    

**Approach:**
- Store frequencies of all numbers using a dictionary.
- For `0`, compute the number of valid pairs using combinations.
- For nonzero values, multiply the frequency of a number by the frequency of its negative.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

---

## q1_UniqueSum
**Problem Type:** Array / Hash Set  
**Time Spent:** ~10 minutes  
**Approach:**
- Iterate through the array while tracking seen values using a set.
- If a value has not been seen before, add it to the set and include it in the sum.
- Return the final sum of unique elements.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

---

## q2_FirstOccurrence
**Problem Type:** String / Hash Set  
**Time Spent:** ~20 minutes  

**Approach:**
- Iterate through the string from left to right.
- Use a set to track characters that have already appeared.
- Append characters to a list only the first time they appear.
- Join the list into a string and return it.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

