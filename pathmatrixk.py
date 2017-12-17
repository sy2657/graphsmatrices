
def pathmatrixk(m,k):
    n=len(m)
    powersdictionary= {}
    
    prevm= m 
    powersdictionary[1]= m
    for i in range(2,k):
        prevm= np.matmul(prevm,m)
        powersdictionary[i]= prevm

    pathmatk = np.zeros((n,n))
    for kk in range(1,k):
        kpow = powersdictionary[kk]
        for i in range(0,n-1):
            for j in range(0,n-1):
                if i==j:
                    continue
                if pathmatk[i,j]==0: # check if there already exists path
                    if kpow[i,j]>0:
                        #print('kpow',kpow[i,j])
                        pathmatk[i,j]= kk
                    
    return pathmatk 
