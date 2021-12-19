from functools import reduce
from re import S
import sys


depth = lambda L: isinstance(L, list) and max(map(depth, L))+1

def read_snail_number(line):
    snail_number = []
    exec("snail_number.append(%s)" % line)
    return snail_number[0]

def needs_reduce(snail_number):
    return depth(snail_number) > 4

def find_at_depth(snail_number, depth, path=[]):
    if depth == 0:
        return (snail_number, path)

    if type(snail_number[0]) == type(list()):
        ret_val = find_at_depth(snail_number[0], depth-1, path+[0])
        if ret_val is not None:
            return ret_val
    if type(snail_number[1]) == type(list()):
        ret_val = find_at_depth(snail_number[1], depth-1, path+[1])
        assert(ret_val != None)
        return ret_val

def set_value(snail_number, value, path):
    expr_str = "snail_number"
    for idx in range(len(path)):
        expr_str += "[path[{}]]".format(idx)
    expr_str += " = value"
    exec(expr_str)
    return snail_number

def get_value(snail_number, path):
    expr_str = "snail_number"
    for idx in range(len(path)):
        expr_str += "[{}]".format(path[idx])
    val = eval(expr_str)
    return val

def all_valid_paths(snail_number, paths, path=[]):
    if type(snail_number[0]) == type(list()):
        all_valid_paths(snail_number[0], paths, path+[0])
    else:
        assert(type(snail_number[0]) == type(int()))
        paths.append(path+[0])
    if type(snail_number[1]) == type(list()):
        all_valid_paths(snail_number[1], paths, path+[1])
    else:
        assert(type(snail_number[1]) == type(int()))
        paths.append(path+[1])

def reduce_number(snail_number, reduce_path):
    val = get_value(snail_number, reduce_path)
    assert(len(val) == 2 and type(val[0]) == type(int()) and type(val[1]) == type(int()))

    # Add left value in pair to the first left element (if any)
    valid_paths = []
    all_valid_paths(snail_number, valid_paths)
    for valid_idx, valid_path in enumerate(valid_paths):
        if valid_path == reduce_path+[0] and valid_idx > 0:
            lval = get_value(snail_number, valid_paths[valid_idx-1])
            set_value(snail_number, val[0]+lval, valid_paths[valid_idx-1])
        elif valid_path == reduce_path+[1] and valid_idx < len(valid_paths)-1:
            rval = get_value(snail_number, valid_paths[valid_idx+1])
            set_value(snail_number, val[1]+rval, valid_paths[valid_idx+1])

    # Set pair to zero
    snail_number = set_value(snail_number, 0, reduce_path)

def split_number(snail_number, split_path):
    val = get_value(snail_number, split_path)
    assert(type(val) == type(int()))
    new_val = [val // 2, (val+1) // 2]
    set_value(snail_number, new_val, split_path)

def do_addition(lhs, rhs):
    snail_number = rhs
    if lhs is not None:
        snail_number = [lhs, rhs]

    # This is not optimized. The prompt was not clear on ordering here and spent
    # a lot of time debugging that...
    reduced_or_split = True
    while reduced_or_split:
        reduced_or_split = False

        test_paths = []
        all_valid_paths(snail_number, test_paths)
        for path in test_paths:
            if len(path) > 4:
                reduce_number(snail_number, path[:-1])
                #print("After reduce:", snail_number)
                reduced_or_split = True
                break

        if not reduced_or_split:
            for path in test_paths:
                if get_value(snail_number, path) > 9:
                    split_number(snail_number, path)
                    #print("After split:", snail_number)
                    reduced_or_split = True
                    break

    return snail_number

def is_pair_path(snail_number, path):
    val = get_value(snail_number, path)
    return type(val) == type(list()) and len(val) == 2 and \
        type(val[0]) == type(int()) and type(val[1]) == type(int())

def magnitude(snail_number):
    paths = []
    all_valid_paths(snail_number, paths)
    while len(paths) > 0:
        # Last two to add
        if len(paths) == 2:
            ret_val = 3*get_value(snail_number, paths[0]) + 2*get_value(snail_number, paths[1])
            break

        for path in paths:
            if len(path) > 1 and is_pair_path(snail_number, path[:-1]):
                val = get_value(snail_number, path[:-1])
                new_val = 3*val[0] + 2*val[1]
                set_value(snail_number, new_val, path[:-1])
                break

        paths = []
        all_valid_paths(snail_number, paths)

    return ret_val

if __name__ == "__main__":
    previous_number = None
    with open(sys.argv[1], 'r') as inp:
        for line in inp:
            snail_number = read_snail_number(line.rstrip())
            # Not handling arbitrary depths. Seems good for the input given.
            assert(depth(snail_number) <= 5)

            previous_number = do_addition(previous_number, snail_number)

    print("Solution:", magnitude(previous_number))