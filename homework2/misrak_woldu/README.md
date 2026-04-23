## Question 1: Singly Linked List

### Question Type
Linked List

### Description
Implemented a singly linked list with basic operations including insert at front, insert at end, search, and delete.

### Time Spent
~40 minutes

### Approach
I created a Node class to store each value and a pointer to the next node.  
Then I created a SinglyLinkedList class that keeps track of the head node.  

For insertion:
- At the front → I update the head directly
- At the end → I traverse to the last node and attach the new node

For search:
- I loop through the list until I find the value or reach the end

For delete:
- I handle deleting the head separately
- Otherwise, I keep track of previous and current nodes to remove the target

### Edge Cases
- Empty list
- Deleting from empty list
- Searching in empty list
- Deleting head node
- Value not found

### Time & Space Complexity
- Insert front: O(1)
- Insert end: O(n)
- Search: O(n)
- Delete: O(n)
- Space: O(1) extra space

### Completion Status
Finished all methods and all tests passed.


## Question 2: Doubly Linked List

### Question Type  
Linked List (Doubly)

### Description  
Implemented a doubly linked list where each node stores a value and pointers to both the next and previous nodes.  
Supports insertion, deletion, traversal, and reversal operations.

### Time Spent  
60 minutes

### Approach 
I created a Node class with `value`, `next`, and `prev` pointers.  
Then I created a DoublyLinkedList class that tracks both the `head` and `tail`.

For insertion:
- At the front → update head and connect backward pointer
- At the back → use tail for O(1) insertion
- Before/after → reconnect previous and next nodes

For deletion:
- Handle head and tail separately
- Otherwise reconnect surrounding nodes using `prev` and `next`

For reverse:
- Swap `prev` and `next` for each node
- Swap head and tail

### Edge Cases  
- Empty list  
- Single node list  
- Deleting head or tail  
- Inserting before head  
- Inserting after tail  

### Time & Space Complexity  
- Insert front: O(1)  
- Insert back: O(1)  
- Insert before/after: O(1)  
- Delete: O(1)  
- Length: O(n)  
- Reverse: O(n)  
- Space: O(1) extra space  

### Completion Status  
Finished all methods and all tests passed.

## Question 3: Binary Search Tree

### Question Type  
Tree / Binary Search Tree (BST)

### Description  
Implemented a Binary Search Tree (BST) with operations including insert, delete, search, find minimum, and find maximum.

### Time Spent  
70 minutes

### Approach 
I used the BST property where:
- left subtree contains smaller values
- right subtree contains larger values

For insert:
- I traverse left or right depending on the value until I find an empty spot

For search:
- I compare the target value and move left or right accordingly

For delete:
- If the node is a leaf → remove it
- If it has one child → replace it with that child
- If it has two children → find the smallest value in the right subtree (successor), replace the node, and delete the successor

For min and max:
- I traverse all the way left (min) or right (max)

### Edge Cases  
- Empty tree  
- Single node tree  
- Deleting root  
- Deleting node with:
  - no children
  - one child
  - two children  
- Value not found  

### Time & Space Complexity  
- Insert: O(log n) average  
- Search: O(log n) average  
- Delete: O(log n) average  
- Min/Max: O(log n)  
- Space: O(1) extra (O(h) recursion stack for delete)

### Completion Status  
Finished all methods and all tests passed.

## Question 4: Queue

### Question Type  
Linked List / Queue (FIFO)

### Description  
Implemented a queue data structure using a linked list.  
The queue follows First In First Out (FIFO) order.

### Time Spent  
35 minutes

### Approach  
I used a linked list structure with two pointers:
- `front_node` → points to the first element
- `back_node` → points to the last element  

For enqueue:
- Add a new node at the back
- Update the back pointer

For dequeue:
- Remove the front node
- Move the front pointer forward
- If the queue becomes empty, update both front and back to None

I also tracked the size using a counter.

### Edge Cases  
- Enqueue into empty queue  
- Dequeue from empty queue  
- Queue becomes empty after dequeue  
- Peek on empty queue  

### Time & Space Complexity  
- Enqueue: O(1)  
- Dequeue: O(1)  
- Peek: O(1)  
- Size: O(1)  
- Space: O(n)  

### Completion Status  
Finished all methods and all tests passed.

## Question 5: Stack

### Question Type  
Linked List / Stack (LIFO)

### Description  
Implemented a stack data structure using a linked list.  
The stack follows Last In First Out (LIFO) order.

### Time Spent  
30 minutes

### Approach  
I used a linked list structure where the head represents the top of the stack.  

For push:
- Create a new node
- Point it to the current top
- Update the top pointer

For pop:
- Remove the top node
- Move the top pointer to the next node

For peek:
- Return the value at the top without removing it

I also tracked the size using a counter.

### Edge Cases  
- Push into empty stack  
- Pop from empty stack  
- Peek from empty stack  
- Stack becomes empty after pop  

### Time & Space Complexity  
- Push: O(1)  
- Pop: O(1)  
- Peek: O(1)  
- Size: O(1)  
- Space: O(n)  

### Completion Status  
Finished all methods and all tests passed.

## Question 6: Deque

### Question Type  
Linked List / Deque (Double-Ended Queue)

### Description  
Implemented a deque data structure using a doubly linked list.  
The deque allows insertion and deletion from both the front and the back.

### Time Spent  
60 minutes

### Approach  
I used a doubly linked list with two pointers:
- `front_node` → points to the front of the deque  
- `back_node` → points to the back  

Each node has both `next` and `prev` pointers, which allows efficient operations on both ends.

For adding:
- `add_front` → insert at the front and update pointers  
- `add_back` → insert at the back using the tail pointer  

For removing:
- `remove_front` → move front pointer forward  
- `remove_back` → move back pointer backward  

I also handled updating both pointers when the deque becomes empty.

### Edge Cases  
- Adding to empty deque  
- Removing from empty deque  
- Deque becomes empty after removal  
- Single element deque  
- Peek on empty deque  

### Time & Space Complexity  
- Add front/back: O(1)  
- Remove front/back: O(1)  
- Peek: O(1)  
- Space: O(n)  

### Completion Status  
Finished all methods and all tests passed.

## Question 7: CopyTree

### Question Type  
Tree / Depth-First Search (DFS)

### Description  
Created a function to make a deep copy of a binary tree.  
The copied tree has the same structure and values as the original but consists of completely new nodes.

### Time Spent  
40 minutes

### Approach
I used recursion (DFS) to copy the tree.

For each node:
- I create a new node with the same value
- Recursively copy the left subtree
- Recursively copy the right subtree

This ensures that every node in the new tree is a separate object while preserving the structure.

### Edge Cases  
- Empty tree (None)  
- Single node tree  
- Skewed tree (all left or all right)  

### Time & Space Complexity  
- Time: O(n) because every node is visited once  
- Space: O(h) due to recursion stack (h = tree height)  

### Completion Status  
Finished implementation and all tests passed.

## Question 8: IsBST

### Question Type  
Tree / Depth-First Search (DFS)

### Description  
Determined whether a binary tree is a valid Binary Search Tree (BST).

### Time Spent  
40 minutes

### Approach
I used a recursive DFS approach with a valid range for each node.

Each node must satisfy:
- its value must be greater than all values in the left subtree
- its value must be less than all values in the right subtree

To enforce this, I passed down a range:
- left subtree → max becomes current node value
- right subtree → min becomes current node value

If any node violates this range, the tree is not a BST.

### Edge Cases  
- Empty tree  
- Single node  
- Duplicate values  
- Deep violations (not just immediate children)  
- Skewed trees  

### Time & Space Complexity  
- Time: O(n) — visit every node once  
- Space: O(h) — recursion stack (h = tree height)  

### Completion Status  
Finished implementation and all tests passed.

## Question 9: DedupSortedList

### Question Type  
Linked List / Two-pointer (single pass)

### Description  
Removed duplicate values from a sorted linked list in place, ensuring each value appears only once.

### Time Spent  
30 minutes

### Approach
Since the linked list is sorted, duplicates appear next to each other.

I used one pointer to traverse the list:
- If the current node and next node have the same value, I skip the next node
- Otherwise I move forward

This allows me to remove duplicates without using extra space.

### Edge Cases  
- Empty list  
- Single node list  
- All elements are duplicates  
- No duplicates  
- Multiple duplicate groups  

### Time & Space Complexity  
- Time: O(n) — traverse the list once  
- Space: O(1) — modify in place  

### Completion Status  
Finished implementation and all tests passed.

## Question 10: MoveNthLastToFront

### Question Type  
Linked List / Two-pointer (fixed distance)

### Description  
Moved the nth-last node of a linked list to the front while maintaining the order of the remaining nodes.

### Time Spent  
40 minutes

### Approach 
I used a two-pointer technique with a fixed distance.

- First, I moved a lead pointer n-1 steps ahead  
- Then I moved both the lead and trailing pointers together  
- When the lead pointer reached the end, the trailing pointer was at the nth-last node  

I then:
- removed that node from its position  
- moved it to the front of the list  

### Edge Cases  
- Empty list  
- Single node list  
- n = 1 (last node moves to front)  
- n equals list length (already at front)  
- n greater than list length  
- n ≤ 0  

### Time & Space Complexity  
- Time: O(n) — one pass through the list  
- Space: O(1) — no extra data structures  

### Completion Status  
Finished implementation and all tests passed.

## Question 11: IsPalindrome

### Question Type  
Linked List / Fast & Slow Pointers + Reverse

### Description  
Checked whether a linked list is a palindrome by comparing the first half with the reversed second half.

### Time Spent  
50 minutes

### Approach
I used fast and slow pointers to find the middle of the list.

- If the list length is odd, I skip the middle node  
- Then I reverse the second half of the list  
- Finally I compare the first half with the reversed second half  

If all values match, the list is a palindrome.

### Edge Cases  
- Empty list  
- Single node list  
- Even vs odd length  
- Two nodes  
- All same values  
- Not a palindrome  

### Time & Space Complexity  
- Time: O(n) — traverse list a few times  
- Space: O(1) — in place operations  

### Completion Status  
Finished implementation and all tests passed.

## Question 12: DisconnectCycle

### Question Type  
Linked List / Fast & Slow Pointers (Cycle Detection)

### Description  
Detected whether a linked list contains a cycle and removed the cycle if it exists.

### Time Spent  
45 minutes

### Approach 
I used the fast and slow pointer technique (Floyd’s algorithm).

- First, I moved a slow pointer (1 step) and a fast pointer (2 steps) to detect a cycle  
- If they meet a cycle exists  

To find where the cycle starts:
- I reset one pointer to the head  
- Move both pointers one step at a time  
- They meet at the start of the cycle  

To remove the cycle:
- I traverse from the cycle start until I find the last node in the cycle  
- Set its next pointer to None  

### Edge Cases  
- Empty list  
- Single node without cycle  
- Single node with cycle  
- Cycle starting at head  
- Cycle starting in the middle  
- No cycle  

### Time & Space Complexity  
- Time: O(n) — traverse list a few times  
- Space: O(1) — no extra memory used  

### Completion Status  
Finished implementation and all tests passed.

## Question 13: LeftView

### Question Type  
Tree / Breadth-First Search (BFS)

### Description  
Returned the values of nodes visible when looking at a binary tree from the left side.

### Time Spent  
30 minutes

### Approach
I used a level-order traversal (BFS).

- I processed the tree level by level using a queue  
- For each level I tracked the number of nodes  
- The first node in each level is the one visible from the left  

I collected those values into a result list.

### Edge Cases  
- Empty tree  
- Single node  
- Left-skewed tree  
- Right-skewed tree  
- Uneven trees  

### Time & Space Complexity  
- Time: O(n) — visit every node once  
- Space: O(w) — queue size (w = max width of tree)  

### Completion Status  
Finished implementation and all tests passed.

## Question 14: FloorInBST

### Question Type  
Tree / Binary Search Tree (BST search)

### Description  
Found the floor of a target value in a BST, which is the largest value less than or equal to the target.

### Time Spent  
25 minutes

### Approach 
I used the BST property to guide the search.

- If the current node value equals the target, that is the floor  
- If the current value is less than the target it is a candidate for floor so I store it and move right  
- If the current value is greater than the target I move left  

I keep track of the best floor value found so far.

### Edge Cases  
- Empty tree  
- Target smaller than all values  
- Target larger than all values  
- Exact match  
- Single node tree  

### Time & Space Complexity  
- Time: O(h), where h is tree height  
- Space: O(1)  

### Completion Status  
Finished implementation and all tests passed.