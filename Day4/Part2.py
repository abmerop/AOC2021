import Part1
import sys

# Since in part1 we have already tracked all of the boards and their scores,
# we can simply call the main function in Part1 and select the maximum value
# from the dict.
if __name__ == "__main__":
    Part1.play_bingo(sys.argv[1])