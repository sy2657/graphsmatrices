import numpy as np
def listpairs2adjacencymatrix(listpairs, nvertices):
    s = [nvertices+1,nvertices+1]
    newamat = np.zeros(s)
    le = len(listpairs)
    il =0
    while il<le:
        print il
        p1 = listpairs[il][0]
        p2 = listpairs[il][1]
        newamat[p1,p2] =1
        newamat[p2, p1]=1
        il=il+1
    newamat = newamat[1:,1:]
    return newamat
