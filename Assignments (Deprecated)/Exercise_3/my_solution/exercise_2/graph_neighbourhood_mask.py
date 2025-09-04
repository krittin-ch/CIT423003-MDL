import numpy as np 

# Each node to attend only to itself and its direct neighbors in the graph.

def attn_mask_generator(A: np.ndarray):
    m, n = A.shape
    assert m == n, "Adjency matrix should be square"

    return A.copy() + np.eye(m)    


A = np.array([
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 1, 0, 1, 0]
])

M_graph = attn_mask_generator(A)

print("The Additive Attention Mask: ")
print(M_graph)