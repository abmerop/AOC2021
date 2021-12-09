import sys
import Part1
import numpy as np


def deduce_segments(inputs, outputs):
    """
    deduce_segments deduces the value of each string in outputs given the
                    strings in input
    :param inputs: list of space delimited string of inputs
    :param outputs: list of space delimited string of outputs
    :return: sum of the deduced output strings
    """

    running_sum = 0

    # For each input, deduce string -> digit mappings and apply to output
    assert(len(inputs) == len(outputs))
    for input_idx in range(len(inputs)):

        # Merge input and output
        merged_str = inputs[input_idx] #+ " " + outputs[input_idx]
        input_strs = merged_str.split(' ')

        # Keep track of the set of characters for uniques
        str_lens = np.asarray([len(s) for s in input_strs])

        one_str = input_strs[np.where(str_lens == 2)[0][0]]
        one_set = set([c for c in one_str])

        four_str = input_strs[np.where(str_lens == 4)[0][0]]
        four_set = set([c for c in four_str])

        seven_str = input_strs[np.where(str_lens == 3)[0][0]]
        seven_set = set([c for c in seven_str])

        eight_str = input_strs[np.where(str_lens == 7)[0][0]]
        eight_set = set([c for c in eight_str])

        # Use this to find 2s
        two_search = eight_set.difference(four_set)

        digit_str = ""
        for output in outputs[input_idx].split(' '):
            # Numbers 1, 4, 7, 8 are unique lengths
            if len(output) == 2:
                digit_str += "1"
            elif len(output) == 3:
                digit_str += "7"
            elif len(output) == 4:
                digit_str += "4"
            elif len(output) == 7:
                digit_str += "8"
            elif len(output) == 6:
                # Next look at strings of length 6. Use the fact that 9 "contains"
                # the same segments as 1, 4, and 7. 0 contains 1 and 7. 6 contains
                # none of 1, 4, 7, nor 8.
                digit_set = set([c for c in output])
                if four_set.issubset(digit_set):
                    digit_str += "9"
                elif seven_set.issubset(digit_set):
                    digit_str += "0"
                else:
                    digit_str += "6"
            elif len(output) == 5:
                # Next look at strings of length 5. Use the fact that 3 "contains"
                # the same segments as 7. To check for 2, we can take the difference
                # of the segments of 8 and 4. This leaves the segments that are all
                # in 2 but not in 5. If nothing matches the digit is 5.
                digit_set = set([c for c in output])
                if seven_set.issubset(digit_set):
                    digit_str += "3"
                elif two_search.issubset(digit_set):
                    digit_str += "2"
                else:
                    digit_str += "5"
            else:
                print("Bad string length:", len(output))
                assert(False)
            
        # Sanity check we got all of the characters
        assert(len(digit_str) == len(outputs[input_idx].split(' ')))
        print("{} -> {}".format(outputs[input_idx], digit_str))

        running_sum += int(digit_str)

    return running_sum


if __name__ == "__main__":
    inputs, outputs = Part1.read_input(sys.argv[1])
    print("Solution:", deduce_segments(inputs, outputs))