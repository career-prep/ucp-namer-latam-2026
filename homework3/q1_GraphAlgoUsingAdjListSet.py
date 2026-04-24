from collections import defaultdict
from collections import deque
#Building a graph representation using Array
#give: Input: [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)], initially weighted, with a From, To relationship

#assumptions: 
"""1. each node stores integer data
    2. all the elemnts are distinct
"""
#task 1: creating an adjacency list:

input = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]

# use the defaultdic to create a map with keys being the Node(vertex)["From"] and teh values 
# being an array of all the neighbours (all the "To")

adj_dic = defaultdict()

for u, v in input:
    adj_dic[u].append(v)

#Task 2a: implement a DFS to search for a Value (Recursion)

"""we are goin to use Recursion to implement the depth first search """

#algo:
# track the seen(visited) Nodes and use recursion to visit the depth using the Adj_dic 
# we just created above
# the element we are searching for: K
# assumtion: for the sake of simplicity we are considering the Node itself as value
# we return true if the value is in graph
def dfsSearch(adj_dic, k):
    seen = set()
    arr = [] # processing the element
    # if we were given a source we could have added that to the seen and started simpler
    # but now we need to use the loop
    for key in adj_dic.keys():
        if key not in seen:
            if dfs(adj_dic, key, seen, arr, k):
                return True
    return False

    #checking if the value K is present
    #return k in arr

def dfs(adj_dic, key, seen, arr, k):
    seen.add(key)
    # processing the elemnt
    if key == k:
        return True

    for nei_node in adj_dic[key]:
        if nei_node not in seen:
            if dfs(adj_dic, nei_node, seen, arr, k):
                return True
            
    #another approach (simpler) can be to build the res and look for k in res


#task3: implement the breadth first Search

#understading the algo: 
# here we dont visit the depth of the graph, we need all the surrouding elemnts of a single node
# we are going to use queue, use the feature of popleft 


def bfsSearch(adj_dic, k):
    queue = deque()
    seen = set()
    

    for key in adj_dic.keys():
        """we only need this outer loop because of
        two reason:
        1. the graph might be disconnected 
        2. and assuming we are not given the first node
        
        if given the first node and graph is connected, we could have append the 
        source to seen set and the queue, and continued with just the while loop
        """
        if key not in seen:
            queue.append(key)
            seen.add(key)
            while queue:
                node = queue.popleft()
                if node == k:
                    return True
                for nei_node in adj_dic[node]:
                    if nei_node not in seen:
                        seen.add(nei_node)
                        queue.append(nei_node)

    return False


#implementing the topological sort
# using depth first search 

"""A very important thing to note here is that 
    what we are trying to achive is that in a 
    u -> v edge relationship, u should always appear before
    v. 
    the intial idea that comes to mind is that in dfs, we first
    recurse down as process nodes as soon as we see them but now 
     we need to find the very last no neighbour existing elemnt
      and then process it  """

# assumption: the graph is disconnected

def dfsTopo(adj_dic, key, seen, stack):
    seen.add(key)
    for nei_node in adj_dic[key]:
        if nei_node not in seen:
            dfsTopo(adj_dic, nei_node, seen, stack)

    stack.append(key)

def topologicalSort(adj_dic):
    seen = set()
    stack =  []

    for key in adj_dic.keys():
        if key not in seen:
            dfsTopo(adj_dic, key, seen, stack)

    return stack[::-1]


# trying to implemment the Topological sort using breath first search 

#initially we have the adj_dic

#algo,

"""
1. we need to give each node an in-degree val: total number of incoming edges to that particular node
2. initial thought is to create a dic with key being the vertx and value being the in degree of that vertx
3. now all the nodes with 0 in degree, add them to the queue and process them(remove them and add to res)
4. now we have processed the node so we update the dic with new in degree val, and we'll get new nodes with 0 in degree
   add them to the queue
5. do this while the queue is not empty
"""

#given to us: adj_dic, assuming no source node given

#so we iterate through each node


queue = deque()
inDegDic = {}

adj_dic = defaultdict()

for u, v in input:
    adj_dic[u].append(v)
    if v not in inDegDic:
        inDegDic[v] = 1
    else:
        inDegDic[v] += 1

#if the adj_list has vertex which has 0 in-deg, that is not included in the inDegDic that
# we created so we will create another for loop to go over all the elemnts in the adj_lis
# and add its value as 0

for key in adj_dic.keys():
    if key not in inDegDic:
        inDegDic[key] = 0

# now the indegdic is ready
for node in inDegDic:
    if inDegDic[node] == 0:
        queue.append(node)

result = []

while queue:
    node = queue.popleft()
    result.append(node)

    for nei in adj_dic[node]:
        inDegDic[nei] -= 1
        if inDegDic[nei] == 0:
            queue.append(nei)

print(result)


# first put all 0 indegree nodes in queue
# pop one
# reduce neighbors
# if neighbor becomes 0, push it