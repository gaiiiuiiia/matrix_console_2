from enum import Enum


class UnknownDirectionException(Exception):
    pass

class Direction(int, Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4
