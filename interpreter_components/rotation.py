import enum


class Rotation(enum.Enum):
    UP, RIGHT, DOWN, LEFT = range(4)

    def __add__(self, other):
        return self.value + other
