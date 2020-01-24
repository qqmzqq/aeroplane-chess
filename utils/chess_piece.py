from .chessboard import *


class ChessPiece:
    def __init__(self, color, index):
        self.color = color
        self.index = index
        self.position = 0
        self.status = -1

    def move(self, points):
        if self.status != -1 and self.status != 99:
            position = self.position + points
            if 2 == self.status:
                if position >= len(self.color.battlefield):
                    self.status = 99
                    raise MoveError("# This piece's mission is accomplished. #")
            if position > len(self.color.chessboard):
                self.status = 2
                self.position = position - len(self.color.chessboard)
            else:
                self.position = position
                self.status = 1
                self.shortcut()
        else:
            raise MoveError("# You cannot move piece in the hangar. #")

    def get_status(self):
        if -1 == self.status:
            return "In the hangar"
        elif 0 == self.status:
            return "Is ready"
        elif 1 == self.status:
            return "On the chessboard"
        elif 2 == self.status:
            return "On the battlefield"
        elif 99 == self.status:
            return "Mission accomplished"
        else:
            raise Exception("error")

    def set_status(self, status):
        self.status = status

    def reset(self):
        self.position = 0
        self.status = -1

    def shortcut(self):
        if self.position == self.color.shortcut[0]:
            self.position = self.color.chessboard[self.color.shortcut[1]]
            raise DeportError('# {0} pieces on the battlefield will be expelled back to the hangar #'.format(
                self.color.restraint()))

    def __str__(self):
        return "ChessPieces(color={0}, index={1}, status=\"{2}\", position={3})".format(
            self.color.get_color(), self.index, self.get_status(), self.color.chessboard[self.position])


class MoveError(Exception):
    pass


class DeportError(Exception):
    pass
