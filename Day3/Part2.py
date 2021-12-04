import sys
import numpy as np
from scipy import stats

# Read input using 1 character as delimiter into numpy ndarray (dtype is float)
matr = np.genfromtxt(sys.argv[1], delimiter=1)
o2_matr = matr
co2_matr = matr

for bit_pos in range(o2_matr.shape[1]):
    # Find most common value in bit position
    o2_mode = stats.mode(o2_matr)
    most_common = o2_mode[0][0][bit_pos]

    # Handle special case with equal number of 0s and 1s
    if not o2_matr.shape[0] % 2: # Can only happen with even number of rows
        sums = o2_matr.sum(axis=0)
        if sums[bit_pos] == o2_matr.shape[0] // 2:
            most_common = 1.0

    o2_mask = o2_matr[:, bit_pos] == most_common
    o2_matr = o2_matr[o2_mask, :]

    # If there is only one number (row) left, stop
    if o2_matr.shape[0] == 1:
        break

# Use same approach from part 1 to convert array to number
o2_rating = int("".join(str(int(i)) for i in o2_matr[0]), 2)

for bit_pos in range(co2_matr.shape[1]):
    # Find most common value in bit position
    co2_mode = stats.mode(co2_matr)
    least_common = abs(co2_mode[0][0][bit_pos] - 1.0)

    # Handle special case with equal number of 0s and 1s
    if not co2_matr.shape[0] % 2:
        sums = co2_matr.sum(axis=0)
        if sums[bit_pos] == co2_matr.shape[0] // 2:
            least_common = 0.0

    co2_mask = co2_matr[:, bit_pos] == least_common
    co2_matr = co2_matr[co2_mask, :]

    # If there is only one number left, stop
    if co2_matr.shape[0] == 1:
        break


# Use same approach from part 1 to convert array to number
co2_rating = int("".join(str(int(i)) for i in co2_matr[0]), 2)

print("Answer:", o2_rating * co2_rating)