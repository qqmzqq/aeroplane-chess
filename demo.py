from utils import *
from rules import BaseRules

if __name__ == '__main__':
    color = Switch()
    p_blue = Player(color.get_route("Blue"))
    p_green = Player(color.get_route("Green"))
    blue = BaseRules(p_blue)
    green = BaseRules(p_green)
    while True:
        try:
            blue.dice()
            green.dice()
        except DeportError as e:
            print(e)
