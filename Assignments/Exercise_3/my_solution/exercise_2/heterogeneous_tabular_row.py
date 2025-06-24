import numpy as np

# Heterogeneous Tabular Row
def HTR_maskgen(n, c):
    d = 1 + n + c
    M = np.zeros((d, d))

    M[0, :] = 1 # CLS attends to all tokens
    M[:, 0] = 1 # all tokens attend to CLS

    M[1:n+1, 1:n+1] = 1 # all x_i^num attend to each other
    M[n+1:, n+1:] = 1 # all x_i^cat attend to each other

    return M 

n = 1
c = 2

M = HTR_maskgen(n, c)

print("Heterogeneous Tabular Row: ")
print(M)
