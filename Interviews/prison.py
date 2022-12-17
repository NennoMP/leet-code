# Goldman Sachs 2021

def prison(n, m, h, v):

    # Base case
    if len(h) == 0 and len(v) == 0:
        return 1
    
    h_vector = [1 for _ in range(n)] # horizontal vector
    v_vector = [1 for _ in range(m)] # vertical vector
    # Cell -> Bar (0: bar present, 1: bar removed)
    for he in h:
        h_vector[he-1] = 0
    for ve in v:
        v_vector[ve-1] = 0
        
    # Count number of contiguous horizontal cells
    h_cont = 1
    h_max = 1
    for i, he in enumerate(h_vector):
        if he == 1:
            h_cont = 1
        else:
            h_cont += 1
        h_max = max(h_cont, h_max)

    # Count number of contiguous vertical cells
    v_cont = 1
    v_max = 1
    for j, ve in enumerate(v_vector):
        if ve == 1:
            v_cont = 1
        else:
            v_cont += 1
        v_max = max(v_cont, v_max)
  
    return h_max * v_max
