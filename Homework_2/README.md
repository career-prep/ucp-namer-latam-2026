# Homework 2 - Solutions

## Problems Completed

### Question 1: Singly Linked List
**File:** [Question1.py](Question1.py)

**Problem:** Implement a singly linked list with insertAtFront, insertAtBack, insertAfter, insertBefore, deleteFront, deleteBack, deleteNode, length, reverseIterative, and reverseRecursive.

**Approach:** Node class with data and next fields. Pointer manipulation for O(1) methods, traversal for O(n) methods.

**Complexity Analysis:**
- insertAtFront: O(1)
- insertAtBack: O(n)
- insertAfter: O(1)
- insertBefore: O(n)
- deleteFront: O(1)
- deleteBack: O(n)
- deleteNode: O(n)
- length: O(n)
- reverseIterative: O(n)
- reverseRecursive: O(n)
- Time Spent: 40 mins

### Question 2: Doubly Linked List
**File:** [Question2.py](Question2.py)

**Problem:** Implement a doubly linked list with the same methods as Question 1, using prev pointers to enable O(1) insertion and deletion.

**Approach:** Node class with data, next, and prev fields. prev pointer allows O(1) insertBefore, deleteBack, and deleteNode.

**Complexity Analysis:**
- insertAtFront: O(1)
- insertAtBack: O(1)
- insertAfter: O(1)
- insertBefore: O(1)
- deleteFront: O(1)
- deleteBack: O(1)
- deleteNode: O(1)
- length: O(n)
- reverseIterative: O(n)
- reverseRecursive: O(n)
- Time Spent: 35 mins

### Question 3: Binary Search Tree
**File:** [Question3.py](Question3.py)

**Problem:** Implement a BST with min, max, contains, insert, and delete.

**Approach:** Iterative insert and search using BST ordering. Delete handles three cases: no children, one child, two children (in-order successor).

**Complexity Analysis:**
- min: O(log n)
- max: O(log n)
- contains: O(log n)
- insert: O(log n)
- delete: O(log n)
- Time Spent: 60 mins

### Question 4: Queue
**File:** [Question4.py](Question4.py)

**Problem:** Implement a Queue using a linked list with peek, enqueue, dequeue, and isEmpty.

**Approach:** Singly linked list with head and tail pointers. Enqueue at tail, dequeue from head for O(1) at both ends.

**Complexity Analysis:**
- peek: O(1)
- enqueue: O(1)
- dequeue: O(1)
- isEmpty: O(1)
- Time Spent: 35 mins

### Question 5: Stack
**File:** [Question5.py](Question5.py)

**Problem:** Implement a Stack using a linked list with top, push, pop, and isEmpty.

**Approach:** Singly linked list. Push and pop both operate on the head.

**Complexity Analysis:**
- top: O(1)
- push: O(1)
- pop: O(1)
- isEmpty: O(1)
- Time Spent: 25 mins

### Question 6: Deque
**File:** [Question6.py](Question6.py)

**Problem:** Implement a Deque with front, back, pushBack, pushFront, popFront, popBack, and isEmpty.

**Approach:** Doubly linked list with head and tail pointers for O(1) at both ends.

**Complexity Analysis:**
- front: O(1)
- back: O(1)
- pushBack: O(1)
- pushFront: O(1)
- popFront: O(1)
- popBack: O(1)
- isEmpty: O(1)
- Time Spent: 40 mins

### Question 7: CopyTree
**File:** [Question7.py](Question7.py)

**Problem:** Given a binary tree, create a deep copy and return the root of the new tree.

**Technique:** Depth-first traversal (generic)

**Approach:** Recursively copy each node, creating a new Node with the same data and recursively setting left and right children.

**Complexity Analysis:**
- Time Complexity: O(n)
- Space Complexity: O(n)
- Time Spent: 20 mins

### Question 8: IsBST
**File:** [Question8.py](Question8.py)

**Problem:** Given a binary tree, determine if it is a binary search tree.

**Technique:** Depth-first traversal (in-order)

**Approach:** In-order traversal collects all values, then checks the list is strictly increasing.

**Complexity Analysis:**
- Time Complexity: O(n)
- Space Complexity: O(n)
- Time Spent: 25 mins

### Question 9: DedupSortedList
**File:** [Question9.py](Question9.py)

**Problem:** Given a sorted singly linked list, remove duplicates so each value appears once.

**Technique:** Linked list reset/catch-up two-pointer

**Approach:** Single pointer traversal. If current equals next, skip next. Otherwise advance.

**Complexity Analysis:**
- Time Complexity: O(n)
- Space Complexity: O(1)
- Time Spent: 38 mins

### Question 10: MoveNthLastToFront
**File:** [Question10.py](Question10.py)

**Problem:** Given a singly linked list, move the nth from last element to the front.

**Technique:** Linked list fixed-distance two-pointer

**Approach:** Advance front pointer n steps, then move both until front hits the end. Back pointer lands on the target node.

**Complexity Analysis:**
- Time Complexity: O(n)
- Space Complexity: O(1)
- Time Spent: 25 mins

### Question 11: IsPalindrome
**File:** [Question11.py](Question11.py)

**Problem:** Given a doubly linked list, determine if it is a palindrome.

**Technique:** Doubly linked list forward-backward two-pointer

**Approach:** Two pointers from head and tail moving inward, comparing values. prev pointer enables backward traversal without extra space.

**Complexity Analysis:**
- Time Complexity: O(n)
- Space Complexity: O(1)
- Time Spent: 20 mins

### Question 12: DisconnectCycle
**File:** [Question12.py](Question12.py)

**Problem:** Given a singly linked list, disconnect the cycle if one exists.

**Technique:** Linked list fast-slow two-pointer

**Approach:** Floyd's cycle detection. Fast and slow pointers meet inside the cycle. Reset slow to head, advance both one step until they meet at the cycle start, then sever the link.

**Complexity Analysis:**
- Time Complexity: O(n)
- Space Complexity: O(1)
- Time Spent: 35 mins

### Question 13: LeftView
**File:** [Question13.py](Question13.py)

**Problem:** Given a binary tree, return an array of the leftmost element at each level.

**Technique:** Level-order (breadth-first) traversal

**Approach:** BFS with a deque. At each level, record the first node and enqueue its children.

**Complexity Analysis:**
- Time Complexity: O(n)
- Space Complexity: O(n)
- Time Spent: 30 mins

### Question 14: FloorInBST
**File:** [Question14.py](Question14.py)

**Problem:** Given a target value and a BST, return the floor (greatest value less than or equal to target).

**Technique:** Search binary search tree (BST)

**Approach:** Traverse the BST. If current value is less than target, record it as best candidate and go right. Otherwise go left.

**Complexity Analysis:**
- Time Complexity: O(log n)
- Space Complexity: O(1)
- Time Spent: 40 mins

## Summary
- Total Time: ~8 hrs
- Completed: 14/14 problems
- Pending: None

CC: careerprep@uber.com
