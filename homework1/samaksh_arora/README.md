# Uber Assignment No. 1

## Q1: MaxMeanSubarray

**Approach**
- I used a fixed sliding window approach
- First, I Calculated the mean of the first k elements
- I slid the window one element at a time:
  - Subtracted the element leaving the window
  - Added the element entering the window
- Then computed the mean at each step and see if it is greater than current mean variable

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)`

---

## Q2: ReverseVowels

**Approach**
- I used a two pointer approach, one starting at the beginning and one at the end of the string
- Move the left pointer forward until it found a vowel and right pointer backwards until it found a vowel
- Swap the vowels and move pointers again

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(n)`

---

## Q3: ZeroSumSubarrays

**Approach**
- I used the prefix sum frequency approach here
- Compute the prefix sum for each element and count the frequencies of the sums
- If any frequency is greater than 1 that means there are k*(k-1)//2 zero sum subarrays that I add to the count.

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(n)`

---

## Q4: Backspace String Compare

**Approach**
- I used two stacks, one for each string
- Iterated through each character in the string and if the character is not a "#" Which denotes a backspace, I push to the stack
- If the character is a "#, I pop the element from the stack if it is not empty

**Time Complexity:** `O(n + m)`  
**Space Complexity:** `O(n + m)`

---

## Q5: Shortest Substring Containing All Characters

**Optimal Approach**
- An Optimal Approach here would be to use a variable size sliding window
- Create a frequency hashmap of the required characters
- Initialize 2 pointers starting at the beginning of the given string
- Increment the rightPtr by 1 each time and each time check if the requirements are satisfied. 
- If the required characters are met calculate the length of the string and keep track of it. 

- I could not figure out how to compare the two hashmaps while incrementing the rightPtr.

**Current Approach**
- Brute force approach where for every element I move the pointer to the right until all the requirements are met
- Then keep track of the window length and return the minimum length

**Time Complexity:** `O(n² * m)`  
**Space Complexity:** `O(m)`

---

## Q6: MissingInteger

**Approach**
- Since the array is sorted from 1 - n-1, each number before the missing number should equal index+1
- Apply Binary search algorithm to the array.
- If the number is greater than index + 1 that means we can discard the right half
- If it is equal to index + 1 then we can discard the left half

**Time Complexity:** `O(log n)`  
**Space Complexity:** `O(1)`

---

## Q7: K-Anagrams

**Approach**
- Treat 1 string as target (string2 in my case).
- Make frequency  maps for both strings
- Calculate how many characters in string1 are different than in string2
- If the count is less than or equal to k, return True. If not, return False

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)`

---

## Q8: Merge Intervals

**Approach**
- I sorted all intervals by their start time
- Then I used two pointers to compare the current and next intervals
- If the end of the current interval is greater than the start of the next interval, merge both intervals
- If the end of the crrent interval is less then the start of the next interval, push the interval to the result list
- Lastly, push the last interval to the final result

**Time Complexity:** `O(n log n)`  
**Space Complexity:** `O(n)`

---

## Q9: Remove Duplicates from an Array

**Approach**
- I converted the array into a set to remove duplicate values
- Then I converted the set back to a list

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(n)`
