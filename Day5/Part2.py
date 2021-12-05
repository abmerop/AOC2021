import Part1
import sys

# Reuse the code from part one but set diagonals to true in map_ocean function
if __name__ == "__main__":
    print("Solution:", Part1.map_ocean(sys.argv[1], True))