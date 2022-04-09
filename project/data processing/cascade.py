"""
https://www.youtube.com/watch?v=XrCAvs9AePM&t=466s
"""

import os
import cv2 as cv

def cascade_negative_samples(positive_dice_type):
    negative_sample = []

    for dice_type in os.listdir('assets\\Dices'):
        if dice_type == positive_dice_type:
            continue

        if dice_type == 'Empty':
            for image_name in os.listdir(os.path.join('assets\\Dices', dice_type)):
                negative_sample.append(os.path.join('assets\\Dices', dice_type, image_name))
            continue

        for dice_rank in os.listdir(os.path.join('assets\\Dices', dice_type)):
            for image_name in os.listdir(os.path.join('assets\\Dices', dice_type, dice_rank)):
                negative_sample.append(os.path.join('assets\\Dices', dice_type, dice_rank, image_name))
    
    for row in negative_sample:
        print(row)
    
    print(len(negative_sample))

    # Save the information to a txt file at assets\Model\Assassin Strategy\Assassin
    # with open(os.path.join('assets\\Model\\Assassin Strategy\\Assassin', 'neg.txt'), 'w') as file:
    #     for row in negative_sample:
    #         file.write(f'{row}\n')


def cascade_positive_sample(positive_dice_type):
    positive_sample = []

    for dice_rank in os.listdir(os.path.join('assets\\Dices', positive_dice_type)):
        if positive_dice_type == 'Empty':
            positive_sample.append(os.path.join('assets\\Dices', positive_dice_type, dice_rank))
            continue

        for image_name in os.listdir(os.path.join('assets\\Dices', positive_dice_type, dice_rank)):
            positive_sample.append(os.path.join('assets\\Dices', positive_dice_type, dice_rank, image_name))
    
    for index, row in enumerate(positive_sample):

        image = cv.imread(row)
        image_width, image_height = image.shape[:2]
        positive_sample[index] = f'{row}  1  0 0 {image_width - 1} {image_height - 1}'
        print(positive_sample[index])

    
    print(len(positive_sample))

    with open(os.path.join('assets\\Model\\Assassin Strategy\\Assassin', 'pos.txt'), 'w') as file:
        for row in positive_sample:
            file.write(f'{row}\n')


if __name__ in '__main__':
    cascade_negative_samples('Assassin')
