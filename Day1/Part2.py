import sys

inp = open(sys.argv[1])
lines = inp.readlines()
vals = [int(x) for x in lines]
print(sum(y>x for x,y in zip(vals, vals[3:])))