# Homework 2

## Question 1: Singly Linked List (q1_singlyLinkedList.py)
 
### Time Spent: 40 minutes
 
### Approach:
For this question I implemented a singly linked list using a head-passing approach. Each function takes and returns the head node. 
 
Methods Implemented:
- `insertAtFront` — O(1)
- `insertAtBack` — O(n)
- `insertAfter` — O(n)
- `insertBefore` — O(n)
- `deleteFront` — O(1)
- `deleteBack` — O(n)
- `deleteNode` — O(n)
- `length` — O(n)
- `reverseIterative` — O(n)
- `reverseRecursive` — O(n)
 
 
## Question 2: Doubly Linked List (q2_doublyLinkedList.py)
 
### Time Spent: 20 minutes
 
### Approach:
So for this one I basically extended the singly linked list implementation by adding a `prev` pointer to each node, allowing O(1) insertion and deletion at any position given a node reference. The main difference from the singly linekd list is that every pointer operation requires updating both `next` and `prev` references. 
 
Methods Implemented:
- `insertAtFront` — O(1)
- `insertAtBack` — O(1)
- `insertAfter` — O(1)
- `insertBefore` — O(1)
- `deleteFront` — O(1)
- `deleteBack` — O(1)
- `deleteNode` — O(1)
- `length` — O(n)
- `reverseIterative` — O(n)
- `reverseRecursive` — O(n)

 
## Question 3: Binary Search Tree (q3_binarySearchTree.py)
 
### Time Spent: 40 minutes
 
### Approach:
For this question I implemented a BST class with a private root node. Insertion and and search use the BST ordering property, values less than the current node go left, greater go right. The `contains` method is implemented recursively while `insert` is iterative. The `delete` method handles deleting a leaf node, a node with one child and a node with two children, the two child case uses the in order successor to replace the deleted node while mainting BST ordering.
 
Methods Implemented:
- `min` — O(log n)
- `max` — O(log n)
- `contains` — O(log n)
- `insert` — O(log n)
- `delete` — O(log n)
 
## Question 4: Queue (q4_queue.py)
 
### Time Spent: 20 minutes
 
### Approach:
For this question I implemented a queue using a singly linked list as the underlying data structure with both a head and tail pointer. The head pointer enables O(1) dequeue by moving it forward and the tail pointer allows O(1) enqueue by appending to the end without traversal. Fifo order is kept since elements are added at the tail and removed from the head.
 
Methods Implemented:
- `peek` — O(1)
- `enqueue` — O(1)
- `dequeue` — O(1)
- `isEmpty` — O(1)


## Question 5: Stack (q5_stack.py)
 
### Time Spent: 20 minutes
 
### Approach:
For this question I implemented a stack using a singly linked list with a head pointer representing the top of the stack. Both push and pop operate at the head, giving O(1) time for both functions. LIFO is kept since elements are added and removed from the same end.
 
Methods Implemented:
- `top` — O(1)
- `push` — O(1)
- `pop` — O(1)
- `isEmpty` — O(1)

## Question 6: Deque (q6_deque.py)
 
### Time Spent: 20 minutes
 
### Approach:
For this question I implemented a deque using a doubly linked list as the data structure with both head and tail pointers. The doubly linked list allows O(1) insertion and deletion at both ends. `pushFront` and `popFront` operate at the head, while `pushBack` and `popBack` operate at the tail. The `prev` pointer on each node is what makes O(1) `popBack` possible without traversal.
 
Methods Implemented:
- `front` — O(1)
- `back` — O(1)
- `pushBack` — O(1)
- `pushFront` — O(1)
- `popFront` — O(1)
- `popBack` — O(1)
- `isEmpty` — O(1)

## Question 7: CopyTree (q7_copyTree.py)

### Technique: Depth-first traversal — pre-order

### Time Spent: 10 minutes

### Approach:
Used pre-order DFS recursion to create a deep copy of the binary tree. The base case returns None when the current node is None. For each node visited, a new Node object is created with the same data value, then the left and right subtrees are recursively copied and assigned to the new nodes left and right pointers. Because every node is a newly created object the result is a deep copy with no shared references to the orginal tree.

Time Complexity: O(n)
Space Complexity: O(n)

## Question 8: IsBST (q8_isBST.py)

### Technique: Search binary search tree (BST)

### Time Spent: 40 minutes

### Approach:
For this question I used recursive DFS with min and max bounds to validate the BST property at every node. Instead of just comparing a node to its immediate children, each recursive call passes down a valid range that the current node's value must fall within. Going left tightens the upper bound to the current nodes value, and going right tightens the lower bound. This catches non valid nodes that span multiple levels, such as a node that satisifies its immediate parent but not the ancestor's constraint.

### Time Complexity: O(n)
### Space Complexity: O(n)

 
## Question 9: DedupSortedList (q9_dedupSortedList.py)
 
### Technique: Fast and slow pointer
 
### Time Spent: 15 minutes
 
### Approach:
For this question I used a single pointe r`curr` to traverse the sorted linked list. At each node an inner while loop checks if `curr.next` has the same value as `curr`, if it does, the duplicate is skipped by rewiring `curr.next = curr.next.next`. This continues until `curr.next` is either a different value or None, at which pointer `curr` advances forward. Because the list is sorted, all duplicates are guaranteed to be next to the duplicate node, so a single pass is enough.
 
Time Complexity: O(n)
Space Complexity: O(1)
 

## Question 10: MoveNthLastToFront (q10_moveNthLastToFront.py)
 
### Technique: Fixed distance two-pointer
 
### Time Spent: 30 minutes
 
### Approach:
For this question I used a fixed distance two pointer with a dummy node to handle edge cases. First, the right pointer is advnaced `k` steps ahead of `left` to create a fixed gap. Then both pointers move together one step at a time until `right` reaches `None`, then `left` is sitting directly before the target node. The target node is then detached from its current positiong by making `left.next` skip it, and prepended to the front of the list by pointing `dummy.next` and updating `dummy.next` to the target node.
 
### Time Complexity: O(n)
### Space Complexity: O(1)

## Question 11: IsPalindrome (q11_isPalindrome.py)

### Technique: Doubly linked list forward-backward two-pointer

### Time Spent: 20 minutes

### Approach:
For this question i used a doubly linked list forward backward two pointer technique. First I traversed to the tail of the list to find the `right` pointer, while `left` starts at the head. Then moved both pointers towards the center, `left` forward with `next` and `right` backward with `prev`, comparing values at each step. If any pair of values are different, the list isnt a palindrome. The loop terminates when the two pointer meet or corss, which hands odd and even lengths.

### Time Complexity: O(n)
### Space Complexity: O(1)

 
## Question 12: DisconnectCycle (q12_disconnectCycle.py)
 
### Technique: Fast-slow two-pointer
 
### Time Spent: 40 minutes
 
### Approach:
For this question I used fast-slow two pointer. First, `slow` moves one step and `fast` moves two steps at a time, if they meet a cycle exists. Second, one pointer is reset to `head` and both pointer move on step at a time until they meet again, which is the cycle entry node. Third a `tail` pointer traverses the cycle from the entry until it finds the node whose `next` points back to the entry, then sets that nodes `next` to `None` to disconnect the cycle.
 
### Time Complexity: O(n)
### Space Complexity: O(1)

## Question 13: LeftView (q13_leftView.py)

### Technique: Level-order traversal

### Time Spent: 40 minutes

### Approach:
For this question I used BFS with a queue to process the tree level by level. At each level the size of the queue is saved befpre processing starts so I know how many nodes belong to the current level. The first node is processed at each level is the leftmost node, so its value is appended to the result array. All children of nodes at the current level are added to the queue for the next left. This continues until the queue is empty, the result array would then contain the leftmost node from every level.

### Time Complexity: O(n)
### Space Complexity: O(n)

## Question 14: FloorInBST (q14_floorInBST.py)

### Technique: Search binary search tree (BST)

### Time Spent: 23 minutes

### Approach:
For this question I used a BST search technique iterateively, maintaining a floor_val variable to track the best candidate seen so far. At each node if the current vlaue equals the target, it is the exact floor and is returned. If the current value is less than the target, it becomes the new floor candidate and I go right to look for something closer to the target. If the current value is greater than the target, it cannot be the floor so I go left. When traversal ends, floor_val holds the greatest value less than or equal to the target.

### Time Complexity: O(log n)
### Space Complexity: O(1)
 