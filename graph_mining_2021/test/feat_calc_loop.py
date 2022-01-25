# input : nx graph collection g_db2

touching_numbers = []

max_clique_sizes = []

mean_clique_sizes= []

deg_dists= []

max_degs = []

for i in range(len(g_db2)):
    g = g_db2[i]
    
    all_cliques = nx.enumerate_all_cliques(g)

    clique_sizes = [len(x) for x in all_cliques]

    max_clique_size = max(clique_sizes)
    # mean clique size
    mean_clique_size = np.mean(clique_sizes)
    
    max_clique_sizes.append(max_clique_size)
    mean_clique_sizes.append(mean_clique_size)
    
    deg_dist = []

    for row in adj_mat:
        rsum = sum(row)
        deg_dist.append(rsum)

    deg_dists.append(deg_dist)
    
    max_deg = max(deg_dist)
    
    max_degs.append(max_deg)
    
    #tn = touching_num(g)
    
    #touching_numbers.append(tn)
