#Run time: O(N) since it vist every node once
#Space: O(n) worst case
#Technique: BF traversal


"""
question: given binary tree, create an array of the left view of the tree

ideas: use BFS
    we create a queue in order to discover node by level
    
    everytime we discover a node, we gonna remove the parent and add the child node.

    while there exist elem in queue:
    
        we dequeue.when dequeue node, we can determine the number of node in that level since: node_num= len(queue)
        after find out the number of node in that level, we loop through all them and only add the first one to the list

        we keep dequeue the elem and add their child to the queue in order to implement the bfs (make sure to add from left -> right since we want leftmost)

"""
from collections import deque #double ended queue lib in python

class Node: 
    def __init__(self, data=None,left=None,right=None): 
        self.data=data 
        self.left=left
        self.right=right

def left_view(head):
    if head ==None:
        return []

    returned_lst=[]
    queue= deque()
    queue.append(head)

    while queue:
        #dequeue to implement bfs
        node_num_in_level= len(queue)

        #loop through every node in that level
        for i in range(node_num_in_level):
            left_most_node= queue.popleft()

            if i==0:
                returned_lst.append(left_most_node.data)

            if left_most_node.left:
                queue.append(left_most_node.left)
            if left_most_node.right:
                queue.append(left_most_node.right)
    
    return returned_lst
            

def test1():

    node1= Node(1)
    node2= Node(2)
    node3=Node(3,node1,node2)
    node5=Node(5)
    node4=Node(4,node3,node5)


    lst=[4,3,1]
    assert left_view(node4) == lst


if __name__=="__main__":
    test1()
    print("passed all")