import uuid
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

        #? This function could in theory be computed once and then
        #? used to calculate the coordinates for each dice square.
        #? Should maybe be done in the future?
        squares_coordinates.append((
            int((j * height_board / columns + height_board / columns / 2) + height * 0.195),
            int((i * width_board / rows + width_board / rows / 2) + width * 0.555),
        ))

    for square in squares:
        cv.imwrite(f'assets\\Raw Data\\{uuid.uuid4()}.png', square)

    return squares, squares_coordinates


def process_board(squares, dices):
    board = [
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None]
    ]

    for row, column in itertools.product(range(3), range(5)):
        confidence = []
        dices_index = []

        for dice_type_index, dice_type in enumerate(dices):
            for dice_rank_index, dice_rank in enumerate(dice_type):

                confidence.append(
                    dice_rank.confidence(squares[row * 5 + column])
                )

                dices_index.append(
                    (dice_type_index, dice_rank_index)
                )

        confidence_max = max(confidence)

        if confidence_max > 0.4:
            index = confidence.index(confidence_max)
            if dices_index[index] != (0, 0):
                # print(confidence_max)
                board[row][column] = dices_index[index]
    
    return board

def process_balance(image):
    width, height, _ = image.shape

    balance_image = image[
        int(width * 0.83):int(width * 0.86),
        int(height * 0.17):int(height * 0.32)
    ]

    return None, balance_image
