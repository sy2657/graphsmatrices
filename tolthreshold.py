import numpy as np 
def tolthreshold(n):
# create adj matrix of size n
    newmat = np.zeros((n,n))
# range for a_i is in [1,2]
# range for t_i is in [0,1]
    a = []
    t = []
    t = np.random.rand(n,1)
    for i in range(1,n):
# assign values to a_i and t_i
     # look at min of a_i
        m = t[i]
        a.append(m+1)
    # check condition and add edges 
    for i in range(1,n):
        for j in range(1,n):
            ai = a[i]
            aj = a[j]
            ti = t[i]
            tj = t[j]
            if (ai+aj) >= min(ti,tj):
                # add edge i and j
                newmat[i,j]=1
                newmat[j,i]=1
    return a, t, newmat
