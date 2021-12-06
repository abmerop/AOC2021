import sys
import numpy as np


def simulate_fish(input_file, num_days):
    """
    simulate_fish simulate laternfish... replication... for num_days

    :param input_file: initial state of fish ages to read
    :param num_days: number of days to simulate fish population
    :return: the number of fish after num_days
    """

    inp = open(input_file, 'r')
    lines = inp.readlines()

    # There is only one line in the input seperate by commas
    initial_state = [int(x) for x in lines[0].split(',')]
    state = np.array(initial_state)

    for day in range(num_days):
        # Just subtract everything by one first
        state -= 1

        # Anything that was previously 0 in the previous day will now be -1.
        # Reset those to 6 and add an equal number of new fish by appending 8s
        if np.sum(state == -1) > 0:
            num_new_fish = np.sum(state == -1)
            state[np.where(state == -1)] = 6

            # Python trick: multiply list by an int to duplicate it that many times
            state = np.hstack([state, [8] * num_new_fish])
        
        # Print details here (optionally)
        print("After Day {}: {}".format(day+1, state))

    return state.size

if __name__ == "__main__":
    print("Solution:", simulate_fish(sys.argv[1], 80))