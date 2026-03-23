Recursion must have this 3 things:

    1. Base Case
    Stopping condition - when to STOP recursing
    Returns a value WITHOUT calling itself again
    Prevents infinite loops/stack overflow

    2. Recursive Case
    Function calls itself with MODIFIED parameters
    Makes the problem smaller/simpler each time
    Moves toward the base case

    3. Progress Toward Base Case
    Each recursive call must get closer to the base case
    Parameters must change in a meaningful way


Type of DFS:

    1. Pre Order (Normal when discovering node in a graph using DFS)
        - Discover root first, then vistied its subtree
        => The FIRST VISITED node is the ROOT and the LAST VISTED is the RIGHTMOST NON-ROOT NODE

        Use when: 
            + Copy, Clone a tree (since it does not change the structure of the tree, the other 2 does)
            + Print the structure from top to bottom

        Code:
            out = "";
            out += node.value.toString() + " ";
            out += preOrderTraversal(node.left);
            out += preOrderTraversal(node.right);
            return out



    2. In Order 
        - The root is visited between its subtree
        => LEFTMOST is discovered FIRST, then RIGHTMOST NODE is visted LAST

        Use when:
            + Sorted list in BST, since it always go to left most, then right most
            + Check if the tree is a valid BST
            + find the k-th smallest elem in BST

        Code:
            String out = "";
            out += inOrderTraversal(node.left);
            out += node.value.toString() + " ";
            out += inOrderTraversal(node.right);




    3. Post Order (discover left subtree, then right subtree, then the parent)
        - the root will be visted after its subtree (last)
        => first visited node is the LEFTMOST, last visited is the ROOT

        Use when:
            + need the children in order to work with root, since sometimes we can't process the parent until we have already processed the children.
            => Delete or Free a Tree
            => Evaluate expression trees
            => compute subtree values, light height, sum,..

        Code:
            out = "";
            out += postOrderTraversal(node.left);
            out += postOrderTraversal(node.right);
            out += node.value.toString() + " ";
            return out;

