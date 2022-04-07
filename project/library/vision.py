import cv2 as cv
import numpy as np


class Vision:
    """
    https://github.com/learncodebygaming/opencv_tutorials/blob/master/005_real_time/vision.py
    """
    image = None
    width = 0
    height = 0
    method = None

    def __init__(self, image_path, method=cv.TM_CCOEFF_NORMED):
        self.image = cv.imread(image_path, cv.IMREAD_UNCHANGED)
        self.image = cv.resize(self.image, (0, 0), fx=0.75, fy=0.75)

        self.width = self.image.shape[1]
        self.height = self.image.shape[0]
        self.method = method
    
    def confidence(self, compare_image):
        # In order to compare the images the 'compare_image'
        # needs to be bigger or equal than the 'self.image'.
        # A solution to this would be to update the compare_image
        # to the same size as the 'self.image' but this is a
        # solution that slows down the program from 21fps -> 1-2fps.
        # The hardcoded solution is to minimize the self.image to 75%

        result = cv.matchTemplate(compare_image, self.image, cv.TM_CCOEFF_NORMED)

        _, max_val, _, _ = cv.minMaxLoc(result)
        return max_val

    def find(self, running_img, threshold=0.4, debug_mode=None):
        result = cv.matchTemplate(running_img, running_img, self.method)

        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))

        # print(locations)

        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), self.width, self.height]
            rectangles.extend((rect, rect))
        rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)
        # print(rectangles)

        points = []
        if len(rectangles):
            line_color = (0, 255, 0)
            line_type = cv.LINE_4
            marker_color = (255, 0, 255)
            marker_type = cv.MARKER_CROSS

            for (x, y, w, h) in rectangles:
                center_x = x + int(w/2)
                center_y = y + int(h/2)
                points.append((center_x, center_y))

                if debug_mode == 'rectangles':
                    top_left = (x, y)
                    bottom_right = (x + w, y + h)
                    cv.rectangle(running_img, top_left, bottom_right, color=line_color, 
                                lineType=line_type, thickness=2)

                elif debug_mode == 'points':
                    cv.drawMarker(running_img, (center_x, center_y), 
                                color=marker_color, markerType=marker_type, 
                                markerSize=40, thickness=2)

        if debug_mode:
            cv.imshow('Matches', running_img)
            # cv.waitKey()
            # cv.imwrite('result_click_point.jpg', haystack_img)

        return points
