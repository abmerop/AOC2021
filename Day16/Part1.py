import sys
import numpy as np


class BinStr:
    def __init__(self, input_file):
        # Input is one single line of hexadecimal numbers
        hex_str = open(input_file, 'r').readlines()[0].rstrip()

        # Python's int() function will ignore leading zeros in the string so we must
        # first prepend those manually
        self.bin_str = ""
        while hex_str[0] == '0':
            self.bin_str += '0000'
            hex_str = hex_str[1:]

        # The bin function prefixes with '0b' which we should remove from the string
        self.bin_str += bin(int(hex_str, 16))[2:]

        # The bin function does not pad the start of the string so we need to add that
        if len(self.bin_str) % 4 != 0:
            pad_count = 4 - (len(self.bin_str) % 4)
            pad_str = '0' * pad_count
            self.bin_str = pad_str + self.bin_str

        self.version_sum = 0

    def pop_bits(self, num_bits):
        pop_val = self.bin_str[0:num_bits]
        self.bin_str = self.bin_str[num_bits:]
        return pop_val

    def get_packet_version(self):
        # Version is 3 bits
        ver_str = self.pop_bits(3)
        ver_val = int(ver_str, 2)
        self.version_sum += ver_val
        return ver_val

    def get_packet_type(self):
        # Type is 3 bits
        type_str = self.pop_bits(3)
        return int(type_str, 2)

    def decode_literal(self):
        # A literal has 5 bits at a time
        # First bit is ~is_last followed by 4 bits of the number literal
        literal_str = ""
        while self.pop_bits(1) == '1':
            literal_str += self.pop_bits(4)
        
        # Append the last group
        literal_str += self.pop_bits(4)
        return int(literal_str, 2)

    def decode_packet(self):
        ret_val = 0

        self.get_packet_version()
        pkt_type = self.get_packet_type()
        if pkt_type == 4:
            # Literal
            ret_val = self.decode_literal()
        else:
            # Operator
            literals = self.decode_operator()
            # This could be a fancy dict of lambdas
            if pkt_type == 0:
                # Sum
                ret_val = np.sum(literals)
            elif pkt_type == 1:
                # Product
                ret_val = np.prod(literals)
            elif pkt_type == 2:
                # Min
                ret_val = np.min(literals)
            elif pkt_type == 3:
                # Max
                ret_val = np.max(literals)
            elif pkt_type == 5:
                # Greater than first element
                assert(len(literals) == 2)
                ret_val = (literals[0] > literals[1])
            elif pkt_type == 6:
                # Less than first element
                assert(len(literals) == 2)
                ret_val = (literals[0] < literals[1])
            else:
                assert(pkt_type == 7)
                # Equal to first element
                assert(len(literals) == 2)
                ret_val = (literals[0] == literals[1])

        return ret_val

    def decode_operator(self):
        literals = []

        # The next bit is the length type ID. If 0, the length is 15 bits.
        # If 1, the length is 11 bits
        length_type = self.pop_bits(1)
        if length_type == '0':
            # This type is encoded in bits
            bit_length = int(self.pop_bits(15), 2)

            # Get the current size and loop until we have popped `bit_length`
            # number of bits
            start_size = self.get_size()
            end_size = start_size - bit_length
            assert(end_size >= 0)
            while self.get_size() > end_size and self.get_size() > 0:
                val = self.decode_packet()
                literals.append(val)

        else:
            # This type is encoded in number of sub-packets
            for pkt_idx in range(int(self.pop_bits(11), 2)):
                val = self.decode_packet()
                literals.append(val)

        return literals

    def get_size(self):
        return len(self.bin_str)

    def get_str(self):
        return self.bin_str

    def get_version_sum(self):
        self.decode_packet()
        return self.version_sum


if __name__ == "__main__":
    # Some tests
    assert(BinStr("example1.txt").get_version_sum() == 6)
    assert(BinStr("example2.txt").get_version_sum() == 9)
    assert(BinStr("example3.txt").get_version_sum() == 16)
    assert(BinStr("example4.txt").get_version_sum() == 12)
    assert(BinStr("example5.txt").get_version_sum() == 23)
    assert(BinStr("example6.txt").get_version_sum() == 31)

    decoder = BinStr(sys.argv[1])

    print(decoder.get_version_sum())
