import numpy as np

def PE_generator(pos, j, d_model):
    i = j // 2

    val = pos/(10000**(2*i/d_model))

    if j % 2 == 0:
        return np.sin(val)
    
    return np.cos(val)