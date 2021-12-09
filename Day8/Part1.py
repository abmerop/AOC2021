import sys
import numpy as np


def read_input(input_file):
    """
    read_input reads the input file and returns a list of inputs and outputs

    :param input_file: path to file with format "<inputs> | <outputs>"
    :return: a tuple of lists with inputs and outputs
    """

    # TODO - Should look into more compact ways to read inputs
    lines = open(input_file, "r").readlines()
    
    inputs = []
    outputs = []
    for line in lines:
        inputs.append(line.strip().split(' | ')[0])
        outputs.append(line.strip().split(' | ')[1])

    return (inputs, outputs)

def count_unique_seqments(outputs):
    """
    count_unique_segments counts the number of 1, 4, 7, or 8 digits in a display.
                          These are unique in the sense that no other digit has
                          the same number of segments illuminated.

    :param outputs: list of output segment strings
    :return: the number of unique segments
    """

    count = 0
    for output in outputs:
        str_lens = np.asarray([len(s) for s in output.split(' ')])
        uniques = np.asarray([2,4,3,7])

        # isin returns a boolean array... a bit odd to sum bools but it works
        count += np.sum(np.isin(str_lens, uniques))

    return count

if __name__ == "__main__":
    _, outputs = read_input(sys.argv[1])
    print("Solution:", count_unique_seqments(outputs))