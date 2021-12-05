import sys
import re


def increment_dict(map, x, y):
    """
    increment_dict is a helper function to increment dict value and handle new keys

    :param map: dict to increment tuple value in
    :param x: x coordinate to increment
    :param y: y coordinate to increment
    """

    # For new keys start the tuple value at 1
    if not (x,y) in map:
        map[(x,y)] = 1
    else:
        map[(x,y)] += 1

def danger_zones(map):
    """
    danger_zones counts how many coordinates have multiple vent crossings LANA!

    :param map: dict containing map data
    :return: the number of coordinates with multiple vent crossings
    """

    # I am sure there is a one-liner for this..
    dangers = 0
    for key, val in map.items():
        dangers = dangers + 1 if val > 1 else dangers

    return dangers

def map_ocean(input_file, diagonals=False):
    """
    map_ocean reads the input file and creates a vent map of the ocean floor

    :param input_file: the input file with multiple lines of "###,### -> ###,###"
    :param diagonals: set to False to consider only straight lines
    :return: the number of coordinates where vents overlap
    """

    # There are two approaches to managing the state of our ocean floor map. For a known
    # size and dense map, using a 2D array is optimal for memory. For a sparse map and
    # unknown size we can just use a dict of pairs.
    #
    # For this dict the the key is the (x,y) coordinate tuple and the "vent count" is the
    # value, where vent count is the number of vent lines which overlap at that point.
    map_dict = {}

    with open(input_file, 'r') as inp:
        # This will match numbers and stop on any other character which is sufficient
        # for the input format of "###,### -> ###,###""
        matcher = re.compile(r'\d+')
        for line in inp:
            # Find all returns a list. Convert to ints on the way out
            coord_list = [int(x) for x in matcher.findall(line)]
            x1, y1, x2, y2 = coord_list[0], coord_list[1], coord_list[2], coord_list[3]
            
            # Only consider straight lines
            if not diagonals and x1 != x2 and y1 != y2:
                continue

            # Just increment points in the dict. Handle horizontal lines first
            if y1 == y2:
                x_max = max(x1, x2)
                x_min = min(x1, x2)
                # Make sure to add 1 so the loop is inclusive of final point
                for offset in range(x_max - x_min + 1):
                    increment_dict(map_dict, x_min + offset, y1)
                continue

            # Then handle vertical lines
            if x1 == x2:
                y_max = max(y1, y2)
                y_min = min(y1, y2)
                # Make sure to add 1 again
                for offset in range(y_max - y_min + 1):
                    increment_dict(map_dict, x1, y_min + offset)
                continue

            # Last handle diagonals
            if diagonals and x1 != x2 and y1 != y2:
                # These should be 45 degrees meaning the lengths are the same
                assert(abs(x1 - x2) == abs(y1 - y2))
                x_step = 1 if x2 > x1 else -1
                y_step = 1 if y2 > y1 else -1
                x_list = [x*x_step+x1 for x in range(abs(x1-x2)+1)]
                y_list = [y*y_step+y1 for y in range(abs(y1-y2)+1)]
                for x, y in zip(x_list, y_list):
                    increment_dict(map_dict, x, y)

    return danger_zones(map_dict)

if __name__ == "__main__":
    print("Solution:", map_ocean(sys.argv[1]))