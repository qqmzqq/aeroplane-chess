from .chess_piece import ChessPiece, MoveError, DeportError
from .chessboard import Switch


class Player:
    def __init__(self, color):
        self.color = color
        self.available = 0
        self.finished = 0
        self.chess_pieces = [ChessPiece(self.color, x + 1) for x in range(4)]

    def reset(self):
        for chess_piece in self.chess_pieces:
            chess_piece.reset()

    def event(self, points):
        try:
            if points == 6:
                if self.available <= 4 and self.finished < 3:
                    print("What do you want to do:")
                    print(" * [1] Move a chess piece to the ready zone")
                    print(" * [2] Move a chess piece")
                    flag = int(input(" - "))
                    if flag in [1, 2]:
                        if 1 == flag:
                            piece = self.choose_piece()
                            if -1 != piece.status:
                                raise MoveError("# You can only move piece in the hangar. #")
                            piece.status = 0
                            self.flush_info()
                        if 2 == flag:
                            self.choose_piece().move(points)
                    else:
                        print("# You need to enter an integer (1 or 2) # ")
                        self.event(6)
            elif self.available > 0:
                self.choose_piece().move(points)
                self.flush_info()
        except MoveError as e:
            print(e)
            self.event(points)
        except DeportError as e:
            raise e
        except IndexError as e:
            print(e)
            self.event(points)
        except ValueError as e:
            print(e)
            self.event(points)

    def choose_piece(self):
        try:
            self.flush_info(True)
            index = int(input("Select a chess piece: \n - ")) - 1
            if index > len(self.chess_pieces) or index < 0:
                raise IndexError("Index out of range.")
            return self.chess_pieces[index]
        except ValueError as e:
            print(e)
            self.choose_piece()

    def flush_info(self, print_console=False):
        self.available = 0
        self.finished = 0
        for piece in self.chess_pieces:
            if print_console:
                print(piece)
            if -1 < piece.status <= 2:
                self.available += 1
            if piece.status == 99:
                self.finished += 1
        if self.finished == 4:
            raise FinishedError("")


class FinishedError(Exception):
    pass
