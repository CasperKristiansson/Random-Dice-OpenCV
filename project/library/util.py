""""""
import time


def fps_compute(start_time):
    end_time = time.time()
    print(f'FPS: {int(1 / (end_time - start_time))}')

    return end_time
