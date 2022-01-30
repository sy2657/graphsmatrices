# touching number given n-cycle
def touching_num_n(g, n):
    cycle_basis = nx.cycle_basis(g, 0)
    touching_num = 0
    touching_edges = []
    
def touching_num(g):
    cycle_basis = nx.cycle_basis(g, 0)
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
                    pass
                else:
                    # add
                    touching_edges.append((v, edge_vertex))
                    touching_num = touching_num + 1
    return touching_num
