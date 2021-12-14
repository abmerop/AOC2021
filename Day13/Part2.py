import sys
from Part1 import LavaMap


class DerivLavaMap(LavaMap):
    def __init__(self, input_file):
        super().__init__(input_file)

    def can_fold(self):

        return len(self.folds) > 0

    def human_readable(self):

        for row in range(len(self.input_map)):
            line_str = ""
            for col in self.input_map[row]:
                line_str += "#" if col > 0 else " "
            print(line_str)


if __name__ == "__main__":
    lava_map = DerivLavaMap(sys.argv[1])

    last_result = 0
    while lava_map.can_fold():
        last_result = lava_map.fold()

    lava_map.human_readable()
