import cv2 as cv

def draw_dice_squares(image, coordinates):
    for square in coordinates:
        image = cv.circle(image, square, 5, (0, 0, 255), -1)
    
    return image
