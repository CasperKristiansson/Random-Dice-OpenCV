import cv2 as cv
import pyautogui
import time

import library.dices as dices
import library.image_computations as image_computations
from library.vision import Vision

class Game:
    def __init__(self, strategy='assassin'):
        self.board = [
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None]
        ]

        self.merged_board = self.board.copy()

        self.strategy = strategy
        self.iteration = 0
        self.offset_x, self.offset_y = 0, 0
        self.board_history_size = 20
        self.initiate_board_history()
        self.merged = [None, None, None, None]
        self.banned_merges = []

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
    
    def set_offset_coordinates(self, x, y):
        self.offset_x, self.offset_y = x, y

    def process_frame(self, image):
        squares, self.squares_coordinates = image_computations.process_dice_board(image)
        self.board, self.board_list = image_computations.process_board(squares, self.dices_type, self.dices_model)

        # if self.board == self.merged_board and self.merged not in self.banned_merges and self.merged[0] is not None:
        #     self.banned_merges.append(self.merged)
        #     self.merged = [None, None, None, None]
        # else:
        #     for banned_merge in self.banned_merges:
        #         if self.board_list[banned_merge[0]] != banned_merge[2] or self.board_list[banned_merge[1]] != banned_merge[3]:
        #             self.banned_merges.remove(banned_merge)


        if all(board == self.board for board in self.board_history):
           # self.merge_dice()
           pass

        self.iteration += 1
        self.board_history[self.iteration % self.board_history_size] = self.board
        # self.balance, self.dice_cost = image_computations.process_balance(image)

        return image
    
    def merge_dice(self):
        self.merged_board = self.board.copy()

        for i in range(len(self.board_list)):
            for j in range(i, len(self.board_list)):
                if self.board_list[i] is None or self.board_list[i] != self.board_list[j] or self.squares_coordinates[i] == self.squares_coordinates[j]:
                    continue
                    
                for coordinate in self.banned_merges:
                    if coordinate[0] == self.squares_coordinates[i] and coordinate[1] == self.squares_coordinates[j]:
                        continue

                # pyautogui.moveTo(self.offset_x + self.squares_coordinates[i][0], self.offset_y + self.squares_coordinates[i][1])
                # pyautogui.dragTo(self.offset_x + self.squares_coordinates[j][0], self.offset_y + self.squares_coordinates[j][1], button='left', duration=1)

                self.merged_board[i % 3][i % 5] = None
                self.merged = [i, j, self.board_list[i], self.board_list[j]]

                break

            else:
                continue
            break
