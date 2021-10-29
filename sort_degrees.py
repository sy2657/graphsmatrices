# order the vertices in terms of degree (increasing order)

vertex_degrees = []
# input: adjacency matrix
for row in adj_matrix:
  # sum number of 1's
  sum_current = np.sum(row)
  vertex_degrees.append(sum_current)
 
import numpy as np
sorted_index = np.argsort(vertex_degrees)
sorted_list = np.sort(vertex_degrees)
