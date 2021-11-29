import networkx as nx
g = nx.Graph()

g.add_nodes_from([0,1,2, 3,4,5])

g.add_edges_from([(1, 2), (1, 3), (2,3), (4,5), (1,4)])

# quotient graph , by triangles

# https://networkx.org/documentation/stable/tutorial.html

# https://www.kite.com/python/docs/networkx.quotient_graph

all_cliques= nx.enumerate_all_cliques(g)

triad_cliques=[x for x in all_cliques if len(x)==3 ]

is_triangle = triad_cliques

Q = nx.quotient_graph(g, is_triangle)
