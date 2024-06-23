import numpy as np

# Coefficients of the polynomial
coeff = [3, -5, -3, 0, -7, -10]

# Compute the roots
roots = np.roots(coeff)

# Filter out only real roots
real_roots = [root for root in roots if np.isreal(root)]

# Print the real roots
print(real_roots)