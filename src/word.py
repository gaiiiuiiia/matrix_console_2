import random
from typing import Generator

from src import settings
from src.enums import Direction, UnknownDirectionException
from src.symbol import Symbol
from src.utils import Position, Boundary, get_random_position_in_boundary


class Word:
    def __init__(
            self,
            value: str,
            position: Position = Position(col=0, row=0),
            direction: Direction = Direction.DOWN,
            speed: int = settings.MIN_WORD_SPEED,
    ) -> None:
        self._value = str(value)
        self._position = position
        self._direction = direction
        self._speed = self._validate_speed(speed)
        self._symbols = self._construct_symbols()

    def _construct_symbols(self) -> tuple[Symbol]:
        symbols: list[Symbol] = []
        for i, _char in enumerate(self._value):
            position = self._get_offset_position(i)
            symbols.append(Symbol(_char, position))

        return tuple(symbols)

    def _get_offset_position(self, step: int) -> Position:
        match self._direction:
            case Direction.UP:
                return Position(col=self._position.col, row=self._position.row - step)
            case Direction.RIGHT:
                return Position(col=self._position.col + step, row=self._position.row)
            case Direction.DOWN:
                return Position(col=self._position.col, row=self._position.row + step)
            case Direction.LEFT:
                return Position(col=self._position.col - step, row=self._position.row)
            case _:
                raise UnknownDirectionException()

    @staticmethod
    def _validate_speed(speed: int) -> int:
        if speed > settings.MAX_WORD_SPEED:
            return settings.MAX_WORD_SPEED
        elif speed < settings.MIN_WORD_SPEED:
            return settings.MIN_WORD_SPEED
        return speed

    @property
    def symbols(self) -> tuple[Symbol]:
        return self._symbols

    @property
    def value(self) -> str:
        return self._value

    @property
    def position(self) -> Position:
        return self._position

    @property
    def direction(self) -> Direction:
        return self._direction

    @property
    def speed(self) -> int:
        return self._speed

    def __getitem__(self, item):
        return self._symbols[item]


def get_random_word(
        dictionary: list[str],
        boundary: Boundary,
        direction: Direction,
) -> Word:
    value = random.choice(dictionary)
    position = get_random_position_in_boundary(boundary)

    return Word(value, position, direction)


def word_generator(
        dictionary: list[str],
        boundary: Boundary,
        direction: Direction = Direction.DOWN,
) -> Generator[Word, None, None]:
    while True:
        yield get_random_word(dictionary, boundary, direction)
