import sys
import numpy as np


class Chitons:
    def __init__(self, input_file):
        lines = open(input_file, 'r').readlines()
        self.risk_map = np.genfromtxt(lines, delimiter=1).astype(int)
        self.weight_map = np.zeros([self.risk_map.shape[0], self.risk_map.shape[1]])

    def get_risk(self, row, col):

        if row >= self.risk_map.shape[0] or col >= self.risk_map.shape[0]:
            return None
        if row < 0 or col < 0:
            return None
        return self.risk_map[row, col]

    def get_weight(self, row, col):

        if row >= self.weight_map.shape[0] or col >= self.weight_map.shape[0]:
            return None
        if row < 0 or col < 0:
            return None
        return self.weight_map[row, col]

    def min(self, a, b, default=0):

        if a == None and b != None:
            return b
        elif a != None and b == None:
            return a
        elif a == None and b == None:
            return default

        return min(a,b)

    def shortest_xy(self):
        """
        shortest_xy find the shortest path moving only in the x and y directions
        """

        print("Risk map size: {}, {}".format(self.risk_map.shape[0], self.risk_map.shape[1]))

        # To solve this, we will start from the end point and populate the weight
        # map with the total risk from that point to the end point. We can then
        # find the shortest path by moving to the smallest number in the weight
        # map. Once we have the path the sum can be found by summing those
        # coordinates in the risk map.

        # Move in a triangle pattern. This loop handles the lower right triangle.
        for col_idx in reversed(range(self.weight_map.shape[1])):
            start_col = col_idx
            start_row = self.weight_map.shape[0]-1

            while start_col < self.weight_map.shape[1]:
                # The cost at this point is the risk plus the minimum of the
                # coordinates to the right and below
                risk = self.get_risk(start_row, start_col)
                right = self.get_weight(start_row, start_col+1)
                below = self.get_weight(start_row+1, start_col)
                self.weight_map[start_row, start_col] = risk + self.min(right, below)

                start_col += 1
                start_row -= 1

        # This loop handles the upper left triangle, ignoring the diagonal.
        for row_idx in reversed(range(self.weight_map.shape[0]-1)):
            start_col = 0
            start_row = row_idx

            while start_row >= 0:
                # The cost at this point is the risk plus the minimum of the
                # coordinates to the right and below
                risk = self.get_risk(start_row, start_col)
                right = self.get_weight(start_row, start_col+1)
                below = self.get_weight(start_row+1, start_col)
                self.weight_map[start_row, start_col] = risk + self.min(right, below)

                start_col += 1
                start_row -= 1

        # The above only works if the map only increases in the right and down directions.
        # To handle corner cases, find locations where the left or upper weight plus the
        # risk of the current position is lower and update to the lower value. Repeat this
        # until the weights are unchanged.
        # Note: Misread problem. This is a salvage operation to use the code above.
        fixups = 1
        while fixups > 0:
            fixups = 0
            #print(self.weight_map)

            for row_idx in reversed(range(self.weight_map.shape[0])):
                for col_idx in reversed(range(self.weight_map.shape[1])):
                    right = self.get_weight(row_idx, col_idx+1)
                    left = self.get_weight(row_idx, col_idx-1)
                    above = self.get_weight(row_idx-1, col_idx)
                    below = self.get_weight(row_idx+1, col_idx)

                    if right != None and self.weight_map[row_idx, col_idx] > right + self.risk_map[row_idx, col_idx]:
                        self.weight_map[row_idx, col_idx] = right + self.risk_map[row_idx, col_idx]
                        #print("{}, {} updated to {}".format(row_idx, col_idx, self.weight_map[row_idx, col_idx]))
                        fixups += 1
                    if left != None and self.weight_map[row_idx, col_idx] > left + self.risk_map[row_idx, col_idx]:
                        self.weight_map[row_idx, col_idx] = left + self.risk_map[row_idx, col_idx]
                        #print("{}, {} updated to {}".format(row_idx, col_idx, self.weight_map[row_idx, col_idx]))
                        fixups += 1
                    if above != None and self.weight_map[row_idx, col_idx] > above + self.risk_map[row_idx, col_idx]:
                        self.weight_map[row_idx, col_idx] = above + self.risk_map[row_idx, col_idx]
                        #print("{}, {} updated to {}".format(row_idx, col_idx, self.weight_map[row_idx, col_idx]))
                        fixups += 1
                    if below != None and self.weight_map[row_idx, col_idx] > below + self.risk_map[row_idx, col_idx]:
                        self.weight_map[row_idx, col_idx] = below + self.risk_map[row_idx, col_idx]
                        #print("{}, {} updated to {}".format(row_idx, col_idx, self.weight_map[row_idx, col_idx]))
                        fixups += 1

            print("Made {} fixups".format(fixups))

    def solve(self):
            # We do not include the starting risk for whatever reason so the
            # solution is the top corner minus the risk at that position.
            return int(self.weight_map[0, 0] - self.risk_map[0, 0])


if __name__ == "__main__":
    chitons = Chitons(sys.argv[1])

    chitons.shortest_xy()
    print("Solution:", chitons.solve())