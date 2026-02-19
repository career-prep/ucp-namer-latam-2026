
## Question 1: MaxMeanSubArray

**Question Type:** 
Array / Fixed-size Sliding Window

**Description:**  
Given an array of integers and an integer `k`, find the maximum mean (average) of any contiguous subarray of size `k`.

**Time Spent:**  
 35 minutes  

**Approach:**  
I use a fixed-size sliding window of length `k`.  
1. First, I add the first `k` numbers to get the first window sum.  
2. Then I slide the window one step at a time:  
   - subtract the number that leaves the window  
   - add the new number that enters the window  
3. I keep track of the largest window sum I ever see.  
4. At the end I divide the best sum by `k` to get the maximum mean.

**Edge Cases Considered:**  
- `k` is 1 (mean is just the max element)  
- All numbers are negative  
- `k` equals the array length (only one window)  
- Invalid `k` values like `k <= 0` or `k > len(array)` (should raise an error)

**Time Complexity (Justification):**  
**O(n)** because I go through the array once, and each slide updates the sum in constant time.

**Space Complexity (Justification):**  
**O(1)** because I only store a few variables (window sums and indices) not extra arrays.

**Finished?**  
 Yes in 35 mintues 

**Tests Passed?**  
All tests passed 

## Question 2: ReverseVowels

**Question Type:** 
String manipulation / Two-pointer

**Description:**  
Reverse only the vowels in a string while keeping all other characters in the same position.

**Approach:**  
I used two pointers, one starting from the beginning of the string and one from the end.
Each pointer moves until it finds a vowel.
When both pointers point to vowels, I swap them and move inward.
This continues until the pointers meet.

**Edge Cases Considered:** 

Empty string
No vowels
Only vowels
Uppercase and lowercase vowels

**Time Complexity (Justification):** 
O(n) because each character is visited at most once by the two pointers.

**Space Complexity (Justification):** 
O(n) because the string is converted to a list to allow swapping.

**Time Spent:**  
38 mintues

**Finished?** 
Yes on time

**Tests Passed?** 
All tests passed

## Question 3: ZeroSumSubArrays

**Question Type:** 
Array / Hashing / Prefix Sum

**Description:**  
Given an array of integers count how many subarrays sum to zero. A subarray is a continuous portion of the array.

**Time Spent:**  
30 mintues 

**Approach:**  
I used a running total (prefix sum) and a hash map to track how often each running sum appears.
As I loop through the array:
    I keep adding each number to a running total.
    If I see the same running total again it means the numbers in between sum to zero.
    I use a dictionary to count how many times each running total has appeared so far.
    Every time a running total repeats I add that count to my answer.
This lets me count all zero sum subarrays in one pass through the array.

**Edge Cases Considered:** 
Empty array -> no subarrays
Single zero -> counts as one zero sum subarray
Multiple zeros -> creates multiple overlapping zero sum subarrays
Arrays with no possible zero sum subarrays

**Time Complexity (Justification):** 
O(n) because I loop through the array once and all dictionary operations are constant time.

**Space Complexity (Justification):** 
O(n) because in the worst case I store all unique prefix sums in a hash map.

**Finished?** 
Yes on time

**Tests Passed?** 
All tests passed

## Question 4: BackspaceStringCompare

**Question Type:** 
String / Two-Pointer Technique

**Description:**  
Given two strings that represent a series of keystrokes determine whether they produce the same final text.
The # character represents a backspace which deletes the previous character if one exists.

**Time Spent:**  
43 mintues 

**Approach:**  
I simulated how typing works using a stack like approach.

For each string:
    I loop through each character.
    If the character is not # I add it to a list.
    If the character is # I remove the most recent character (if one exists)
    After processing the whole string I join the list to get the final text

Once both strings are processed this way I compare their final results.

**Edge Cases Considered:** 
Strings that become empty after backspaces (eg "###")
More backspaces than characters
Strings with no backspaces
Case sensitivity ("A" and "a" are treated as different characters)

**Time Complexity (Justification):** 
O(n + m)
Each character in both strings is processed exactly once.
No nested loops.

**Space Complexity (Justification):** 
O(n + m)
Extra space is used to store the processed characters for both strings.

**Finished?** 
Yes on time

**Tests Passed?** 
All tests passed One test case initially failed due to a typo in the expected output which i corrected after validating the backspace behavior step by step

## Question 5: ShortestSubstring

**Question Type:** 
String / Sliding Window / Hash Map

**Description:**  
Given a string text and a string required return the length of the shortest substring of text that contains all characters from required including duplicate characters. If no such substring exists return 0.

**Time Spent:**  
40 mintues 

**Approach:**  
I used a variable size sliding window technique.

First I counted how many times each character appears in the required string.
Then I expanded a window over the text string using a right pointer and tracked character counts inside the window.

Once the window contained all required characters with the correct frequencies I tried shrinking the window from the left to find the smallest valid substring.
I continued expanding and shrinking the window until I reached the end of the string.

**Edge Cases Considered:** 
Empty text or required string
Required characters not present in text
Duplicate characters in required
Single character strings

**Time Complexity (Justification):** 
O(n)
Each character in text is visited at most twice once by the right pointer and once by the left pointer.

**Space Complexity (Justification):** 
O(m)
Extra space is used to store character counts for the required string and the current window where m is the number of unique required characters.

**Finished?** 
finished on time but debugged and that went a little over time like 5 mins 

**Tests Passed?** 
All tests passed
One expected value was corrected after verifying the actual shortest valid substring length.

## Question 6: MissingInteger
**Question Type:** 
Sorted Array / Binary Search Variation

**Description:**  
You are given an integer n and a sorted array of size n-1 that contains every integer from 1 to n except one.
Return the missing integer.

**Time Spent:**  
30 mintues 

**Approach:**  
Since the array is sorted I can use binary search to find where the “pattern breaks.”
Normally in a perfect array with no missing number:
    the value at index i (0-based) should be i + 1
When one number is missing everything after the missing spot shifts left meaning:
    at some point array[i] becomes greater than i + 1
So I binary search for the first index where array[mid] != mid + 1.
Then the missing number is mid + 1.

**Edge Cases Considered:** 
Missing number is in the middle (example: missing 5)
Missing number is the last number n (example: [1] with n=2 -> missing 2)
Missing number is the first number 1 (example: [2,3,4,...])
Smallest input sizes like n = 2

**Time Complexity (Justification):** 
O(log n)
Binary search halves the search space each step.

**Space Complexity (Justification):** 
O(1)
Only a few variables are used (pointers + mid) no extra data structures.

**Finished?** 
Finished on time

**Tests Passed?** 
All tests passed

## Question 7: KAnagrams

**Question Type:** 
String manipulation, Hashing (character frequency comparison)

**Description:**  
Given two strings and an integer k determine whether the two strings are k-anagrams. Two strings are considered k-anagrams if they can be made into anagrams of each other by changing at most k characters in one of the strings.

**Time Spent:**  
35 mintues 

**Approach:**  
First I check if the two strings have the same length.
    If they don’t they can never be anagrams so I return False.
I Count how many times each character appears in both strings using hash maps 
I then Compare the character counts:
    If the first string has extra characters that the second string does not have enough of those extra characters must be changed.
    Each extra character counts as one change.
Add up how many character changes are needed.
If the total number of changes needed is less than or equal to k return True. if not return False.

**Edge Cases Considered:** 
Empty strings
Strings with different lengths
Strings that are already anagrams (k = 0)
Strings with repeated characters
k being larger than the number of changes needed

**Time Complexity (Justification):** 
O(n + m)
n = length of the first string
m = length of the second string
We iterate through both strings once to build frequency counts.

**Space Complexity (Justification):** 
O(u)
u = number of unique characters across both strings
Extra space is used to store character counts in hash maps.

**Finished?** 
Finished on time

**Tests Passed?** 
All tests passed

## Question 8: MergeIntervals

**Question Type:** 
Array problem — Sorting & Interval Merging

**Description:**  
Given a list of integer pairs where each pair represents the start and end of an interval (inclusive) merge all overlapping intervals and return the final list of merged intervals. Two intervals overlap if the start of one interval is less than or equal to the end of another interval.

**Time Spent:**  
33 mintues 

**Approach:**  

First I sort all the intervals by their starting value.
This makes it easier to see which intervals overlap.
I then go through the sorted intervals one by one.
    I keep track of the current interval I am merging.
    If the next interval overlaps with the current one I extend the end of the current interval.
    If it does not overlap I save the current interval and start a new one.
At the end i add the last interval I was working on to the result.
This way I only need one pass after sorting to merge everything correctly

**Edge Cases Considered:** 
Empty list of intervals
Only one interval
Intervals that touch at the boundary (eg (1,2) and (2,3))
One interval completely inside another
Intervals given in unsorted order

**Time Complexity (Justification):** 
O(n log n)
Sorting the intervals takes O(n log n)
Merging them in one pass takes O(n)

**Space Complexity (Justification):** 
O(n)
In the worst case, none of the intervals overlap so we store all of them in the output list.

**Finished?** 
Finished 

**Tests Passed?** 
All tests passed

## Question 9: DedupArray

**Question Type:** 
Array manipulation using a two-pointer technique.

**Description:**  
Given a sorted array of non negative integers remove duplicate values so that each number appears only once.
The unique elements should be moved to the left side of the array.
Any remaining positions on the right side of the array should be filled with -1.

**Time Spent:**  
20 mintues 

**Approach:**  

Because the array is already sorted all duplicate values appear next to each other.
I used two pointers:
    One pointer (read_index) scans through the array.
    Another pointer (write_index) keeps track of where the next unique value should be placed
When the current value is different from the previous one it is a new unique number so it gets written at the write_index.
After processing all elements the remaining positions in the array are filled with -1.
This allows the array to be modified in place without using extra memory.

**Edge Cases Considered:** 
Empty array
Array with no duplicates
Array where all values are the same
Array with only one element

**Time Complexity (Justification):** 
O(n) because the array is scanned once from left to right.

**Space Complexity (Justification):** 
O(1) extra space because the array is modified in place and no additional data structures are used.

**Finished?** 
Finished didnt take long

**Tests Passed?** 
All tests passed