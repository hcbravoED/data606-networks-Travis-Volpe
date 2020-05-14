import numpy as np
import random
from random import randint
from random import seed

## TODO: Implement this function
##
## Input:
##  - dmat (np.array): symmetric array of distances
##  - K (int): Number of clusters
##
## Output:
##   (np.array): initialize by choosing random number of points as medioids


def random_init(dmat, K):
    num_vertices = dmat.shape[0]
    medioids = np.array(random.sample(range(0, num_vertices), K))
    return medioids


## TODO: Implement this function
##
## Input:
##   - dmat (np.array): symmetric array of distances
##   - medioids (np.array): indices of current medioids
##
## Output:
##   - (np.array): assignment of each point to nearest medioid

def assign(dmat, medioids):
    num_vertices = dmat.shape[0]
    num_clusters = len(medioids)
    assignment = np.zeros((num_vertices))
    
    for m in range(len(medioids)):
        medioids[m] = int(medioids[m])
    
    for i in range(num_vertices):
        dist = sorted([(dmat[i][m], m) for m in medioids])
        assignment[i] = dist[0][1]

    return assignment


## TODO: Implement this function
##
## Input:
##   - dmat (np.array): symmetric array of distances
##   - assignment (np.array): cluster assignment for each point
##   - K (int): number of clusters
##
## Output:
##   (np.array): indices of selected medioids
def get_medioids(dmat, assignment, K):
    medioid = np.zeros(K)
    
    for i in range(K):
        index = np.where(assignment == i)
        index = np.array(index)
        med = dmat[index, index.transpose()]
        sums = med.sum(axis = 0)
        med_min = np.argmin(sums)
        medioid[i] = index[0, med_min]
    return medioid

## TODO: Finish implementing this function
##
## Input:
##   - dmat (np.array): symmetric array of distances
##   - K (int): number of clusters
##   - niter (int): maximum number of iterations
##
## Output:
##   - (np.array): assignment of each point to cluster
def kmedioids(dmat, K, niter=10):
    num_vertices = dmat.shape[0]
    
    # we're checking for convergence by seeing if medioids
    # don't change so set some value to compare to
    old_mediods = np.full((K), np.inf, dtype=np.int)
    medioids = random_init(dmat, K)
    
    # this is here to define the variable before the loop
    assignment = np.full((num_vertices), np.inf)
   
    it = 0
    while np.any(old_mediods != medioids) and it < niter:
        it += 1
        old_medioids = medioids
        
        # finish implementing this section
        assignment = assign(dmat, medioids)
        medioids = get_medioids(dmat, assignment, K)

    return assignment


