import sys
import numpy as np
import Part1


if __name__ == "__main__":
    energy_grid = Part1.EnergyGrid(sys.argv[1])

    step = 0
    while energy_grid.grid_sum() > 0:
        step += 1
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