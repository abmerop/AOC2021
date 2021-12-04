import sys

# Using a bit of a cheeky approach, format the input in a way that it consists
# of function calls, then use python's eval() call. Not safe for generic input :)
def forward(units, position, depth, aim):
    position += units
    depth += units * aim
    return position, depth, aim

def down(units, position, depth, aim):
    aim += units
    return position, depth, aim

def up(units, position, depth, aim):
    aim -= units
    return position, depth, aim

if __name__ == "__main__":
    # Read input
    inp = open(sys.argv[1], 'r')
    lines = inp.readlines()

    position = 0
    aim = 0
    depth = 0

    funcs = [x.replace(' ', '(').replace('\n', ',position,depth,aim)') for x in lines]
    for func in funcs:
        position, depth, aim = eval(func)

    print("Magnitude:", position * depth)
