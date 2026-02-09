# ucp-namer-latam-2026

## UCP Career Prep: Homework 1 Submission - Danny Tat

---

### Question 1: MaxMeanSubArray
* **Problem Type:** Sliding Window
* **Time Spent:** 7 minutes
* **Complexity Analysis:** 
    * **Time Complexity:** $O(n): Use two for loops to iterate our array
    * **Space Complexity:** $O(1): Constant because we aren't making new space

--

### Question 2: ReverseVowels
* **Problem Type:** Two Pointers
* **Time Spent:** [19 mins]
* **Complexity Analysis:**
    * **Time Complexity:** $O(n)$ Use a while loop to iterate our pointers
    * **Space Complexity:** $O(n)$ Created a List and store result into list

--

### Question 3: ZeroSumSubArrays
* **Problem Type:** Hash Map
* **Time Spent** [35 minutes]
* **Complexity Analysis:**  
    * **Time Complexity:** $O(n)$: Use a for loop to iterate through the array
    * **Space Complexity:** $O(n)$: Created a hash map to store the value of our key

--

### Question 4: BackspaceStringCompare
* **Problem Type:** Stack
* **Time Spent:** [15 mins]
* **Complexity Analysis:**
    * **Time Complexity:** $O(n + m)$ We iterate through both strings independently
    * **Space Complexity:** $O(n + m)$ We use two stacks to store the resulting characters

--

### Question 5: ShortestSubstring
* **Problem Type:** Sliding Window (Variable Size)
* **Time Spent:** [40 mins]
* **Complexity Analysis:**
    * **Time Complexity:**$O(n + m)$ Both pointers travel across the string at most once
    * **Space Complexity:** $O(k)$ Space is used for frequency maps of the unique characters required

---

### Question 6: MissingInteger
* **Problem Type:** Hash Map
* **Time Spent:** [20 mins]
* **Complexity Analysis:****Time Complexity:
    * ** $O(n)$ We iterate through the array once and then through the range 1-n
    * **Space Complexity:** $O(n)$ We store n-1 elements in a hash map

---

### Question 7: KAnagrams
* **Problem Type:** String / Hash Map
* **Time Spent:** [19 mins]
    * **Complexity Analysis:****Time Complexity:** $O(n)$ We iterate through both strings of length $n$ once
    * **Space Complexity:** $O(k)$ Space grows relative to $k$, the number of unique characters in the input

--

### Question 8: MergeIntervals
* **Problem Type:** Sorting 
* **Time Spent:** [35 mins]
* **Complexity Analysis:**
    * **Time Complexity:** $O(n \log n)$ Due to the sorting step using the lambda key
    * **Space Complexity:** $O(n)$ To store the output list of merged intervals

--

### Question 9: DedupArray
* **Problem Type:** Two Pointer
* **Time Spent:** [10 mins]
* **Complexity Analysis:**
    * **Time Complexity:** $O(n)$ Use a single loop for our pointer
    * ***Space Complexity:** $O(1)$ Array is modified in place