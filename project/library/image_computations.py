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
        squares_coordinates.append([
            int((j * height_board / columns + height_board / columns / 2) + height * 0.195),
            int((i * width_board / rows + width_board / rows / 2) + width * 0.555),
        ])

    return squares, squares_coordinates


def process_board(squares, dices_type, dices_model):
    board = [
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None]
    ]

    board_list = []

    for index_square, square in enumerate(squares):
        jump = False
        for index_model, model in enumerate(dices_model):
            rectangles = model.detectMultiScale(square)
            area = 0
            for recantangle in rectangles:
                x, y, w, h = recantangle
                area = (w - x) * (h - y)
            if area > 2500:
                # board[index_square // 5][index_square % 5] = f'{dices_type[index_model]} - {area}'
                board[index_square // 5][index_square % 5] = dices_type[index_model]
                board_list.append(dices_type[index_model])
                jump = True
                break

        if not jump:
            board_list.append(None)    

    return board, board_list

def process_balance(image):
    width, height, _ = image.shape

    balance_image = image[
        int(width * 0.83):int(width * 0.86),
        int(height * 0.17):int(height * 0.32)
    ]

    return None, balance_image


def image(image_compare, screenshot):
    result = cv.matchTemplate(image_compare, screenshot, cv.TM_CCOEFF_NORMED)

    _, max_val, _, _ = cv.minMaxLoc(result)
    return max_val
