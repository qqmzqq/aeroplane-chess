from secrets import randbelow
from utils import *


class BaseRules:
    def __init__(self, user):
        self.dice_time = 0
        self.user = user

    def dice(self):
        try:
            if 3 > self.dice_time:
                points = randbelow(6) + 1
                print("「{0}」The points of dice are: {1}.".format(self.user.color.get_color(), points), end="")
                if 6 == points:
                    print("Get an extra chance to roll the dice!")
                    self.dice_time += 1
                    self.user.event(points)
                    self.dice()
                else:
                    print()
                    self.user.event(points)
            else:
                points = randbelow(6) + 1
                print("「{0}」The points of dice are: {1}.".format(self.user.color.get_color(), points), end="")
                if 6 == points:
                    self.user.reset()
                    self.dice_time = 0
                    print("Are you cheating? All your chess pieces will return to the hangar.")
                else:
                    print()
                    self.user.event(points)
        except DeportError as e:
            raise e
        except Exception as e:
            raise e
