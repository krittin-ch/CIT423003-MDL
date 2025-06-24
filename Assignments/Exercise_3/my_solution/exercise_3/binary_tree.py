import numpy as np
from sinusoidal_positional_encodings import PE_generator
import math 

def attn_bfs_generator(bfs_tree, d_model):
    n = bfs_tree.size
    m_pe = np.zeros((n, d_model))

    depth_pos = np.concatenate([np.full(2**i, i) for i in range(math.ceil(math.log2(n)) + 1)])
    depth_pos = depth_pos[:n]

    offset_pos = np.concatenate([np.arange(2**i) for i in range(math.ceil(math.log2(n)) + 1)])
    offset_pos = offset_pos[:n]

    for i in range(d_model):
        m_pe[:, i] = PE_generator(depth_pos, i, d_model) + PE_generator(offset_pos, i, d_model)
        
    return m_pe


bfs_tree = np.array([1, 2, 3, 4, 5, 6, 7])

m_pe = attn_bfs_generator(bfs_tree, 4)

print("Binary Tree (BFS) with Sinusoidal Positinal Encodings: ")
print(m_pe)