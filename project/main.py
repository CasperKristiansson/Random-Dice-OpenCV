import cv2 as cv
import datetime

from library.window_capture import WindowCapture
from library.vision import Vision
from library.game import Game
import tests.detection_tests as detection_tests


def run_detection_tests():
    wincap = WindowCapture('BlueStacks App Player')
    time_start = datetime.datetime.now()

    while True:
        screenshot = wincap.get_screenshot()
        screenshot = detection_tests.detect_pvp_box(screenshot)
        screenshot = detection_tests.detect_coop_box(screenshot)
        cv.imshow('Computer Vision', screenshot)

        time_end = datetime.datetime.now()
        time_delta = time_end - time_start
        time_start = time_end

        print(f'FPS: {1 / time_delta.total_seconds()}')

        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break


def run():
    wincap = WindowCapture('BlueStacks App Player')
    time_start = datetime.datetime.now()
    game = Game(strategy='assassin')

    while True:
        screenshot = wincap.get_screenshot()
        
        screenshot = game.process_frame(screenshot)
        cv.imshow('Computer Vision', screenshot)

        time_end = datetime.datetime.now()
        time_delta = time_end - time_start
        time_start = time_end

        print(f'FPS: {1 / time_delta.total_seconds()}')

        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break


def main():
    run()
    # run_detection_tests()


if __name__ == '__main__':
    main()
