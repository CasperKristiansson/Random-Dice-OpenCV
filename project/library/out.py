""""""

import rich
import time

class Out:
    """"""

    def __init__(self):
        pass

    def print_out(self, old_time, board):
        """"""
        end_time = time.time()

        print('\n\n\n\n\n\n\n\n')
        rich.print(f'FPS: {int(1 / (end_time - old_time))}')
        for row in board:
            rich.print(row)

        return end_time


if __name__ == '__main__':
    out = Out()
    board = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    out.print_out(0, board)
