import sys
import re

# Read input
inp = open(sys.argv[1], 'r')
lines = inp.readlines()

# Since we don't care about the order we will simply sum everything in each direction
# Format is: "forward/up/down ##". Match each case, split into a list, and convert
# the first element of that list into an integer. Then, take the sum.
forwards = sum([int(x.split()[1]) for x in lines if re.match(r'forward', x)])
ups = sum([int(x.split()[1]) for x in lines if re.match(r'up', x)])
downs = sum([int(x.split()[1]) for x in lines if re.match(r'down', x)])

# Y-axis is inverted, so down is moving in the positive direction
horiz, vert = forwards, downs-ups
print("Horizontal/Vertical:", horiz, vert)
print("Magnitude:", horiz * vert)
