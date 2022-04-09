"""
https://www.youtube.com/watch?v=XrCAvs9AePM&t=466s

Train Model:
"""
# C:\Users\caspe\Downloads\opencv\build\x64\vc15\bin\opencv_createsamples.exe -info assets\Model\Assassin_Strategy\Bounty\pos.txt -w 24 -h 24 -num 1000 -vec assets\Model\Assassin_Strategy\Bounty\pos.vec
# C:\Users\caspe\Downloads\opencv\build\x64\vc15\bin\opencv_traincascade.exe -data assets\Model\Assassin_Strategy\Assassin\model\ -vec assets\Model\Assassin_Strategy\Assassin\pos.vec -bg assets\Model\Assassin_Strategy\Assassin\neg.txt -numPos 100 -numNeg 400 -numStages 10 -w 24 -h 24

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
    
    print(len(negative_sample))

    with open(os.path.join('assets\\Model\\Assassin_Strategy', positive_dice_type, 'neg.txt'), 'w') as file:
        for row in negative_sample:
            file.write(f'{row}\n')


def cascade_positive_samples(positive_dice_type):
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
        # print(positive_sample[index])

    
    print(len(positive_sample))

    with open(os.path.join('assets\\Model\\Assassin_Strategy', positive_dice_type, 'pos.txt'), 'w') as file:
        for row in positive_sample:
            file.write(f'{row}\n')


if __name__ in '__main__':
    cascade_negative_samples('Joker')
    cascade_positive_samples('Joker')
