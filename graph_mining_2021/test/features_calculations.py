# features: max clique size
# touching number
# max degree
# degree distn 
max_clique_sizes = []

touching_numbers = []


# clique_sizes = []


all_cliques = nx.enumerate_all_cliques(g)

clique_sizes = [len(x) for x in all_cliques]

max_clique_size = max(clique_sizes)

deg_dist = []

for row in adj_mat:
    rsum = sum(row)
    deg_dist.append(rsum)

max_deg = max(deg_dist)
