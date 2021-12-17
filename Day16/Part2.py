import sys
from Part1 import BinStr


if __name__ == "__main__":
    # Some tests
    assert(BinStr("example7.txt").decode_packet() == 3)
    assert(BinStr("example8.txt").decode_packet() == 54)
    assert(BinStr("example9.txt").decode_packet() == 7)
    assert(BinStr("example10.txt").decode_packet() == 9)
    assert(BinStr("example11.txt").decode_packet() == 1)
    assert(BinStr("example12.txt").decode_packet() == 0)
    assert(BinStr("example13.txt").decode_packet() == 0)
    assert(BinStr("example14.txt").decode_packet() == 1)

    decoder = BinStr(sys.argv[1])

    print("Top level decode output:", decoder.decode_packet())
