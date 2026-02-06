# ucp-namer-latam-2026
## 1. MaxMeanSubArray

Description:
Given an array of integers and an integer k, find the maximum mean of any subarray of size k.

Approach:
Sliding window to maintain the sum of k elements and update the mean efficiently.

Time Complexity: O(n)

Space Complexity: O(1)

Time Spent: ~36 minutes

## 2. ReverseVowels

Description:
Reverse the order of vowels in a string while keeping other characters in place.

Approach:
Two-pointer technique with a helper function to check vowels.

Time Complexity: O(n)

Space Complexity: O(n) (char array)

Time Spent: ~15 minutes

## 3. ZeroSumSubArrays

Description:
Count the number of subarrays that sum to zero.

Approach:
Prefix sum + HashMap to track previously seen sums.

Time Complexity: O(n)

Space Complexity: O(n)

Time Spent: ~35 minutes

## 4. BackspaceStringCompare

Description:
Given two strings representing keystrokes (with # as backspace), determine if the final strings are equal.

Approach:
Traverse strings from right to left, skipping characters affected by backspaces.

Time Complexity: O(n + m)

Space Complexity: O(n + m)

Time Spent: ~15 minutes

## 5. ShortestSubstring

Description:
Given a string and a second string representing required characters, return the length of the shortest substring containing all required characters.

Approach:
Sliding window with a frequency array (ASCII size).

Time Complexity: O(n + m)

Space Complexity: O(1) (fixed-size array)

Time Spent: ~32 minutes

## 6. MissingInteger

Description:
Given a sorted array of size n-1 containing integers from 1 to n with one missing, find the missing integer.

Approach:
Two-pointer comparison to detect the missing gap.

Time Complexity: O(n)

Space Complexity: O(1)

Time Spent: ~10 minutes

## 7. KAnagrams

Description:
Determine whether two strings are k-anagrams (can be made anagrams by changing at most k characters in one string).

Approach:
Character frequency array for lowercase letters.

Time Complexity: O(n + m)

Space Complexity: O(1)

Time Spent: ~18 minutes

## 8. MergeIntervals

Description:
Given a list of intervals, merge all overlapping intervals.

Approach:
Sort intervals by start time, then merge using a sliding window approach.

Time Complexity: O(n log n)

Space Complexity: O(n)

Time Spent: ~38 minutes

## 9. DedupArray

Description:
Given a sorted array, remove duplicates so each element appears only once.

Approach:
Use a HashSet to track seen elements and overwrite the input array.

Time Complexity: O(n)

Space Complexity: O(n)

Time Spent: ~10 minutes
