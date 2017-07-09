# returns adjacency matrix where entry is number of edges between path of 2 vertices
def pathmat(M):
    s = len(M)
    col=0
    currrow = 0
    hashd= {}
    newpairmat = np.zeros((s+1,s+1))
    while currrow < s-1:
        row = M[currrow,:]
        ind = currrow
        nrow = currrow+1
        ind = ind+1
        ilist = []
        ei = 0
        while ei < s-1:
            ind = ei+1
            if M[ei,currrow]==1:
                
                if M[nrow, ind] == 1:
           # length of current pat
                    ilist.append((nrow, ind))
                    newpairmat[ currrow, nrow] = ind
                    newpairmat[nrow, currrow] = ind
                    nrow = nrow+1 
                    ind=ind+1
            ei=ei+1
        ind1 = currrow-1
        nrow = currrow+1
        #while M[nrow, ind1] == 1:
         #   ilist.appned((nrow, ind1))
          #  newpairmat[currrow,ind1] = nrow
          #  nrow = nrow+1
          #  ind1 = ind1 -1 
        hashd[currrow] = ilist
        currrow = currrow+1 
    return newpairmat
