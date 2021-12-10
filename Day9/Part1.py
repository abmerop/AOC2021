import sys
import numpy as np


def read_input(input_file):
    """
    read_input reads a "map" from input_file contain a digit 0-9 representing a
               height and returns a numpy ndarray. There are no spaces between
               digits.

    :param input_file: path to the map file to read
    :return: a numpy ndarray with the heights in the file
    """

    lines = open(input_file, 'r').readlines()
    height_map = np.genfromtxt(lines, delimiter=1).astype(int)
    
    return height_map


def local_mins(row, val):
    """
    local_mins iterates over a numpy array representing a single row in an
               ndarray and returns a new array consisting of elements which
               are smaller than both neighbors and the input value 'val'
               otherwise.
               
    :param row: a numpy array representing a row in a height map
    :param val: value to set element which are NOT smaller than both neighbors
    :return: a list equal to input row but with non-local minimums set to 'val'
    """

    out_row = [val] * len(row)

    # Handle inners
    for elem_idx in range(1, len(row)-1):
        if row[elem_idx] < row[elem_idx-1] and row[elem_idx] < row[elem_idx+1]:
            out_row[elem_idx] = row[elem_idx]

    # Handle edges
    out_row[0] = row[0] if row[0] < row[1] else val
    out_row[len(row)-1] = row[len(row)-1] if row[len(row)-1] < row[len(row)-2] else val

    return out_row


def find_mins(height_map):
    """
    find_mins finds all local minimums in a height map. The approach is to find local
              minimums in a row of a numpy ndarray, then transpose the height map and
              repeat the process. Elements which are the same in both cases are the
              local minimums.
              
    :param height_map: a numpy ndarray of ints representing heights in a 2d map
    :return: a pair of numpy arrays with the x and y coordinates of local minimums in
             the height map, respectively.
    """

    # Important: use .copy() as otherwise it is a reference to height_map
    transpose_map = np.transpose(height_map).copy()

    # We use a different value for the second argument of local_mins so that when
    # subtracted the values do not equal zero.
    for row_idx, row in enumerate(height_map):
        height_map[row_idx] = local_mins(row, -1)

    for row_idx, row in enumerate(transpose_map):
        transpose_map[row_idx] = local_mins(row, -3)

    diff_map = height_map - np.transpose(transpose_map)
    return np.where(diff_map == 0)


def evaluate_risk(height_map, mins):
    """
    evaluate_risk sums the values of all local minimums + 1 in a height map
    
    :param height_map: the height map read from read_input
    :param mins: the local minimums in the height map from find_mins
    :return: the sum of all local minimums + 1
    """

    risk_level = 0
    for x, y in zip(mins[0], mins[1]):
        risk_level += height_map[x][y] + 1

    return risk_level


if __name__ == "__main__":
    height_map = read_input(sys.argv[1])
    mins = find_mins(height_map)
    print("Solution:", evaluate_risk(height_map, mins))
