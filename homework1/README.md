# Homework 1

## Question 1: MaxMeanSubArray

### Problem Description: Given an array of integers and an integer, k, find the maximum mean of a subarray of size k.

### Problem Type:  Static sliding window

### Approach: Decided to look use sliding window method and essentially calculate the sum up to k, and at each iteration, remove from the left and add to the right, compare and determine max sum until the end

### Time Complexity:  O(n)

### Space Complexity: O(1)

### Time Spent: 20 min


## Question 2: ReverseVowels

### Problem Description: Given a string, reverse the order of the vowels in the string
### Problem Type:  Dynamic Sliding Window

### Approach: Decided to look use dynamic sliding window method approach and switch vowels using the list version of the string as a helper. This way we can swap parts without any issues.

### Time Complexity:  O(n)

### Space Complexity: O(n)


### Time Spent: 20 min

## Question 3: ZeroSumSubArrays

### Problem Description: Given an array of integers, count the number of subarrays that sum to zero


### Problem Type:  Prefix  One-directional hashmap

### Approach: Reminded me of a complement map and implemented the idea keeping track of the running sum.

### Time Complexity:  O(n)

### Space Complexity: O(n)

### Time Spent: 30 min

## Question 4: BackSpaceStringCompare

### Problem Description: Given two strings representing series of keystrokes, determine wheter the resulting  text is the same. Backspaces are represented by the '#' character so "x#" results in the empty string ("").


### Problem Type:  Backwards two pointer 

### Approach: I felt like it made the most sense to implement some sort of backwrads two pointer, where we start at the end of both strings and go backwards, using a helper function to skip over the backspaced characters

### Time Complexity:  O(n)

### Space Complexity: O(1)

### Time Spent: 30 min


## Question 5: Shortest Substring

### Problem Description: Given a string and a second string representing required characters, return the length of the shortest substring containing all the required characters


### Problem Type:  Dynamic sliding window

### Approach: Most difficult one so far, decided to use some sort of shrinking/growing sliding window with a helper function to see if smaller windows meet reqs

### Time Complexity:  O(n^2)

### Space Complexity: O(n)

### Time Spent: 40 min

## Question 6: missing integer

### Problem Description: Given an itneger n and a sorted array of integers of size n-1 which ontain all but  one of the integers in  the range 1-n, find the missing integr


### Problem Type:  binary search

### Approach: Classic binary search approach

### Time Complexity:  O(log n)

### Space Complexity: O(1)

### Time Spent: 15  min


## Question 7: KAnagrams

### Problem Description: Two strings are considered to be k anagrams if they can be made into anagrams by changing at most k characters in one of the strings. Given two strings and an integer k, determine if they are k anagrams

### Problem Type:  Bucket sort/hashmap?

### Approach: Mapped this solution to one a neetcode question that I solved before. Arrived to optimal space complexity after using a fixed size list to keep count of each character count, then added that count and if its not the same as k, it's not valid

### Time Complexity:  O(n)

### Space Complexity: O(1)

### Time Spent: 15  min

## Question 8: mergeIntervals

### Problem Description: Given a list of integer pairs representing the low and high end of an interval, inclusive, return a list which overlapping intervals are merged

### Problem Type: sort->solve

### Approach: Correctly identified Technique->Sort the array, then solve

### Time Complexity:  

### Space Complexity: 

### Time Spent: 40  min

## Question 9: deduparray

### Problem Description: Given a sorted array of non neg integers, modify the array by removing duplicates so each element appears once. If arrays are static in your language of choice, the remaining elements should appear in the left hand side of the array and the extra space in the right hand should be padded with -1s

### Problem Type: two pointer

### Approach: Used a read pointer to scan the array and a write pointer to place each unique element at the front of the list. Then, truncating the remaining duplicates using Python's slicing

### Time Complexity:   O(n)

### Space Complexity:  O(1)

### Time Spent: 35  min