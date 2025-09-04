import numpy as np 
import math

'''
      0        
  1      2     
3   4  5   6   

L = 2 * P + 1
R = 2 * P + 2

Hence, P = floor((idx - 1)/2)
'''

def BFS_maskgen(n=7):
    M = np.zeros((n, n))

    for i in range(n):
        M[i, i] = 1 # always attend to itself

        parent = math.floor((i - 1)/2)
        if parent >= 0:
            M[i, parent] = 1

        left_child = 2*i + 1
        if left_child < n:
            M[i, left_child] = 1
        
        right_child = 2*i + 2
        if right_child < n:
            M[i, right_child] = 1

    return M


M = BFS_maskgen(7)

print("Binary Tree Mask (BFS): ")
print(M)