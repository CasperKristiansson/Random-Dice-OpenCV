""""""
import os
import cv2 as cv

class Processing:
    """This class main goal is to provide a easy
    way to navigate dices and pick the correct type.
    The class receives a list dices.

    :param dices: List of dices names
    :param raw_data_path: raw data path
    :param destination_path: destination path

    :return: None
    """
    def __init__(self, dices, raw_data_path='assets\Raw Data', destination_path='assets\Dices'):
        self.dices = dices
        self.raw_data_path = raw_data_path
        self.destination_path = destination_path

    def filter_data(self):
        """Iterates over the images in the raw data path
        and decides the dice type and rank.

        :return: None
        """
        for image_name in os.listdir(self.raw_data_path):
            image_path = os.path.join(self.raw_data_path, image_name)
            image = cv.imread(image_path)

            image = cv.resize(image, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)
            cv.imshow('Image', image)
            cv.waitKey(0)
            cv.destroyAllWindows()

            string = ' '.join(f'{dice}={index + 1}' for index, dice in enumerate(self.dices)) + ' Empty=0 Remove=-'

            print(string)
            dice_type = input('Enter Type: ')

            if dice_type == '-':
                os.remove(image_path)
                continue

            if int(dice_type) == 0:
                path = os.path.join(self.destination_path, 'Empty')
                os.rename(image_path, os.path.join(path, image_name))
                continue

            dice_rank = input('Enter rank: ')
            path = os.path.join(self.destination_path, os.path.join(self.dices[int(dice_type) - 1], f'Level {str(dice_rank)}'))

            if not os.path.exists(path):
                print(f"Path dose'nt exist: {path}")
                continue

            os.rename(image_path, os.path.join(path, image_name))


if __name__ == '__main__':
    dices = [
        'Assassin',
        'Bounty',
        'Joker',
        'Mimic',
        'Mine',
    ]

    processing = Processing(dices)
    processing.filter_data()
