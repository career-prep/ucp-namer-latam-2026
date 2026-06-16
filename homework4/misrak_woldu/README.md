## Question 1: Build a Trie

### Question Type  
Trie / Prefix Tree

### Description  
Implemented a Trie data structure with the following methods:

- `insert(word)` — adds a word to the trie
- `is_valid_word(word)` — checks whether a full word exists in the trie
- `remove(word)` — removes a word from the trie and deletes unused nodes

### Time Spent  
40 minutes

### Approach  

I implemented the Trie using a `TrieNode` class and a `Trie` class.

Each `TrieNode` stores:
- `children`, which is a dictionary mapping each character to another TrieNode
- `valid_word`, which tells whether the node marks the end of a complete word

For `insert`:
- I start at the root node
- I go through each character in the word
- If the character does not exist as a child, I create a new TrieNode
- Then I move to that child node
- After processing all characters, I mark the last node as a valid word

For `is_valid_word`:
- I start at the root node
- I follow each character in the word
- If any character is missing, I return `False`
- After reaching the final character, I return whether that node is marked as a valid word

For `remove`:
- I used a recursive helper method
- The helper walks down the trie until it reaches the end of the word
- If the word exists, it unmarks `valid_word`
- Then it works backward and deletes child nodes that are no longer needed
- A node is deleted only if it has no children and is not the end of another valid word

This prevents deleting shared prefixes that are still needed by other words.

### Edge Cases  
- Searching for a word that was never inserted  
- Searching for a prefix that is not a full word  
- Removing a word that does not exist  
- Removing a word that shares a prefix with another word  
- Removing a word that is a prefix of another word  
- Removing a longer word while keeping the shorter prefix word  
- Empty string insertion and removal  

### Time & Space Complexity  

- Insert: O(L)  
  Where `L` is the length of the word, because each character is processed once

- Search: O(L)  
  Because each character in the word is checked once

- Remove: O(L)  
  Because the recursive helper follows the word character by character and may clean up nodes on the way back

- Space: O(T)  
  Where `T` is the total number of characters stored across all words in the trie


### Completion Status  
Finished implementation and all tests passed.

## Question 2: Boggle

### Question Type  
Trie as a Parameter / DFS Backtracking

### Description  
Given a Boggle board and a dictionary of valid words, return all valid words that can be formed on the board.

A valid word must:
- Be at least 3 characters long
- Exist in the dictionary
- Be formed using adjacent letters
- Allow diagonal movement
- Not reuse the same board position more than once in the same word


### Time Spent  
40 minutes

### Approach  

I used a Trie together with DFS backtracking.

First, I built a Trie from the dictionary. I only inserted words that have length 3 or more because the prompt says valid words must be at least three characters.

Each Trie node stores:
- `children`, which maps characters to the next TrieNode
- `word`, which stores the full word when that node marks the end of a valid dictionary word

Then I searched the board using DFS.

For each cell on the board:
- I start DFS from that cell
- I check whether the current character exists in the current Trie node
- If it does not exist, I stop early because no dictionary word can be formed from that path
- If it does exist, I move to the next Trie node
- If that Trie node stores a word, I add the word to the result set
- Then I explore all 8 directions: up, down, left, right and diagonals
- I use a visited set to make sure the same board position is not reused in one word
- After exploring a path, I remove the cell from visited so it can be used in other paths

Using the Trie helps avoid unnecessary searching because DFS stops as soon as the current path is not a prefix of any dictionary word.


### Edge Cases  
- Empty board  
- Empty dictionary  
- Words shorter than 3 characters  
- Words that are prefixes but not complete dictionary words  
- Diagonal movement  
- Preventing reuse of the same board cell in one word  
- Duplicate words found through different paths  


### Time & Space Complexity  

- Time: O(rows * cols * 8^L)  
  Where `L` is the maximum word length. In the worst case, DFS can explore up to 8 directions from each cell for each character path.

- Space: O(total dictionary characters + rows * cols)  
  The Trie stores all dictionary characters, and the DFS visited set can store up to all board positions in the current path.

### Completion Status  
Finished implementation and all tests passed.

## Question 3: Running Median

### Question Type  
Maintain Two Heaps

### Description  
Given an array of numbers representing a stream received one by one, return an array of the median after each new number is received.

### Time Spent  
30 minutes

### Approach  

I used two heaps to keep track of the lower half and upper half of the numbers seen so far.

The two heaps are:

- `lower_half`: a max heap that stores the smaller half of the numbers  
- `upper_half`: a min heap that stores the larger half of the numbers  

Since Python only has a min heap by default, I stored negative numbers in `lower_half` so it acts like a max heap.

For each number in the input:
- I add the number to one of the heaps
- If the number belongs in the smaller half, I add it to `lower_half`
- Otherwise, I add it to `upper_half`
- Then I rebalance the heaps so their sizes stay close
- Finally I calculate the current median and add it to the result list

The heaps are balanced so that:
- `lower_half` is allowed to have one more element than `upper_half`
- `upper_half` should never have more elements than `lower_half`

For the median:
- If both heaps have the same size, I average the two heap tops
- If one heap has more elements, the median is the top of `lower_half`

This works because the middle value or values are always at the top of the heaps.

### Edge Cases  
- Empty input → return empty list  
- Single number  
- Even number of values  
- Odd number of values  
- Duplicate values  
- Negative numbers  
- Increasing order input  
- Decreasing order input  


### Time & Space Complexity  

- Time: O(n log n)  
  Each number is inserted into a heap, and heap insertion/removal takes O(log n). Since there are `n` numbers, the total time is O(n log n).

- Space: O(n)  
  The two heaps together store all numbers from the stream.


### Completion Status  
Finished implementation and all tests passed.


## Question 4: Catalan Numbers

### Question Type  
Dynamic Programming - Tabulation

### Description  
Given a non-negative integer `n`, return the Catalan numbers from `0` to `n`.

### Time Spent  
40 minutes

### Approach  
I used dynamic programming with tabulation.

I created an array called `catalan` of size `n + 1`. The first value is `catalan[0] = 1`.

Then I calculated each Catalan number using the values already stored in the array. For each number, I loop through the possible left and right parts and add:

catalan[left_index] * catalan[right_index]

to build the current Catalan number.

If `n` is negative, I return an empty list.

### Edge Cases

* `n = 0`
* `n = 1`
* Negative input
* Larger values of `n`

### Time & Space Complexity

* Time: O(n²)
  Because each Catalan number uses a loop over previous values.

* Space: O(n)
  Because the array stores Catalan numbers from `0` to `n`.

### Completion Status
Finished implementation and all tests passed.

## Question 5: MinCostStairClimbing

### Question Type  
Dynamic Programming - Tabulation

### Description  
Given an array of costs where each index represents the toll cost for stepping on that stair, return the minimum cost needed to climb the staircase.

You can climb either 1 stair or 2 stairs at a time, and the last stair stepped on can be either `n - 1` or `n - 2`.

### Time Spent  
40 minutes

### Approach  
I used dynamic programming with tabulation.

I created an array called `min_cost`, where `min_cost[i]` stores the minimum cost needed to land on stair `i`.

The base cases are:
- `min_cost[0] = costs[0]`
- `min_cost[1] = costs[1]`

For each stair starting at index `2`, I calculate the minimum cost to reach that stair using:

costs[stair_index] + min(min_cost[stair_index - 1], min_cost[stair_index - 2])

This works because each stair can only be reached from either one stair before or two stairs before.

At the end, I return:

min(min_cost[-1], min_cost[-2])

because the prompt says the last stair stepped on can be either n - 1 or n - 2.

If the input list is empty, I return 0.
If there is only one stair, I return the cost of that stair.

### Edge Cases
Empty cost list
One stair
Two stairs
Increasing costs
Mixed costs
Larger input arrays

### Time & Space Complexity
Time: O(n)
Because each stair is processed once.
Space: O(n)
Because the min_cost array stores one value for each stair.

### Completion Status

Finished implementation and all tests passed.

## Question 6: WordBreak

### Question Type  
Dynamic Programming - Tabulation

### Description  
Given a string without spaces and a dictionary of valid words, determine if the string can be broken into valid dictionary words by adding spaces.

### Time Spent  
40 minutes

### Approach  
I used dynamic programming with tabulation.

First, I converted the dictionary into a set called `word_set` so that checking if a word exists is faster.

I also converted both the dictionary words and the input string to lowercase so the search is case-insensitive.

I created an array called `can_break`, where:

can_break[i]

means the substring from the start of the input string up to index i can be broken into valid dictionary words.

The base case is: can_break[0] = True

This means an empty string can be broken successfully.

Then I loop through every ending index in the string. For each ending index, I try every possible starting index before it and check: can_break[start_index] and current_word in word_set

If the part before start_index can already be broken, and the current substring is a valid dictionary word, then I mark: can_break[end_index] = True

At the end, I return: can_break[len(input_string)]

This tells whether the full string can be broken into valid words.

### Edge Cases
Empty string
Word already exists in dictionary
String cannot be broken into valid words
Multiple valid word combinations
Case differences between input and dictionary
Dictionary with words of different lengths

### Time & Space Complexity

Time: O(n² * m)
Because I check all possible substrings, and slicing each substring can take up to m time.
Space: O(n + d)
Because can_break stores n + 1 values, and word_set stores the dictionary words.

### Completion Status
Finished implementation and all tests passed.

## Question 7: LargestSquareOf1s

### Question Type  
Dynamic Programming - Tabulation

### Description  
Given a matrix of `0`s and `1`s, find the dimension of the largest square that contains only `1`s.

### Time Spent  
40 minutes

### Approach  
I used dynamic programming with tabulation.

I created a 2D array called `dp`, where:

dp[row_index][col_index]

stores the size of the largest square of 1s ending at that cell.

If the current cell in the original matrix is 0, then it cannot be part of a square, so the dp value stays 0.

If the current cell is 1:

If it is in the first row or first column, the largest square ending there can only be size 1
Otherwise, I look at the three neighboring values:
- above
- left
- diagonal top-left

Then I use: 1 + min(above, left, diagonal)

This works because a larger square can only be formed if all three neighboring directions support it.

I keep track of the largest square size found while filling the dp table.

### Edge Cases
Empty matrix
Matrix with no columns
Matrix with all 0s
Matrix with all 1s
Single-cell matrix
Matrix where the largest square is not at the end

### Time & Space Complexity
Time: O(rows * cols)
Because every cell in the matrix is processed once.
Space: O(rows * cols)
Because the dp table stores one value for each cell.

### Completion Status

Finished implementation and all tests passed.

## Question 8: CoinChange

### Question Type  
Dynamic Programming - Tabulation

### Description  
Given a list of coin denominations and a target sum `k`, return the number of possible ways to make change for that sum.

### Time Spent  
40 minutes

### Approach  
I used dynamic programming with tabulation.

I created an array called `ways`, where `ways[current_sum]` stores how many ways we can make that sum using the coins processed so far.

I start with: ways[0] = 1
because there is one way to make 0, which is using no coins.

Then I loop through each unique valid coin and update the ways array for every sum from that coin value up to the target. This counts combinations once and avoids counting different orders as separate answers.

If the target sum is negative, I return 0.
If the target sum is 0, I return 1.

### Edge Cases
Empty coin list
Target sum is 0
Negative target sum
Coin values larger than the target
Duplicate coin values
Invalid coin values like 0
No possible way to make the target sum

### Time & Space Complexity
Time: O(c * k)
Where c is the number of unique valid coin denominations and k is the target sum.
Space: O(k)
Because the ways array stores one value for each sum from 0 to k.

### Completion Status

Finished implementation and all tests passed.


## Question 9: AdoptAPet

### Question Type  
Maintain a Queue

### Description  
Given an initial list of pets and a sequence of adoption/addition events, return the pets as they are adopted.

Adopters can choose a species, but they receive the pet of that species that has been waiting the longest. If that species is unavailable, they receive the other species.

### Time Spent  
40 minutes

### Approach  
I used two queues:
- one queue for dogs
- one queue for cats

I first sorted the initial pets by time in shelter so the longest waiting pets are placed at the front of their species queue.

For each event:
- If the event is a person adopting, I check their preferred species queue first
- If that queue is empty, I check the other species queue
- If the event is a new pet, I add that pet to the back of the correct species queue

This keeps the longest waiting pet of each species at the front.

### Edge Cases  
- Desired species is unavailable
- No pets available
- New pets added during the sequence
- Empty initial pet list
- Empty event list

### Time & Space Complexity  
- Time: O(n log n + e)  
  Because the initial pets are sorted, and each event is processed once.

- Space: O(n)  
  Because the queues store the pets currently in the shelter.

### Completion Status  
Finished implementation and all tests passed.
