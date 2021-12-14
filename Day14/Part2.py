import sys
from Part1 import Polymer


# Part2 is simply Part1 with additional steps. A naive string concatenation
# approach would eventually fail to do 40 steps due to the amount of memory
# required.
if __name__ == "__main__":
    poly = Polymer(sys.argv[1])

    for step in range(40):
        poly.step()

    poly.count_chars()
    print("Solution:", poly.solve())