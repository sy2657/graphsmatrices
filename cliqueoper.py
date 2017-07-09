# now write clique intersection operator 
def cliqueoper(G):
    isize =3 # initial size 
    msize = len(G) # maxsize
    nwadmat = np.zeros((msize,msize))
    ifor =0
    icdic = {}
    for ifor in range(isize,msize):
        # intersect cliques
        # record size of intersected cliques 
        if ifor>=3:
            kclique_current =nx.k_clique_communities(G,ifor)
            if kclique_current:
                print kclique_current
                #print len(kclique_current)
                listi = list(kclique_current)
                lisi = [] # list of lists of sets in clique 
                ind= 0
                for i in listi:
                    fs = listi[ind]
                    listj = []
                    for j in fs:
                        listj.append[j]
                    ind=ind+1
                    lisi.append[listj]
                icdic[ifor] = lisi
        # intersect with previous lists 
        if ifor>=3:
            for j in range(isize, ifor):
            # find matching vertices 
                lisj = icdic[j]
            # match sets of each with each 
                for lj in lisj:
                    elj = lisj[lj]
                    for li in lisi:
                        eli = lisi[li]
                        intersect = matchlists(elj, eli)
                    # find the size smallest intersection >=3 and record 
                        if matchlistslen(elj, eli) >2 :
                        # add to new ad mat 
                            nwadmat[elj,eli] =1
                            nwadmat[eli,elj] =1
                        
    return nwadmat 
