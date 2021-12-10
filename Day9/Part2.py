import sys
import numpy as np
import Part1


# Note: this is not very optimized since I ran out of time today.

def count_basin(row, col, basin_map, marked_map):
    """
    count_basin takes a starting coordinate, representing a local minimum, and expands in all
                directions until the value 9 is reached. If the neighboring element is not 9,
                marked_map is set to 1 at that coordinate. This is a recursive functions but
                does not need to be. The output of this function is the marked_map.
                
    :param row: x coordinate of local minimum
    :param col: y coordinate of local minimum
    :param basin_map: same as height map read from read_input
    :param marked_map: a boolean matrix the same dimensions as basin_map
    """

    # Count to left
    if col-1 >= 0 and not marked_map[row][col-1] and basin_map[row][col-1] != 9:
        marked_map[row][col-1] = 1
        count_basin(row, col-1, basin_map, marked_map)

    # Count right
    if col+1 < len(basin_map[0]) and not marked_map[row][col+1] and basin_map[row][col+1] != 9:
        marked_map[row][col+1] = 1
        count_basin(row, col+1, basin_map, marked_map)

    # Count above
    if row-1 >= 0 and not marked_map[row-1][col] and basin_map[row-1][col] != 9:
        marked_map[row-1][col] = 1
        count_basin(row-1, col, basin_map, marked_map)
    
    # Count below
    if row+1 < len(basin_map) and not marked_map[row+1][col] and basin_map[row+1][col] != 9:
        marked_map[row+1][col] = 1
        count_basin(row+1, col, basin_map, marked_map)


def largest_basins(basin_map, mins):
    """
    largest_basins find all basins in a basin_map and returns the product of the largest 3.
                   A basin is the set of all coordinates neighboring a local minimum or one
                   of it's neighbor's neighbors that does not include the value 9.
    
    :param basin_map: same as height map from read_input
    :param mins: the minimums found from find_mins
    :return: the product of the largest 3 basins
    """

    basin_sizes = []
    # Check all basins starting at local minimums
    for x, y in zip(mins[0], mins[1]):
        # We need a clean marked_map for each local minimum
        marked_map = np.zeros([len(basin_map), len(height_map[0])]).astype(int)
        count_basin(x, y, basin_map, marked_map)

        # The size is the number of non-zero elements in the marked_map
        basin_size = np.sum(marked_map)
        basin_sizes.append(basin_size)

    largest_basins = sorted(basin_sizes)[-3:]
    result = 1
    for idx in range(len(largest_basins)):
        result = result * largest_basins[idx]

    return result


if __name__ == "__main__":
    # Reuse read_input and find_mins from part 1
    height_map = Part1.read_input(sys.argv[1])
    basin_map = height_map.copy()
    mins = Part1.find_mins(height_map)
    print("Solution:", largest_basins(basin_map, mins))