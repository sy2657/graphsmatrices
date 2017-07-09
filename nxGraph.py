import networkx as nx
# add edges from edge list 
def nxGraph(listoflists):
    G=nx.Graph()
    il=0
    le = len(listoflists)
    while il<le:
        p1 = listoflists[il][0]
        p2 = listoflists[il][1]
        G.add_edge(p1,p2)
        il =il+1
    
    # find cliques
    
    return G
