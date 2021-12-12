import sys
import Part1


closing_dict = {
    '<': '>',
    '(': ')',
    '[': ']',
    '{': '}'
}

score_dict = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

def fix_incomplete(lines):

    nav_checker = Part1.NavChecker()

    fixups = []
    for line in lines:
        corrupt, _ = nav_checker.check_corrupt(line)
        if not corrupt:
            stack = nav_checker.get_stack()
            fixup = ""
            while len(stack) > 0:
                fixup += closing_dict[stack.pop()]
            print("Fixed line {} with {}".format(line, fixup))
            fixups.append(fixup)

    return fixups


def score_fixups(fixups):

    scores = []
    for fixup in fixups:
        score = 0

        # Score from left to right
        for char in fixup:
            score = score * 5 + score_dict[char]
        scores.append(score)

    return scores


if __name__ == "__main__":
    input = Part1.read_input(sys.argv[1])
    fixups = fix_incomplete(input)
    scores = score_fixups(fixups)

    sorted_scores = sorted(scores)
    print(sorted_scores)
    print("Solution:", sorted_scores[len(scores)//2])