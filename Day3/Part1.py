import sys
import numpy as np
from scipy import stats

# Read input using 1 character as delimiter into numpy ndarray (dtype is float)
matr = np.genfromtxt(sys.argv[1], delimiter=1)
# This performs a column-wise mode on the ndarray
mode = stats.mode(matr)
# Join the numbers in the mode list by converting each float to int then str and concatenate
gamma = int("".join(str(int(i)) for i in mode[0][0]), 2)
# Repeat with abs(mode - 1). Since it is a array of binary values 0 -> -1 and 1 -> 0
epsilon = int("".join(str(int(i)) for i in abs(mode[0][0]-1)), 2)
print("Answer:", gamma * epsilon)