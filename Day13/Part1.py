import sys
import numpy as np


class LavaMap:
    def __init__(self, input_file):
        self.folds = []
        self.coords = []
        self.input_map = np.zeros([1000,1000])

        with open(input_file, 'r') as inp:
            set_folds = False
            for line in inp:
                if not set_folds:
                    if line.rstrip() == '':
                        set_folds = True
                    else:
                        x, y = [int(val) for val in line.rstrip().split(',')]
                        self.coords.append([x, y])
                else:
                    words = line.rstrip().split(' ')
                    fold_info = words[2].split('=')
                    if fold_info[0] == 'x':
                        self.folds.append([int(fold_info[1]), 0])
                    else:
                        assert(fold_info[0] == 'y')
                        self.folds.append([0, int(fold_info[1])])

            # Figure out the map size. To do this find the first x fold and first y fold
            found_x_fold = False
            found_y_fold = False
            map_height = 0
            map_width = 0
            for fold in self.folds:
                if fold[0] > 0 and not found_x_fold:
                    found_x_fold = True
                    map_height = fold[0] * 2 + 1
                elif fold[1] > 0 and not found_y_fold:
                    found_y_fold = True
                    map_width = fold[1] * 2 + 1

            self.input_map = np.zeros([map_width, map_height])

            for idx in range(len(self.coords)):
                self.input_map[self.coords[idx][1]][self.coords[idx][0]] = 1

    def fold(self):

        fold_axis = self.folds.pop(0)

        if fold_axis[1] > 0:
            assert(fold_axis[0] == 0)

            # Fold on y is simple
            upper = self.input_map[:fold_axis[1]]
            lower = np.flip(self.input_map[fold_axis[1]+1:], axis=0)

            self.input_map = upper + lower
        else:
            assert(fold_axis[1] == 0)

            # For fold on x axis, do the same but transpose before and after
            transpose_map = np.transpose(self.input_map)
            left = np.transpose(transpose_map[:fold_axis[0]])
            right = np.flip(np.transpose(transpose_map[fold_axis[0]+1:]), axis=1)

            self.input_map = left + right

        return len(np.where(self.input_map > 0)[0])
                

if __name__ == "__main__":
    lava_map = LavaMap(sys.argv[1])
    print("Solution:", lava_map.fold())
