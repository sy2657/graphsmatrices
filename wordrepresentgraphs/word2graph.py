import numpy as np
def word2graph(wd, n): # n number of vertices
    
    ln = len(wd)

    wmat = np.zeros(shape=(ln,ln))
    clist=[]

    bv = (ln+1)*[0]
    print ln
    ind =0
    while ind < ln:
        wl = int(wd[ind])
    
        bv[wl] = bv[wl]+1
        print wl
    
        if bv[wl]==1:
            clist.append(wl)
    
        if bv[wl]==2:# stop adding to dictionary# remove from list
            clist.remove(wl)
        for nc in clist:# add edge from nc to wl 
            print 'adding edge from', nc, wl
            wmat[nc,wl] =1.0
            wmat[wl,nc] =1.0
        ind = ind+1
    
    return wmat
