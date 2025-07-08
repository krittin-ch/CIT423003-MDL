import numpy as np 
from sinusoidal_positional_encodings import PE_generator
import math

def pos_img_patch(r, c, d_model):
    n = r*c
    m_pe = np.zeros((n, d_model))

    row_pos = np.concatenate([np.arange(r) for i in range(c)])
    print(row_pos)
    row_pos = row_pos[:n]

    col_pos = np.concatenate([np.arange(c) for i in range(r)])
    print(col_pos)
    col_pos = col_pos[:n]

    for i in range(d_model):
        m_pe[:, i] = PE_generator(row_pos, i, d_model) + PE_generator(col_pos, i, d_model)

    return m_pe

m_pe = pos_img_patch(3, 2, 4)

print("2-D Grid Image Patch with Sinusoidal Positinal Encodings: ")
print(m_pe)