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
        self.dice_one = dices.get_assassin_dice()
        self.dice_one_type = 'assassin'

        self.dice_two = dices.get_joker_dice()
        self.dice_two_type = 'joker'

        self.dice_three = dices.get_summoner_dice()
        self.dice_three_type = 'summoner'

        self.dice_four = dices.get_mimic_dice()
        self.dice_four_type = 'mimic'

        self.empty = dices.get_empty()

        self.dices = [
            self.empty,
            self.dice_one,
            self.dice_two,
            self.dice_three,
            self.dice_four
        ]     

    def process_frame(self, image):
        squares, squares_coordinates = image_computations.process_dice_board(image)
        self.board = image_computations.process_board(squares, self.dices)

        # print(self.board)

        return image
