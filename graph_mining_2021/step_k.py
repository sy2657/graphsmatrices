# Step_k graph of G 

def step_k(G, k):
    #  take k-th power and check for entry in coluumn
    matpow = adj_mat
    for i in range(k):
        matpow = np.matmul(matpow, adj_mat)
    # return this matpow with nonzero entries equal 1 
    matpow1 = np.array(np.where(matpow > 0, 1, 0))
    
    # edge list 
    edge_list = []
    edge1= 0
    for row in matpow:
        # check entries equal 1
        res = [idx for idx, val in enumerate(row) if val != 0]
        for r in res:
            edge_list.append((edge1, r))
            edge_list.append((r, edge1))
        edge1 = edge1+ 1
    
    return edge_list, matpow1
