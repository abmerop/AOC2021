import sys
import re


class Polymer:
    def __init__(self, input_file):
        lines = open(input_file, 'r').readlines()
        self.template = lines[0].rstrip()
        self.step_count = 0

        self.pairs_dict = {}
        self.unique_chars = set()
        pair_matcher = re.compile('([A-Z]+) -> ([A-Z])\n')
        for pair_str in lines[2:]:
            pair = pair_matcher.match(pair_str).groups()
            self.pairs_dict[pair[0]] = pair[1]
            self.unique_chars.add(pair[1])

        print("Unique chars:", self.unique_chars)
        self.element_counts = {}

        # Convert the template into a dict of character pairs. The input should
        # have all possible combinations of letters. This means we can simply
        # scan two letters at a time.
        self.pairs_counts = {}
        for idx in range(len(self.template) - 1):
            pair = self.template[idx:idx+2]
            if pair in self.pairs_counts:
                self.pairs_counts[pair] += 1
            else:
                self.pairs_counts[pair] = 1

    def step(self):

        self.step_count += 1
        print("Step", self.step_count)

        # Because the pairs overlap, we can simply replace the pair in the pair
        # counts dictionary with the first character concatenated with the char
        # to be inserted. To prepare for the next step also add the insertion
        # char concatenated with the second character of the pair. These
        # replacements would happen for each occurrence of that pair, so the
        # number of pairs with the new character pair is the same.
        new_pairs_counts = {}
        for key, val in self.pairs_counts.items():
            new_key = key[0] + self.pairs_dict[key]
            if not new_key in new_pairs_counts:
                new_pairs_counts[new_key] = val
            else:
                new_pairs_counts[new_key] += val

            new_key = self.pairs_dict[key] + key[1]
            if not new_key in new_pairs_counts:
                new_pairs_counts[new_key] = val
            else:
                new_pairs_counts[new_key] += val
        self.pairs_counts = new_pairs_counts

    def count_chars(self):

        # Initialize list so we don't need to handle KeyErrors
        for char in self.unique_chars:
            self.element_counts[char] = 0

        # Because of the overlap we only need to count one of the characters in
        # each pair. This will not count either the first or last character in
        # the polymer. However, this character never changes, so we can add that
        # extra character outside of the loop.
        self.element_counts[self.template[0]] += 1
        for key, val in self.pairs_counts.items():
            self.element_counts[key[1]] += val

    def solve(self):

        # The solution is the count of the most common element minus the count of
        # the least common element.
        return max(self.element_counts.values()) - min(self.element_counts.values())


if __name__ == "__main__":
    poly = Polymer(sys.argv[1])

    for step in range(10):
        poly.step()

    poly.count_chars()
    print("Solution:", poly.solve())