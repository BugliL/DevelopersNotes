class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x} {self.y}"


class Direction(object):
    NORD = 'N'
    SOUTH = 'S'
    EAST = 'E'
    WEST = 'W'

    def __init__(self, d):
        self.d = d

    def __str__(self):
        return str(self.d)


class DirectedPosition(object):
    def __init__(self, x, y, d):
        self.d = Direction(d)
        self.p = Position(x, y)

    def __str__(self):
        return f"{self.p} {self.d}"


class Rover(object):

    def __init__(self, x, y, d):
        # self.dp = DirectedPosition(x, y, d)
        self.x = x
        self.y = y
        self.d = d

    def __str__(self):
        return str(DirectedPosition(self.x, self.y, self.d))  # "{self.x} {self.y} {self.d}"

    def command(self, c):
        for a in c:
            if a == 'F':
                self.move_forward()
            # elif a == 'B':
            #     self.move_backward()

            #
            # if d == 'N':
            # # self
            # elif d == 'S':
            # elif d == 'W':
            # elif d == 'E':

        return str(self)
        # if 'F':

    def move_forward(self):
        if self.d == Direction.NORD:
            self.y += 1
        elif self.d == Direction.WEST:
            self.x -= 1
        elif self.d == Direction.EAST:
            self.x += 1
        elif self.d == Direction.SOUTH:
            self.y -= 1

        # elif d == 'W':

    def move_backward(self):
        pass

    def get_position(self):
        pass
