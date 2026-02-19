# Homework 0 - Misrak Woldu

This README documents my approach, time spent, and complexity analysis for Homework 0. 

## Question 0 
**Problem Type:**
 Array/Hashmap**

**Description:**
Given an array of integers , return the number of paris that sum to zero. Each element index can be used at most once.

**Time spent:**
~35 mintues 

**Approach**
I used a hash map to trak availabe numbers.
For each number I check if its complememt already exist and form a pair if possible. 

**Time Complexity:**
O(n)

**Space complexity**
O(n)

--------------

## Question 0 (Follow-up): Zero sum- reusable indices 

**Problem type**
Array/hasmap

**Description**
Count all index pairs (i < j) such that nums[i] + nums[j] == 0
Elements may be reused across differnt pairs

**Time spent**
~25

**Approach**
I used a hash map to count previously seen values. 
Each new value forms pais with al previously seen complements. 

**Time Complexity**
O(n)

**Space Complexity**
O(n)

----------

## Question 1:UniqueSum

**Problem Type:**
Array/ Hash set/ Hash Map

**Description:**
Return the sum of unique elements in the array

**Time spent**
~25 mintues 

**Approach:**
I used a hash map to count occurrences, then summed only values that appeared once

**Time complexity;**
O(n)

**Space Complexity**
O(n)


--------------------

# Question 2: FirstOccurrence

**Problem type:**
String/Hash set

**Description;**
Given a string retun a string containing only the first occrrence of each character, preserving order. 

**Time spent:**
20 mintues

**Approach:**
I iterated through the string and used a set to track seen characters, appending characters only the first time they appear. 

**Time complexity**
O(n)

**Space compexity;**
O(n)
