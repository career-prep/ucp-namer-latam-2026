# Homework 0 – Delight Oti

## q0_ZeroSum
**Problem Type:** Array
**Time Spent:** ~30 minutes
**Approach:**
- Iterate through the array using two indices.
- For each element, compute the value needed to sum to zero.
- Search the remaining portion of the array for that value.
- Use a set to ensure each index is used at most once.
- Store valid pairs and return the total number of pairs.
**Time Complexity:** O(n²)
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
