import cv2 as cv
import time

from library.window_capture import WindowCapture
from library.vision import Vision
from library.game import Game
from library.out import Out


def run():
    wincap = WindowCapture('BlueStacks App Player')
    game = Game(strategy='assassin')
    game.set_offset_coordinates(wincap.offset_x, wincap.offset_y)
    out = Out()

    current_time = time.time()

    while True:
        screenshot = wincap.get_screenshot()
        screenshot = game.process_frame(screenshot)
        # cv.imshow('Computer Vision', screenshot)

        # current_time = out.print_out(current_time, game.board)
        out.print_board(game.banned_merges)

        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break


def main():
    run()


if __name__ == '__main__':
    main()
