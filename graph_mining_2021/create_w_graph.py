# create weighted graph

# sample input create_w_graph([[0,1, w_1],[1,2, w_2],[2,3, w_3],[0,3, w_4]], n_vertices)

def create_w_graph(edgelist, n_vertices):
    #n_vertices = np.max(edgelist)+1
    # create adjacency matrix
    adj_mat = np.zeros((n_vertices, n_vertices))
    
    for e1, e2, w in edgelist:
        adj_mat[e1][e2] = w
        adj_mat[e2][e1] = w

    
    return adj_mat
    
