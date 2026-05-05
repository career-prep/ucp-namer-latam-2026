"""
idea: use bfs:
    - handle the case of num=0 separately
    -  when num=1 => use bfs:
        left_neighbor -> add 0 , right_neighbor -> add 1




"""
from collections import deque
def first_k_binary_numbers(k):
    #edge case
    if k==0:
        return []
    
    k_binary_list=[]

    #handle case when num=0
    k_binary_list.append("0")
    if k==1:
        return k_binary_list
    
    
    queue= deque()
    queue.append("1")

    while len(k_binary_list) < k:
        node= queue.popleft()

        k_binary_list.append(node)

        #find neighbor
        left_neighbor= node+ "0"
        right_neighbor= node+ "1"

        #add in queue
        queue.append(left_neighbor)
        queue.append(right_neighbor)
    
    return k_binary_list




def test1():
    print(first_k_binary_numbers(5))

def test2():
    print(first_k_binary_numbers(10))

test1()
test2()

