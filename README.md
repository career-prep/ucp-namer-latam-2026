# UCP NAMER LATAM 2026

Solutions to coding problems by **Aung Nanda Oo**.

## Problems Overview

| # | Problem | Technique | Time | Space |
|---|---------|-----------|------|-------|
| 1 | [SinglyLinkedList](#q1-singlylinkedlist) | Linked List Pointers | O(n) per op | O(1) |
| 2 | [DoublyLinkedList](#q2-doublylinkedlist) | Doubly Linked List Pointers | O(1) most ops | O(1) |
| 3 | [BinarySearchTree](#q3-binarysearchtree) | BST Traversal | O(log n) per op | O(1) |
| 4 | [Queue](#q4-queue) | Linked List (FIFO) | O(1) per op | O(1) |
| 5 | [Stack](#q5-stack) | Linked List (LIFO) | O(1) per op | O(1) |
| 6 | [Deque](#q6-deque) | Doubly Linked List | O(1) per op | O(1) |
| 7 | [CopyTree](#q7-copytree) | DFS Recursion | O(n) | O(n) |
| 8 | [IsBST](#q8-isbst) | DFS + Min/Max Bounds | O(n) | O(h) |
| 9 | [DedupSortedList](#q9-dedupsortedlist) | Single Pass Pointers | O(n) | O(1) |
| 10 | [MoveNthLastToFront](#q10-moventhlasttotfront) | Two Pointers | O(n) | O(1) |
| 11 | [IsPalindrome](#q11-ispalindrome) | Two Pointers (head+tail) | O(n) | O(1) |
| 12 | [DisconnectCycle](#q12-disconnectcycle) | Floyd's Cycle Detection | O(n) | O(1) |
| 13 | [LeftView](#q13-leftview) | BFS Level Order | O(n) | O(w) |
| 14 | [FloorInBST](#q14-floorinbst) | BST Traversal | O(log n) | O(1) |

---

## Q1: SinglyLinkedList

**Problem:** Implement insertAtFront, insertAtBack, insertAfter, insertBefore, deleteFront, deleteBack, deleteNode, length, reverseIterative, and reverseRecursive on a singly linked list.

**Example:**
```
insertAtFront([1->2->3], 0) -> [0->1->2->3]
reverseIterative([1->2->3]) -> [3->2->1]
```

**Approach:** Maintain a head pointer. Use pointer manipulation for insertions and deletions. For reverse, iterative uses prev/cur/next pointers; recursive uses a helper that builds up the reversed list on the call stack.

**Complexity:** O(n) time for traversal-based ops, O(1) for front ops; O(1) space

---

## Q2: DoublyLinkedList

**Problem:** Modify the singly linked list to add a prev pointer. Most operations become O(1) since we can navigate both directions.

**Example:**
```
insertAtBack([1<->2<->3], tail, 4) -> [1<->2<->3<->4]  (O(1) with tail reference)
deleteNode([1<->2<->3], node_2) -> [1<->3]              (O(1) with prev pointer)
```

**Approach:** Maintain both head and tail. Each node has prev and next. insertBefore and deleteNode become O(1) since we can access the predecessor directly via prev.

**Complexity:** O(1) for all ops except length and reverse; O(n) for those

---

## Q3: BinarySearchTree

**Problem:** Implement a BST class with min, max, contains, insert, and delete.

**Example:**
```
Insert: [5, 3, 7, 1, 4, 6, 9]
min() -> 1, max() -> 9
contains(3) -> True, contains(8) -> False
delete(3) -> replace with in-order successor
```

**Approach:** Standard BST property: left < root < right. min/max walk left/right until leaf. Delete handles three cases: no children, one child, two children (replace with in-order successor).

**Complexity:** O(log n) time, O(1) space (O(log n) call stack for recursive delete)

---

## Q4: Queue

**Problem:** Implement a Queue (FIFO) using a linked list with O(1) peek, enqueue, dequeue, and isEmpty.

**Example:**
```
enqueue(1), enqueue(2), enqueue(3)
peek() -> 1
dequeue() -> 1, dequeue() -> 2
isEmpty() -> False
```

**Approach:** Maintain head (front) and tail (back) pointers. Enqueue adds to tail, dequeue removes from head — both O(1).

**Complexity:** O(1) time per operation, O(1) space

---

## Q5: Stack

**Problem:** Implement a Stack (LIFO) using a linked list with O(1) top, push, pop, and isEmpty.

**Example:**
```
push(1), push(2), push(3)
top() -> 3
pop() -> 3, pop() -> 2
isEmpty() -> False
```

**Approach:** Maintain head as the top of the stack. Push adds to head, pop removes from head — both O(1). No tail needed since both operations occur at the same end.

**Complexity:** O(1) time per operation, O(1) space

---

## Q6: Deque

**Problem:** Implement a Deque (double-ended queue) using a doubly linked list with O(1) operations at both ends.

**Example:**
```
pushBack(1), pushBack(2), pushBack(3), pushFront(0)
front() -> 0, back() -> 3
popFront() -> 0, popBack() -> 3
```

**Approach:** Doubly linked list with head (front) and tail (back) pointers. pushFront/popFront operate on head, pushBack/popBack operate on tail — all O(1).

**Complexity:** O(1) time per operation, O(1) space

---

## Q7: CopyTree

**Problem:** Given a binary tree, create a deep copy and return the root of the new tree.

**Example:**
```
Input:  1 -> 2 -> 3 (tree)
Output: identical tree with no shared node references
```

**Approach:** Recursive DFS. At each node, create a new node with the same data, then recursively copy left and right subtrees.

**Complexity:** O(n) time, O(n) space (new tree + O(h) call stack)

---

## Q8: IsBST

**Problem:** Given a binary tree, determine if it is a binary search tree.

**Example:**
```
BST [5,3,7,1,4,6,9] -> True
Tree [5,3,4] (right child 4 < root 5) -> False
```

**Approach:** Pass a (min_val, max_val) range to each recursive call. A node is valid only if its value is strictly within the range. Tighten the range as you go left (max = node.data) or right (min = node.data).

**Complexity:** O(n) time, O(h) space (call stack)

---

## Q9: DedupSortedList

**Problem:** Given a sorted singly linked list, remove duplicates so each value appears once.

**Example:**
```
Input:  1->1->2->3->3->3->4->5->5
Output: 1->2->3->4->5
```

**Approach:** Single pass — if current node equals next, skip next. Otherwise advance.

**Complexity:** O(n) time, O(1) space

---

## Q10: MoveNthLastToFront

**Problem:** Given a singly linked list, move the nth from the last element to the front.

**Example:**
```
Input: 1->2->3->4->5, k=2
Output: 4->1->2->3->5
```

**Approach:** Two pointers with a dummy head. Advance fast pointer k+1 steps ahead, then walk both until fast is None. slow lands just before the target. Unlink target and prepend to head.

**Complexity:** O(n) time, O(1) space

---

## Q11: IsPalindrome

**Problem:** Given a doubly linked list, determine if it is a palindrome.

**Example:**
```
Input: 1<->2<->3<->2<->1 -> True
Input: 1<->2<->3<->4<->5 -> False
```

**Approach:** Find the tail, then use two pointers (head and tail) walking inward, comparing values at each step.

**Complexity:** O(n) time, O(1) space

---

## Q12: DisconnectCycle

**Problem:** Given a singly linked list, disconnect the cycle if one exists.

**Example:**
```
Input:  1->2->3->4->5->3 (cycle back to 3)
Output: 1->2->3->4->5
```

**Approach:** Floyd's cycle detection (fast/slow). After detecting a cycle, reset slow to head and advance both one step at a time to find cycle start. Then walk from cycle start to find the tail (node whose next == cycle start) and set tail.next = None.

**Complexity:** O(n) time, O(1) space

---

## Q13: LeftView

**Problem:** Given a binary tree, return an array of the leftmost element at each level.

**Example:**
```
Output: [7, 8, 10, 20, 15]
Output: [7, 20, 15]
```

**Approach:** BFS level-order traversal. At each level, record the first (leftmost) node's value.

**Complexity:** O(n) time, O(w) space (w = max width of tree)

---

## Q14: FloorInBST

**Problem:** Given a target and a BST, return the greatest element ≤ target (the floor). Return None if no such element exists.

**Example:**
```
BST [10,5,15,3,7,12,20], target=8  -> 7
BST [10,5,15,3,7,12,20], target=11 -> 10
BST [10,5,15,3,7,12,20], target=2  -> None
```

**Approach:** Walk the BST. If node.data == target, return immediately. If node.data > target, go left. If node.data < target, record as candidate floor and go right for a closer value.

**Complexity:** O(log n) time, O(1) space

---

## How to Run

```bash
python aungnanda_oo/q1_SinglyLinkedList.py
python aungnanda_oo/q2_DoublyLinkedList.py
python aungnanda_oo/q3_BinarySearchTree.py
python aungnanda_oo/q4_Queue.py
python aungnanda_oo/q5_Stack.py
python aungnanda_oo/q6_Deque.py
python aungnanda_oo/q7_CopyTree.py
python aungnanda_oo/q8_IsBST.py
python aungnanda_oo/q9_DedupSortedList.py
python aungnanda_oo/q10_MoveNthLastToFront.py
python aungnanda_oo/q11_IsPalindrome.py
python aungnanda_oo/q12_DisconnectCycle.py
python aungnanda_oo/q13_LeftView.py
python aungnanda_oo/q14_FloorInBST.py
```
