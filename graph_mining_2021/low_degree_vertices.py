# find all degrees <= 2 
ind= 0
degrees_less_equal2 = []
for val in sorted_list:
  vertex = sorted_index[ind]
  ind= ind+1
  if val <=2:
    # add 
    degrees_less_equal2.append(vertex)
  if val >2:
    break
 
# delete the rows/ columns with degree at most 2 or 1 -> change to all zeros (?) 
ind=0
for row in adj_matrix:
  if ind in degrees_less_equal2:
    adj_matrix[ind] = np.zeros(n)
  ind=ind+1
