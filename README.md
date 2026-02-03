# ucp-namer-latam-2026

## UCP Career Prep: Homework 0 Submission - Danny Tat

---

### Question 1: ZeroSum
* **Problem Type:** Array / Hash Map
* **Time Spent:** [37 mins]
* **Complexity Analysis:**
    * **Time Complexity:** $O(n)$ We iterate through the array once.
    * **Space Complexity:** $O(n)$ We created a hash map to store values

### Question 1 (Follow-Up): ZeroSum with Reuse
* **Problem Type:** Combinatorial Array Logic / Hash Map
* **Time Spent:** [57 mins]
* **Complexity Analysis:**
    * **Time Complexity:** $O(n)$ We use a for loop to iterate over the array and hash map
    * **Space Complexity:** $O(n)$ The frequency map stores at most $n$ unique integers

---

### Question 2: UniqueSum
* **Problem Type:** Array / Hash Map
* **Time Spent:** [10 mins]
* **Complexity Analysis:**
    * **Time Complexity:** $O(n)$ We use a single loop to process the array and check if its unique
    * **Space Complexity:** $O(n)$ We created a hash map to check if the number occur more than once

---

### Question 3: FirstOccurrence
* **Problem Type:** String / Hash Map
* **Time Spent:** [7 mins]
* **Complexity Analysis:**
    * **Time Complexity:** $O(n)$ We iterate through the string once, checking if its in the hash map
    * **Space Complexity:** $O(k)$ Space grows relative to $k$, the number of unique characters in the input string