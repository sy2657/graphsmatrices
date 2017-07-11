from random import randint
# generates adjacency matrix for n possible vertices, a random tree
def treegenerate(n):
# print(randint(0, 9))

# generate tree by random paths, from root to leaf
    ilist = [1]
    newadmat = np.zeros((n,n))
#input size of tree's vertices

# generate number of random paths to add together
    num = int(10*np.random.rand())
# first generate random length of path  from 1 to 10
    for i in range(0, num):
        pathnum = randint(1,10)
        cur = ilist[-1]
        if cur == n:
            break
        randind = randint(1,cur)
     # add connection for the edge and the others
        newadmat[randind, cur+1] = 1
        newadmat[cur+1, randind] = 1
        for j in range(1,pathnum-1):
            ilist.append(cur + j)
            newadmat[cur+j-1, cur+j] = 1 # add edge for this path
            newadmat[cur+j, cur+j-1] = 1
        cur = cur + pathnum
        
    return newadmat
