import sys
import numpy as np


# For part 2 we'll use the same function check_all_positions but modify check_position
# to account for the non-constant fuel burn.
def check_position(position, position_list):
    """
    check_position determines the amount of fuel needed to move all crabs from
                   their position in position_list to position

    :param position: the position to move all crabs to
    :param position_list: the current position of all crabs as numpy ndarray
    :return: the amount of fuel consumed for this move
    """

    # We still need the distance moved in total
    distance_list = abs(position_list - position)

    # To calculate fuel we need to sum from 1 to distance. This is simply:
    #    (distance/2)*(distance+1)
    # when the first step is 1
    fuel_list = (distance_list / 2) * (distance_list + 1)
    return np.sum(fuel_list)

def check_all_positions(input_file):
    """
    check_all_positions reads input from input_file, determines the range of
                        positions, then calls check_position for each possible
                        position value

    :param input_file: path to file with comma delimited starting position values
    :return: the minimum fuel used
    """

    lines = open(input_file, 'r').readlines()
    initial_positions = np.array([int(x) for x in lines[0].split(',')])

    # Note: in C++ i'd use std::numeric_limits<uint64_t>::max() but this works here
    min_fuel = 9999999999999999
    for position in range(np.min(initial_positions), np.max(initial_positions)):
        fuel = check_position(position, initial_positions)
        min_fuel = fuel if fuel < min_fuel else min_fuel

    return min_fuel

if __name__ == "__main__":
    print("Solution:", check_all_positions(sys.argv[1]))