import cv2 as cv

from vision import Vision
import dices

class Game:
    def __init__(self, strategy='assassin'):
        self.strategy = strategy

        if strategy == 'assassin':
            self.assassin_strategy()
        
    def assassin_strategy(self):
        self.dice_one = dices.get_assassin_dice()
        self.dice_two = dices.get_joker_dice()
        self.dice_three = dices.get_summoner_dice()
        self.dice_four = dices.get_mimic_dice()        
