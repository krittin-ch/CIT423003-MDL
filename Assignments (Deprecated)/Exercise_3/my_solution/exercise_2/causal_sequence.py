import numpy as np 

n = 8
k = 3
M = np.zeros((n, n))

for i in range(n):
    if k <= i:
        M[i, k] = 1

print("8x8 Binary Causal Mask: ")
print(M)

M = np.zeros((n, n))

for i in range(n):
    for k in range(n):
        if k <= i:
            M[i, k] = 1

print("Closed-Form Expression: ")
print(M)