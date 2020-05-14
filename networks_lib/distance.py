import numpy as np
from collections import deque

## TODO: Implement this function
##
## input:
##   mat (np.array): adjacency matrix for graph
## 
## returns:
##   (np.array): distance matrix
##
## Note: You can assume input matrix is binary, square and symmetric 
##       Your output should be square and symmetric

#Input: Adjacency matrix of size n by n  
#Output: Distance matrix `dist` of size n by n  
#    - For each vertex `u` in the network  
#    - Create boolean array `visited` of length n   
#    - Initialize all vertices u as `visited[u]=False`  
#    - Push tuple `(u, 0)` to a (first-in-first-out) queue `Q`  
#    - While `Q` is not empty:  
#        - Pop tuple `(v,d)` from the top of `Q`  
#        - Set `visited[v]=True`  
#        - Set distance `dist[u,v]=d`  
#        - For each neighbor `w` of `v`  
#            - if `visited[w]=False`, push tuple `(w, d+1)` to `Q`  
            
def bfs_distance(mat):
    num_vertices = mat.shape[0]    
    res = np.full((num_vertices, num_vertices), np.inf)
    deq = deque()
    
    for u in range(num_vertices):
        visited = np.full((num_vertices), False)
        deq.append([u, 0])
        #visted[u] = 1
    
       while len(deq) > 0:
            node = deq.popleft()
            visited[node[0]] = True
            res[u, node[0]] = node[1]
            
            nghbr = np.where(mat[x[0],:]>0)[0]   

            for w in range(len(nghbr)):
                if visited[nghbr[w]] == 0:
                    deq.append((nghbr[w], node[1]+1))
                    visited[nghbr[w]] = 1
            
    return res


## TODO: Implement this function
##
## input:
##   mat (np.array): adjacency matrix for graph
## 
## returns:
##   (list of np.array): list of components
##
## Note: You can assume input matrix is binary, square and symmetric 
##       Your output should be square and symmetric


def get_components(mat):
    dist_mat = bfs_distance(mat)
    num_vertices = mat.shape[0]
    available = [True for _ in range(num_vertices)]

    components = []
    # finish this loop
    while any(available):
        x = []
        u = np.argmax(available)
        for i in range(num_vertices):
            if dist_mat[u, i] < np.inf:
                x.append(i)
            available[u] = False
        if x not in components:
            components.append(x)
        

    
    return components
