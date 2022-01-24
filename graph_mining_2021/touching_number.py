cycle_basis = nx.cycle_basis(g, 0) # 0 is root

# touching number of cycles in the cycle basis

# https://networkx.org/documentation/stable/_modules/networkx/algorithms/cycles.html

touching_num = 0
touching_edges = []

for cycle in cycle_basis:
    # look up edges with vertices from cycle
    for v in cycle:
        v_row = adj_mat[v]
        output = [idx for idx, element in enumerate(v_row) if element ==1]
        for edge_vertex in output:
            if edge_vertex in cycle:
                # do not add
            else:
                # add
                touching_edges.append((v, edge_vertex))
                touching_num = touching_num + 1
                
                
