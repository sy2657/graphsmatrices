# input example : create_graph([[1,2], [0,3] ])
def create_graph(edgelist): # vertices from 0 to n-1 
   
    graph = {}
    n_vertices = np.max(edgelist)+1
    # create adjacency matrix
    adj_mat = np.zeros((n_vertices, n_vertices))
    

    for e1, e2 in edgelist:
        graph.setdefault(e1, []).append(e2)
        graph.setdefault(e2, []).append(e1)
        adj_mat[e1][e2] = 1
        adj_mat[e2][e1] = 1

    
    return adj_mat #graph
