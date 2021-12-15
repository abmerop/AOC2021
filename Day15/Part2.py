import sys
import numpy as np
from Part1 import Chitons


class BigChitons(Chitons):
    def __init__(self, input_file):
        super().__init__(input_file)

        # Extend the risk map by creating first: U = [A B C D E] where A is the
        # original risk map, B = A + 1, C = A + 2, etc.
        B = self.risk_map + 1
        C = self.risk_map + 2
        D = self.risk_map + 3
        E = self.risk_map + 4
        U = np.concatenate((self.risk_map, B, C, D, E), axis=1)

        # Next extend rows
        V = U + 1
        W = U + 2
        X = U + 3
        Y = U + 4
        Z = np.concatenate((U, V, W, X, Y), axis=0)

        # Reset anything that increased beyond 9 to 1
        fixups = np.where(Z > 9)
        for x, y in zip(fixups[0], fixups[1]):
            Z[x, y] -= 9

        # Overwrite the risk and weight maps so we can reuse super's methods
        self.risk_map = Z
        self.weight_map = np.zeros([self.risk_map.shape[0], self.risk_map.shape[1]])


if __name__ == "__main__":
    chitons = BigChitons(sys.argv[1])
        
    # Note: takes about a minute
    chitons.shortest_xy()
    print("Solution:", chitons.solve())