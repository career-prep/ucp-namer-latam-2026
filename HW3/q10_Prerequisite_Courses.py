"""
idea: 
    course= node
    pre= edge
    use kahn algo since we want a topological order


"""

from collections import deque, defaultdict

def course_order(courses, pres): #pres= prerequisite
    
    #init the indegree
    in_degree={}
    for course in courses:
        in_degree[course]=0
    
    #adj list
    graph= defaultdict(list)

    for course in pres:
        pre_list= pres[course]

        for pre in pre_list:
            #for graph
            graph[pre].append(course)

            #for indegree
            in_degree[course]+=1
    
    #kahn algo, add course with indegree=0 to queue
    queue=deque()
    for course in in_degree:
        if in_degree[course]==0:
            queue.append(course)
    
    topo_order=[]

    while queue:
        node= queue.popleft()
        topo_order.append(node)

        #check all neighbor and decrease the indegree
        for neighbor in graph[node]:
            in_degree[neighbor]-=1

            #if the neighbor have indegree=0 => add to queue to do kahn algo
            if in_degree[neighbor]==0:
                queue.append(neighbor)
            
    
    if len(topo_order)==len(courses):
        return topo_order
    else:
        return []






    
