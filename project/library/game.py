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
        self.iteration = 0
        self.board_history_size = 50

        self.initiate_board_history()

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
            cv.CascadeClassifier('assets\Model\Assassin_Strategy\Assassin\model\cascade.xml')
        ]  

        self.dices_type = [
            self.dice_one_type,
            self.dice_two_type,
            self.dice_three_type,
            self.dice_four_type,
            self.dice_five_type
        ]
    
    def initiate_board_history(self):
        self.board_history = [[] for _ in range(self.board_history_size)]

    def process_frame(self, image):
        squares, squares_coordinates = image_computations.process_dice_board(image)
        self.board = image_computations.process_board(squares, self.dices_type, self.dices_model)
        self.iteration += 1

        if all(board == self.board for board in self.board_history):
            pass
        
        self.board_history[self.iteration % self.board_history_size] = self.board


        # self.balance, self.dice_cost = image_computations.process_balance(image)

        return image
