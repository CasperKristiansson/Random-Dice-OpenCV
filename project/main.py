import cv2 as cv
import datetime

from window_capture import WindowCapture

def main():
    wincap = WindowCapture('BlueStacks App Player')
    time_start = datetime.datetime.now()

    while True:
        screenshot = wincap.get_screenshot()
        cv.imshow('Computer Vision', screenshot)

        time_end = datetime.datetime.now()
        time_delta = time_end - time_start
        time_start = time_end

        print(f'FPS: {1 / time_delta.total_seconds()}')

        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break


if __name__ == '__main__':
    main()
