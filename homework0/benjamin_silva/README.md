# Homework 0

## Question 1: Zero Sum (q1_ZeroSum.py)

### Problem Description:
For this problem I was tasked with finding the total amount of pairs that add up to zero in a given input list, and we can use the element at each index at most once.

### Problem Type: 
Array, Hash Map

### Approach:
I used a hash map to count the frequency of each number in the array. Then, I iterated through the hash map to find pairs that sum to zero by checking if the difference between 0 and the key exists in the map. To avoid double counting pairs, I only counted pairs where the key is positive. I attempted to handle the edge case of multiple zeros but I was unable to fully implement that part within the time limit.

### Time Complexity: O(n)
The time complexity if O(n). Building the frequency map takes on pass through the array which is O(n) and iterating through the hash map keys is O(n). Overall the time complexity is O(n).

### Space Complexity: O(n)
The hash map I made stores up to n unique elements from the array so that would take O(n) space.

### Time Spent: 
40 minutes

## Question 2: Unique Sum (q2_UniqueSum.py)

### Problem Description:
I was tasked with finding the sum of unique numbers in an input array. So numbers that only appear once.

### Problem Type: 
Array, Set

### Approach:
I used a set to automatically remove duplicate values from the array. Since sets only store unique elements, converting the array to a set removes all duplicates. Then I added all the unique elements using Pythons sum() function.

### Time Complexity: O(n)
The time complexity is O(n). Converting the array to a set requires iterating through all elements in the array which takes O(n) time and summing the unique elements iteratres through at most n elements which is O(n) time. Overall, O(n).

### Space Complexity: O(n)
The set stores up to n unique elements in the worst case so its O(n) space.

### Time Spent: 
5 minutes

## Problem 3: First Occurence (q3_FirstOccurrence.py)

### Problem Description:
This problem tasked us with returning a string that only included characters first occurence from a input string.

### Problem Type:
Array, Set, Strings

### Approach:
I used a set to track which characters have already been seen and a list to maintain the order of the first occurrences. I iterate through the string once and for each character I check if it's already in the seen set. If not I add it to both the seen set and the result list. Finally I join the list into a string to return the result with characters in their first occurence order.

### Time Complexity: O(n)
Iterating through the string is O(n), set lookups and adding to sets are O(1), and joining the list at the end is O(n). Overall O(n) time.

### Space Complexity: O(n)
The set stores up to n unique characters, so O(n) space and the result list stores up to n characters so O(n) space. Overall O(n) space.

### Time Spent:
12 minutes
