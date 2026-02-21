# Homework 1

## Question 1: MaxMeanSubArray

### Problem Description:
For this problem we are given an array of integers and an integer k, and I need to find the maximum mean of a subarray of size k. A mean would be adding all the numbers and dividing it by the total number of elements.

### Problem Type:
Array, Two-Pointer/Sliding Window

### Approach
I used a sliding window to keep track of the window and get a running sum. I check if the current window size is greater than k if it is I remove the left most element from the sum and move the left pointer up 1. If the window is the size of k I calculate the mean (curr_sum / k) and compare it to the max_mean, if it is greater than the max mean then that is my new max_mean. Once the loop breaks I return the max_mean.

### Time Complexity: O(n) 
I have to iterate through the entire input arr and that takes n time.

### Space Complexity: O(1)
I use only a constant amount of extra space with variables like L, R, curr_sum etc. regardles of the input size, so the sapce is O(1)

### Time Taken:
This problem took me 38 minutes

## Question 2: ReverseVowels

### Problem Description:
For this problem I am given a string, and I need to reverse the vowels in the string. For example, the first vowel in the string should be reversed with the last vowel in the string.

### Problem Type:
String, Two Pointer

### Approach:
For my approach I went with using a two pointer algorithm. I create two pointers L and R, L is placed at the 0 index and R is placed at the last element in the string. I turn the string into a list of characters so I can easily swap characters. In each iteration of the main loop, I check if the characters at both the left and right pointers are vowels. If they are both vowels, I swap them and move both pointers inward. After each swap check, I use inner while loops to move the left pointer forward past any characters that arent vowels and move the right pointer backward past any characters that arent vowels, this process continues until the pointers meet or cross. Once the main loop finishes each vowel in the list has been swapped. I buid a new string called ret from the list and return the new reversed vowel string.

### Time Complexity: O(n)
It takes O(n) time to traverse through the array to identify vowels because each character in the string is visited at most once.

### Space Complexity: O(n)
Space is O(n) because I convert the input string to a list of chars which requires O(n) space.

### Time Taken:
20 minutes

## Question 3: ZeroSumSubarrays

### Problem Description:
For this problem I am given an array of integers and I need to find the total number of continuous subarrays whose sum equals to 0. 

### Problem Type:
Array, Hash Map, Prefix Sum

### Approach
I used a prefix sum with a hash map to track how many times each prefix sum has occured. I initialize the hash map with {0 : 1} to handle subarrays that start from the beginning. As I iterate through the array, I maintain a running sum (cur_sum). So if I've seen the same prefix sum before, it means the elements between those two positions sum to 0. So I check if cur_sum exists in my hash map, if it does I add that count to my result because each occurence represents a different zero sum subarray ending at the current position. Then I update the hash map to increment the count for cur sum. Once the loop finishes, I return the total count.

### Time Complexity: O(n)
I iterate through the entire input array once, and each hash map operation takes O(1) time, so the overall time complexity is O(n)

### Space Complexity: O(n)
In the worst case, all prefix sums are unique, so the hash map coult store n entires. Which would be O(n) time

### Time Taken:
This problem took me 34 minutes

## Question 4:

### Problem Description 
For this problem we are given 2 strings, and we need to compare the strings to see if they are the same, but the strings have '#' in them representing a back space, for example 'aa#' is equal to 'a' and 'aaa##' = 'a'. So we have to compare the strings with those backspaces to see if they are the same.

### Problem Type:
Two pointer, String

### Approach
For this problem I went with a two pointer approach to compare the strings. So what I did was I had two pointers each going to on of the input strings. I start the pointers at the back and they move backward. I also have a skip_counter for each string, how it works is every time the pointer goes over a # it increments the skip counter by 1 and while the counter is greater than 0 and the current char isnt a # then we skip the character, i do that for both strings until the pointers both land on a valid character or a character thats not skipped or is a #, once that happens I compare the characters to see if they are the same if they are I continue to decrement the pointers if they arent I return False. By the time the pointers land on a valid character or the skip counter reaches zero its possible that one of the pointers could've gone out of bounds, if they have I return false. Its also possible that both pointers have gone out of bounds, if thats the case I return True because that means both strings have been scanned and the characters have matched everytime they were compared.

### Time Complexity: O(n)
It takes O(n) time to scan each string because we visit each character in the strings, so O(n) for string s and O(n) for string t, so I believe the time complexity would be something like O(n + n), which I believe equates to O(n).

### Space Complexity: O(1)
No extra space was used in my solution.

### Time Taken:
This problem took me the entire 40 minutes

## Question 5:

### Problem Description:
For this problem I am given 2 strings s and t, and I need to find the length of the shortest substring in s that contains all the characters from t. For example, if s = abracadabra and t = abc, the shortest substring in s that contains t is brac, which has a length of 4.

### Problem Type:
Sliding Window, Hash Map

### Approach 
I was unable to implement my solution within the allowed 40 minutes, but my planned approach was to use a sliding window approach with two hash maps to track character frequencies. First, I create a hash_map to store the frequency of each character in t. Then I use a window_map to track characters in my current window as I expand it with the right pointer. I have a valid counter to track how many unique characters from t have been in the current window. As I expand the window by moving R, I add characters to window_map. When valid equals the number of unique characters in t, I know the current window contains all required characters. At this point I try to shrink the window from the left to find the min lengt, updating it whenever I find a smaller valid window. This would continue until R reaches the end of the stirng s and I return the min length found.

### Time Complexity: O(n + m)
So n is the length of strings s and m is the length of string t. I iterate through s once with the sliding window, and I iterate through t to build the hash map. Each character is processed at most twice, once when expanding and once when contracting, so the time complexity would be O(n + m)

### Space Complexity; O(n) ??
I believe its O(n) because I use two hash maps, one for t and one for the sliding window, and in the worst case, they store all unique characters from both strings making it O(n).

### Time Taken:
40 minutes

## Question 6:

### Problem Description:
For this problem I am given a sorted array of integers nums and an integer n, and I need to find the missing integer in the sequence. For example, nums = [1, 2, 3, 4, 6, 7] and n = 7, the missing integer is 5.

### Problem Type:
Array

### Approach:
For my approach I scan the array to find the missing integer. I iterate through the array comparing each element with the next element. If the difference between the conescutive elemnts is not exactly 1 then I've found the gap. When I find this gap I return nums[i] + 1, whcih is the missing integer. If I complete the loop without finding a gap it means the missing integer is at the end of the array so I return n.

### Time Complexity: O(n)
I iterate through the array once, checking each pair of consecutive elements. In the worst case, I check all n-1 pairs before finding the missing integer or saying its at the end so the time complexity os O(n).

### Space Complexity: O(1)
I only use a constant amount of extra scape with the loop i, so the space is O(1).

### Time Taken:
10 minutes

## Question 7

### Problem Description
For this problem I am given two strings s and t, and an integer k, and I need to determine if the two strings can become anagrams of each other by changing at most k characters. For example, apple and peach can become anagrams with 2 changes.

### Problem Type:
Hash Map, Strings

### Approach 
I used a hash map approach to track character frequencies and determine how many changes are needed. First, I remove all spaces from both strings and check if they have the same length, if they dont they cant be anagrams. Then I create two frequency maps to count the occurrences of each character in both strings. Next I iterate through map_s and for each character, I find the minimum count between s and t to determine how many matching chatacters there are. I use matching to track the total number of characters that already match between the two strings. The number of changes needed is len(s) - matching. Finally I check if the needed changes is less than or equal to k. If it is I return True, otherwise I return False.

### Time Complexity: O(n)
n is the length of the strings. I iterate through both strings once to build the frequency maps, which takes O(n) time. Then I iterate through one of the maps to count matching characters, which in the worst case takes O(n) time if all characters are unique. So the overall time complexity is O(n).

### Space Complexity: O(n)

I use two hash maps to store character frequencies. In the worst case, if all characters in the strings are unique both maps could store up to n entires, resulting in O(n) space.

### Time Taken:
37 minutes

## Question 8

### Problem Description:
For this problem I am given a list of intervals represented as pairs [start, end], and I need to merge all overlapping intervals and return a list of of the merged intervals.

### Problem Type:
Arrays, Sorting

### Approach:
I used a sorting and merging approach. First, I sort the intervals by their start times. Then I iterate through the sorted intervals and build a result list, for each interval I check if the result list is empty or if the current interval doesnt overlap with the last interval in the result. If there isnt an overlap I append the current interval as a sepereate interval. If there is an overlap I merge the intervals by updating the end time of the last interval in the result to be the maximum of the current end. Once ive processed everything I return the ret list. I know I have some errors in the code i believe my overlap condition might be backwards, and something else might be wrong, but I reached the 40 minute mark before figuring it out.

### Time Complexity: O(n logn)
The sorting take nlogn time where n is the number of intervals after sorting I iterate through all intervals once which takes O(n) time.

### Space Complexity: O(n)
THe result list in the worst case where no intervals overlap will contain n intervals.

### Time Taken
40 minutes

## Question 9:

### Problem Description:
For this problem I am given an array of integers that may have duplicates, I need to remove all duplicates and return an array with the unique elements.

### Problem Type:
Array, Hash Set

### Approach
I used a set approach to remove duplicates. I convert the input array into a set, then I convert the set back to a list and return the list.

### Time Complexity:
Converting the array to a set takes O(n) time as each element needs to be processed, converting the set back to a list also takes O(n) time.

### Space Complexity: O(n)

I create a new set to store the unique elements, which in the worst case it will store all elements of the list O(n), and when I create a new set from the list and the set contained all the elements from the orginal list it will also take O(n) space. Overall O(n) space.

### Time Taken:
5 minutes