import numpy as np 

x = np.array([2.7, 3.1, 9.4, 6.5, 4.2, 3.8])

# (a) Apply min-max normalization
x_min = np.min(x)
x_max = np.max(x)
x_norm = (x - x_min) / (x_max - x_min)

print("Normzlized Data: ", x_norm)

# (b) Apply z-score standardization
x_mean = np.average(x)
x_std = np.std(x)
x_z = (x - x_mean) / x_std

print("Standardized Data: ", x_z)