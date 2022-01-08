# returns new adjacency matrix of Line(G), the vertices of Line(G), and edge list representation of Line(G)

def linegraph(G):
    hashnewVertexoldEdge = {}
    newVertexSet =[]
    ine= 0
    E =[] # edges 
    s = len(G)
    print("s is ", s)
    for r in range(0,s):
        for c in range(0,s):
            if G[r,c]==1 and findinE(E, r,c) ==0:

                E.append([r,c]) # add to edges 
                E.append([c,r])
                newVertexSet.append(ine)
                hashnewVertexoldEdge[ine] = [r,c]
                ine=ine+1
    print("ine is ", ine)
    # num edge is num 1's divided by 2 
    ine = s
    newadjmat = np.zeros((ine,ine))
    new_edge_list = [] # Jan 7, 2022 
    #edges = non empty intersection
    for v in newVertexSet:
        for vv2 in newVertexSet:
            e1 = hashnewVertexoldEdge[v]
            e2 = hashnewVertexoldEdge[vv2]
            # check for intersection
            v1 = e1[0]
            v2 = e1[1]
            v3 = e2[0]
            v4 = e2[1]
            if v1 == v3 or v1 ==v4:
                # add edge
                newadjmat[v,vv2] =1
                newadjmat[vv2,v] =1
                new_edge_list.append((v,vv2))
                new_edge_list.append((vv2, v))
                if v==vv2: # change diagonal to 0
                  newadjmat[v,vv2] = 0
            if v2 ==v3 or v2==v4:
                # add edge 
                newadjmat[v,vv2]=1
                newadjmat[vv2,v]=1
                new_edge_list.append((v,vv2))
                new_edge_list.append((vv2,v))
                if v==vv2:
                  newadjmat[v,vv2] = 0
    return newadjmat, hashnewVertexoldEdge, new_edge_list
