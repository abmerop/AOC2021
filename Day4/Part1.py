import sys
import numpy as np


def score_board(board, last_draw):
    """
    score_board computes the score of a winning board

    :param board: a 5x5 numpy ndarray of integers
    :param last_draw: the last random number drawn
    :return: the sum of the remaining unmatched spaces on board * winning number
    """

    assert(check_board(board))

    # Sum up the board and add back the number of -1s
    matches = np.sum(board == -1)
    return ((np.sum(board) + matches) * last_draw)

def check_board(board):
    """
    check_board checks if a single bingo card has won

    :input board: a 5x5 numpy ndarray of integers
    :return: Returns True on win and False otherwise
    """

    row_sums = board.sum(axis=1)
    col_sums = board.sum(axis=0)

    return True if -5 in row_sums or -5 in col_sums else False

def play_board(board, draws):
    """
    play_board plays a single bingo card using draws as the random numbers

    :param board: a 5x5 numpy ndarray of integers
    :param draws: a list of integer from the input file
    :return: the score from score_board and number of moves to win
    """

    # Draw each number from the draw list. Since integers are positive I am going
    # to mark matches by setting the value to -1. The board has won when a row
    # or column sums to -5.
    for turns, draw in enumerate(draws):
        if draw in board:
            loc = np.where(board==draw)
            # Ensure only one position is found (i.e., no duplicates on board)
            assert(len(loc[0]) == 1 and len(loc[1]) == 1)
            y = loc[0][0] # Row
            x = loc[1][0] # Col
            board[y][x] = -1

        if check_board(board):
            return (score_board(board, draw), turns)

    # We should only get to this point if the board did not win after all draws
    print("Board did not win!")
    print(board)
    assert(False)
    return 0, len(draws)


def play_bingo(input_file):
    """
    play_bingo reads an input file containing one line of random numbers
               followed by multiple 5x5 bingo boards with a blank line as
               a header. The 5x5 boards are positive integers <100 with 3
               spaces justified

    :param input_file: abspath to input text file meeting the criteria
    """

    inp = open(input_file, "r")
    lines = inp.readlines()

    # First line is the random numbers drawn
    # Convert to integer list for play_board
    draws = lines[0]
    draw_list = [int(x) for x in draws.split(',')]

    # Next are multiple 5x5 boards with a blank line before
    num_boards = (len(lines) - 1) // 6

    board_scores = {}
    for num in range(num_boards):
        board_text = lines[num*6+2:num*6+7]
        board = np.genfromtxt(board_text, delimiter=3).astype(int)
        (score, turns) = play_board(board, draw_list)
        print("Board won with score", score, "in", turns, "turns")
        print(board)

        # Keep track of all scores. Not strictly necessary since we
        # can track the minimum turns / maximum scores to solve.
        if not turns in board_scores:
            board_scores[turns] = [score]
        else:
            board_scores[turns].append(score)

    sorted_scores = {}
    for idx in sorted(board_scores):
        sorted_scores[idx] = board_scores[idx]
    print(sorted_scores)

if __name__ == "__main__":
    play_bingo(sys.argv[1])