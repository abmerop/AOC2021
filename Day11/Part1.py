import sys
import numpy as np


class EnergyGrid:
    def __init__(self, input_file):
        lines = open(input_file, 'r').readlines()
        self.energy_levels = np.genfromtxt(lines, delimiter=1).astype(int)
        self.flash_inhibited = np.zeros([len(self.energy_levels), len(self.energy_levels[0])])
        self.flash_count = 0


    def flash_check(self):

        return np.where(self.energy_levels > 9)

    def step(self):

        # Reset inhibited flash locations to zero
        self.flash_inhibited = np.zeros([len(self.energy_levels), len(self.energy_levels[0])])
        self.energy_levels += 1

    def count_step(self):

        self.flash_count += np.sum(self.flash_inhibited)

    def flash(self, x, y):

        # np.cross doesn't seem to do what I want
        neighbors = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]

        for neighbor in neighbors:
            self.increment_position(neighbor[0], neighbor[1])
        self.energy_levels[x][y] = 0
        self.flash_inhibited[x][y] = 1


    def increment_position(self, x, y):

        if x < 0 or y < 0 or y >= len(self.energy_levels) or x >= len(self.energy_levels[0]) or self.flash_inhibited[x][y]:
            return

        self.energy_levels[x][y] += 1

    def print_grid(self):
        print(self.energy_levels)

    def print_count(self):
        print(self.flash_count)

    def grid_sum(self):
        return np.sum(self.energy_levels)


if __name__ == "__main__":
    energy_grid = EnergyGrid(sys.argv[1])

    for step in range(1, 196):
        print("Step {}".format(step))

        energy_grid.step()
        flash_locations = energy_grid.flash_check()

        while len(flash_locations[0]) > 0:
            for x, y in zip(flash_locations[0], flash_locations[1]):
                energy_grid.flash(x, y)
            flash_locations = energy_grid.flash_check()
        energy_grid.print_grid()

        energy_grid.count_step()
        energy_grid.print_count()