import sys
import Part1
import copy


if __name__ == "__main__":
    lines = [Part1.read_snail_number(sline.rstrip()) for sline in open(sys.argv[1], 'r').readlines()]

    # There might be some trick here but running out of time, so brute force check every combination
    max_magnitude = 0
    check_count = 0
    checks = len(lines)**2
    for lhs in lines:
        for rhs in lines:
            check_count += 1
            if lhs == rhs:
                continue

            print("Progress: {}/{}".format(check_count, checks))
            check_number = Part1.do_addition(copy.deepcopy(lhs), copy.deepcopy(rhs))
            magnitude = Part1.magnitude(check_number)
            if magnitude > max_magnitude:
                max_magnitude = magnitude

    print("Max magnitude is", max_magnitude)