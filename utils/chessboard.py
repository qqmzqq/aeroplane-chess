

class Chessboard:
    def __init__(self):
        self.chessboard = [x for x in range(1, 53)]
        self.battlefield = [x for x in range(1, 7)]
        self.shortcut = [10, 22]

    def generate_route(self, index):
        if 0 == index:
            return self.chessboard[:43]
        source = index * 7 + index * 6
        destination = source + 43 - len(self.chessboard)
        return self.chessboard[source:52] + self.chessboard[:destination]

    def get_color(self):
        pass

    def restraint(self):
        pass


class Blue(Chessboard):
    def __init__(self):
        super(Blue, self).__init__()
        self.index = 0
        self.chessboard = self.generate_route(self.index)

    def get_color(self):
        return "Blue"

    def restraint(self):
        return "Green"


class Yellow(Chessboard):
    def __init__(self):
        super(Yellow, self).__init__()
        self.index = 1
        self.chessboard = self.generate_route(self.index)

    def get_color(self):
        return "Yellow"

    def restraint(self):
        return "Red"


class Green(Chessboard):
    def __init__(self):
        super(Green, self).__init__()
        self.index = 2
        self.chessboard = self.generate_route(self.index)

    def get_color(self):
        return "Green"

    def restraint(self):
        return "Blue"


class Red(Chessboard):
    def __init__(self):
        super(Red, self).__init__()
        self.index = 3
        self.chessboard = self.generate_route(self.index)

    def get_color(self):
        return "Red"

    def restraint(self):
        return "Yellow"


class Switch:
    def __init__(self):
        self.color = {
            "Blue": Blue(),
            "Yellow": Yellow(),
            "Green": Green(),
            "Red": Red()
        }

    def get_route(self, color):
        return self.color.get(color)
