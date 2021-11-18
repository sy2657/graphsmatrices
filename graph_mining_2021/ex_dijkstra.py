# simple example with dijkstra

w1 = create_w_graph([[0,1, 3], [0,2,5], [1,3,2],[2,3,1], [1,4,8], [2,4,6] ], 5)

g1 = Graph(5)
g1.graph = w1

g1.dijkstra(0)
