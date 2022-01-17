# time series -> vis. graph (temporal preserved)

# input: mat 
# the time series turned into -> graph

# for t_c, yc with t_a < t_c < t_b, 
# y_c < y_b + (y_a - y_b) [ (t_b - t_c) / (t_b - t_a )]

mat = sham_mat

n_ver = len(mat)

"""for row in mat:
    t_row = row[0]
    val_row = row[1]"""
    

edges = []  # input to networkx graph

# adj mat input
adj_mat = np.zeros((n_ver, n_ver))

# faster way to check

total_len = len(mat)
# fix y_a first 

for ind_a in range(0, total_len):
    row_a = mat[ind_a]
    t_a = row_a[0]
    val_a = row_a[1]
    
    # iterate over y_b
    for ind_b in range(2, total_len):
        row_b = mat[ind_b]
        
        t_b = row_b[0]
        val_b = row_b[1]
        
        bool_c = True
        
        for ind_c in range(1, ind_b):
            row_c = mat[ind_c]
            
            t_c = row_c[0]
            val_c = row_c[1]
            
            # check if indices are equal; check if t_a < t_c < t_b
            
            if not t_a < t_c < t_b:
                continue
            
            if val_c < val_b and (val_a - val_b) > 0:
                # add edge
                edges.append((t_a, t_b))
                edges.append((t_b, t_a))
                
                adj_mat[t_a, t_b] =1
                adj_mat[t_b, t_a]= 1
                
            else:
                # check condition
                if val_c < val_b + (val_a - val_b)*(t_b - t_c)/(t_b -t_a):
                    edges.append((t_a, t_b))
                    edges.append((t_b, t_a))
                    
                    adj_mat[t_a, t_b] =1
                    adj_mat[t_b, t_a]= 1
                
        
