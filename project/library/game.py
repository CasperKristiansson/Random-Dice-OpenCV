import cv2 as cv

import library.dices as dices
import library.image_computations as image_computations

class Game:
    def __init__(self, strategy='assassin'):
        self.board = [
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None]
        ]

        self.strategy = strategy

        if strategy == 'assassin':
            self.assassin_strategy()
        
    def assassin_strategy(self):
        self.dice_one_type = 'Assassin'
        self.dice_two_type = 'Bounty'
        self.dice_three_type = 'Joker'
        self.dice_four_type = 'Mimic'
        self.dice_five_type = 'Mine'

        self.empty = dices.get_empty()

        self.dices_model = [
            cv.CascadeClassifier('assets\Model\Assassin_Strategy\Assassin\cascade\cascade.xml')
        ]  

        self.dices_type = [
            self.dice_one_type,
            self.dice_two_type,
            self.dice_three_type,
            self.dice_four_type

        ]

    def process_frame(self, image):
        squares, squares_coordinates = image_computations.process_dice_board(image)
        self.board = image_computations.process_board(squares, self.dices_type, self.dices_model)

        # self.balance, self.dice_cost = image_computations.process_balance(image)

        return image
