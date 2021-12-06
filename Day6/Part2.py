import sys
import numpy as np


def simulate_fish(input_file, num_days):
    """
    simulate_fish simulate laternfish... replication... for num_days. The previous
                  implementation suffers from serious memory issues. Rather than
                  keeping an array with each fish's timer, we instead have an array
                  which counts the number of fish which are at that timer value.

    :param input_file: initial state of fish ages to read
    :param num_days: number of days to simulate fish population
    :return: the number of fish after num_days
    """

    inp = open(input_file, 'r')
    lines = inp.readlines()

    # Leveraging numpy array for easy query of values initially
    initial_state = np.array([int(x) for x in lines[0].split(',')])

    # Timer values range from -1 to 8 here
    state = [0] * 10
    for timer_val in range(7): # Input can only go to 6
        num_vals = np.sum(initial_state == timer_val)
        state[timer_val+1] = num_vals

    for day in range(num_days):
        # For each day "subtract" timer by shifting the array left
        # Append a zero for the right-most value
        state = state[1:] + [0]

        # Index 0 represents -1, or fish that were 0 in the last day. Create this
        # many new fish (timer 8, index 9) and "fish on cooldown" (timer 6, index 7)
        if state[0] > 0:
            num_new_fish = state[0]
            state[9] = num_new_fish
            state[7] += num_new_fish

            # The shift will naturally pop this off, but clear it clear so we can get
            # accurate intermediate counts for testing.
            state[0] = 0

        print("After day {} the total number of fish is {}".format(day+1, np.sum(state)))

    return np.sum(state)

if __name__ == "__main__":
    print("Solution:", simulate_fish(sys.argv[1], 256))
