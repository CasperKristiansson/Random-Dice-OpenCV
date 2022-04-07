import cv2 as cv
import itertools

def process_dice_board(image):
    width, height, _ = image.shape

    # Extracts the players board from the screenshot
    dice_board = image[
        int(width * 0.555):int(width * 0.748),
        int(height * 0.195):int(height * 0.75)
    ]

    width_board, height_board, _ = dice_board.shape

    squares = []
    squares_coordinates = []
    rows = 3
    columns = 5

    # Extracts and adds each dice square to the squares list
    # The function will also add the coordinates for each dice square.
    # To calculate the real coordinates the coordinate gets increased
    # with what the board was cutted from the screenshot.
    # imagine this loop just builds a grid system for the dice squares.
    for i, j in itertools.product(range(rows), range(columns)):
        squares.append(dice_board[
            int(i * width_board / rows):int(i * width_board / rows + width_board / rows),
            int(j * height_board / columns):int(j * height_board / columns + height_board / columns)
        ])

        squares_coordinates.append((
            int((j * height_board / columns + height_board / columns / 2) + height * 0.195),
            int((i * width_board / rows + width_board / rows / 2) + width * 0.555),
        ))

    return squares, squares_coordinates
