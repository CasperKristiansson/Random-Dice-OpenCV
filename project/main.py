import cv2 as cv
import time

from library.window_capture import WindowCapture
from library.vision import Vision
from library.game import Game
from library.out import Out

import tests.detection_tests as detection_tests


def run_detection_tests():
    wincap = WindowCapture('BlueStacks App Player')
    current_time = time.time()

    while True:
        screenshot = wincap.get_screenshot()
        screenshot = detection_tests.detect_pvp_box(screenshot)
        screenshot = detection_tests.detect_coop_box(screenshot)
        cv.imshow('Computer Vision', screenshot)

        current_time = library.util.fps_compute(current_time)

        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break


def run():
    wincap = WindowCapture('BlueStacks App Player')
    game = Game(strategy='assassin')
    out = Out()

    current_time = time.time()

    while True:
        screenshot = wincap.get_screenshot()
        
        screenshot = game.process_frame(screenshot)
        # cv.imshow('Computer Vision', screenshot)

        current_time = out.print_out(current_time, game.board)

        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break


def main():
    run()
    # run_detection_tests()


if __name__ == '__main__':
    main()
