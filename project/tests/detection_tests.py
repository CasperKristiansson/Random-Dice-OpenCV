import cv2 as cv
import time
import numpy as np

def detect_coop_box(menu_img):
    """
    Detects the coop button in the menu image and
    draws a rectangle around the button. Average
    detection rate is 99.957%

    :param menu_img: opencv object

    :return: opencv object
    """
    coop_button_img = cv.imread('assets\Menu\CO-OP Button.png', cv.IMREAD_UNCHANGED)
    result = cv.matchTemplate(menu_img, coop_button_img, cv.TM_CCOEFF_NORMED)

    _, max_val, _, button_top_left = cv.minMaxLoc(result)
    print(f'Best match top left position: {str(button_top_left)}')
    print(f'Best match confidence: {max_val}')

    bottom_right = button_top_left[0] + coop_button_img.shape[1], button_top_left[1] + coop_button_img.shape[0]
    cv.rectangle(menu_img, button_top_left, bottom_right, color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

    return menu_img


def detect_pvp_box(menu_img):
    """
    Detects the pvp button in the menu image and
    draws a rectangle around the button. Average
    detection rate is 45.625%.

    :param menu_img: opencv object

    :return: opencv object
    """
    pvp_button_img = cv.imread('assets\Menu\PVP Button.png', cv.IMREAD_UNCHANGED)
    result = cv.matchTemplate(menu_img, pvp_button_img, cv.TM_CCOEFF_NORMED)

    _, max_val, _, button_top_left = cv.minMaxLoc(result)
    print(f'Best match top left position: {str(button_top_left)}')
    print(f'Best match confidence: {max_val}')

    bottom_right = button_top_left[0] + pvp_button_img.shape[1], button_top_left[1] + pvp_button_img.shape[0]
    cv.rectangle(menu_img, button_top_left, bottom_right, color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

    return menu_img
