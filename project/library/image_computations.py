import cv2 as cv
import itertools

def process_dice_board(image):
    width, height, _ = image.shape

    # Extracts the players board from the screenshot
    dice_board = image[
        int(width * 0.555):int(width * 0.748),
        int(height * 0.195):int(height * 0.75)
    ]

    width, height, _ = dice_board.shape

    squares = []
    rows = 3
    columns = 5

    # Extracts and adds each dice square to the squares list
    for i, j in itertools.product(range(rows), range(columns)):
        squares.append(dice_board[
            int(i * width / rows):int(i * width / rows + width / rows),
            int(j * height / columns):int(j * height / columns + height / columns)
        ])

    return squares
