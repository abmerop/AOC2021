import sys


corruption_scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

# Using a class because I want experience with python classes.
class NavChecker:
    def __init__(self):
        self.openers = ['<', '(', '{', '[']
        self.closers = ['>', ')', '}', ']']
        self.valid_pairs = [pair for pair in zip(self.openers, self.closers)]

        self.stack = []

    def check_corrupt(self, line):

        self.stack = []

        # Push openers to stack. Pop the stack when a closer is seen and check
        # that the opener matches
        for char in line:
            if char in self.openers:
                self.stack.append(char)
            elif char in self.closers:
                opener = self.stack.pop()
                if not (opener, char) in self.valid_pairs:
                    return (True, char)
            else:
                print("Ignoring invalid syntax: {}".format(char))

        return (False, ' ')

    def get_stack(self):
        return self.stack


def read_input(input_file):

    lines = open(input_file, 'r').readlines()
    slines = [line.strip() for line in lines]

    return slines


def score_corrputed(lines):

    nav_checker = NavChecker()

    score = 0
    for line in lines:
        corrupt, illegal_char = nav_checker.check_corrupt(line)
        if corrupt:
            score += corruption_scores[illegal_char]
            print("Line {} is corrupt!\n".format(line))
        else:
            print("Line {} is not corrupt\n".format(line))

    return score


if __name__ == "__main__":
    input = read_input(sys.argv[1])
    print("Solution:", score_corrputed(input))